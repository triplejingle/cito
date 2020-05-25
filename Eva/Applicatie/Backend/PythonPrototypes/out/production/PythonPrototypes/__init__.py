from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)


app = Flask(__name__)
cors = CORS(app)


@app.route('/uploadFile', methods=['POST'])
def upload():
    # print(request)
    # print(request.form)
    # print(request.get_json())
    # json = request.get_json()
    # path = request.form.get("path")
    # if path is None:
    #    for var in json:
    #        path = json[var]
    # print("path:==="+path)
    path = "C:/dev/PythonPrototypes/Inladen/Test/Inladen/sources/test_inladen.xlsx"
    inladen = Controller()
    inladen.inladen(path)
    return jsonify(succes=True)


@app.route('/getCriteria', methods=['GET'])
def getCriteria():
    controller = Controller()
    return jsonify(controller.get_criteria())


@app.route('/filter', methods=['POST'])
def filter():
    json = request.get_json()
    controller = Controller()
    index = controller.filter(json)
    return jsonify(index)


if __name__ == '__main__':
    app.run(debug=True)
