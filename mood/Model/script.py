import ktrain
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def getEmotion(str):
    predictor = ktrain.load_predictor(os.path.join(__location__, 'iMood_model'))
    resp = predictor.predict(str)
    return resp
