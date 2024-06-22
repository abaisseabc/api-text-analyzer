from flask import Blueprint, request
from flask_cors import cross_origin

analyzer = Blueprint("analyzer", __name__)


@analyzer.route("/analyze/", methods=["POST"])
@cross_origin()
def analyze_test():
    pass
