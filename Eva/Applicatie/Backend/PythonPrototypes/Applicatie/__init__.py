import os

from flask import Flask, jsonify, request
from flask import send_file
from flask_cors import CORS

from Applicatie.UsecaseControllers.VisualizeVariablesController import VisualizeVariablesController
from ResourceHandlerFactory import ResourceHandlerFactory

app = Flask(__name__)
cors = CORS(app)


@app.route('/uploadFile', methods=['POST'])
def upload():
    file = "uploadedFile.xlsx"
    path = "./"
    request.files['file'].save(path + file)
    controller = VisualizeVariablesController()
    try:
        controller.load(path + file)
        os.remove(path + file)
        return jsonify(succes=True)
    except Exception as error:
        return jsonify(error)


@app.route('/getCriteria', methods=['GET'])
def get_criteria():
    controller = VisualizeVariablesController()
    try:
        return jsonify(controller.get_criteria())
    except:
        return jsonify(succes=False)


@app.route('/filter', methods=['POST'])
def filter():
    json = request.data.decode()
    controller = VisualizeVariablesController()
    try:
        index = controller.filter(str(json))
        return jsonify(index)
    except Exception as error:
        return jsonify(error)

@app.route('/getProperties', methods=['GET'])
def get_properties():
    controller = VisualizeVariablesController()
    try:
        return jsonify(controller.get_properties())
    except Exception as error:
        return jsonify(error)


@app.route('/Execute', methods=['POST'])
def execute():
    data = request.data.decode()
    controller = VisualizeVariablesController()
    try:
        return send_file(controller.execute(data), mimetype='image/png')
    except Exception as error:
        raise Exception(error)


if __name__ == '__main__':
    app.run("127.0.0.1", 4201, debug=True)
    resource_factory = ResourceHandlerFactory()
    resource_handler = "git"
    handler = resource_factory.get_resource_handler(resource_handler)
    handler.download_scripts()
