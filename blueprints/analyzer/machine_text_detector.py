import re
import language_tool_python
import spacy

from collections import Counter


class MachineTextDetector:
    def __init__(self, language="ru"):
        self.tool = language_tool_python.LanguageTool(language)
        self.nlp = spacy.load("ru_core_news_sm")

    @staticmethod
    def split_sentences(text: str) -> list:
        sentences = re.split(r"[.!?]", text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    @staticmethod
    def average_sentence_length(sentence: str) -> int:
        """
        Проверка среднего количества слов в предложении
        :param sentence:
        :return:
        """
        return len(sentence.split())

    @staticmethod
    def rare_words_ratio(sentence: str) -> float:
        """
        Проверка частоты использования редких слов
        :param sentence:
        :return:
        """
        words = sentence.split()
        word_counts = Counter(words)
        rare_words = [word for word in words if word_counts[word] == 1]
        return len(rare_words) / len(words)

    def grammar_errors_count(self, sentence: str) -> int:
        """
        Грамматический анализ
        :param sentence:
        :return:
        """
        matches = self.tool.check(sentence)
        return len(matches)

    def coherence_score(self, sentence: str) -> float:
        """
        Семантический анализ
        :param sentence:
        :return:
        """
        doc = self.nlp(sentence)
        sents = list(doc.sents)
        if not sents:
            return 1.0
        coherence_scores = [sent.similarity(doc) for sent in sents]
        return sum(coherence_scores) / len(coherence_scores)

    def analyze_sentence(self, sentence: str) -> str:
        avg_length = self.average_sentence_length(sentence)
        rare_ratio = self.rare_words_ratio(sentence)
        grammar_errors = self.grammar_errors_count(sentence)
        coherence = self.coherence_score(sentence)

        if avg_length > 20:
            return "machine"

        if rare_ratio > 0.5:
            return "machine"

        if grammar_errors < 2:
            return "machine"

        if coherence < 0.5:
            return "machine"

        return "human"

    def analyze_text(self, text: str):
        sentences = self.split_sentences(text)
        total_sentences = len(sentences)

        if total_sentences == 0:
            return 0.0, 0.0, []

        machine_generated_count = 0
        sentence_analysis = []

        for sentence in sentences:
            result = self.analyze_sentence(sentence)
            sentence_analysis.append((sentence, result))
            if result == "machine":
                machine_generated_count += 1

        human_generated_count = total_sentences - machine_generated_count
        machine_generated_percentage = (machine_generated_count / total_sentences) * 100
        human_generated_percentage = (human_generated_count / total_sentences) * 100

        return machine_generated_percentage, human_generated_percentage, sentence_analysis

    def get_result_analysis(self, text: str):
        machine_percentage, human_percentage, analysis = self.analyze_text(text)
        sentences_ai = [
            {
                "sentence": sentence,
                "result": result
            }
            for sentence, result in analysis
        ]
        return f"{machine_percentage:.2f}", f"{human_percentage:.2f}", sentences_ai
