from flask import Blueprint, request
from flask_cors import cross_origin

from .machine_text_detector import MachineTextDetector

analyzer = Blueprint("analyzer", __name__)


@analyzer.route("/analyze/", methods=["POST"])
@cross_origin()
def analyze_test():
    try:
        user_data = request.get_json()
        machine, human = MachineTextDetector().get_result_analysis(user_data["text"])
        return {
            "status": "success",
            "data": {
                "human": human,
                "machine": machine,
            },
            "message": "Проверка текста прошла успешно!"
        }
    except Exception as err:
        return {
            "status": "error",
            "data": None,
            "message": f"Произошла ошибка: {err}"
        }
