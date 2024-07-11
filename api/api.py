from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS

import logging

import os.path as osp
import sys
sys.path.append(osp.abspath(osp.join(osp.dirname(__file__), '..')))
from main import main

# Initialize the Flask app and API
app = Flask(__name__)

# Cross Origin Resource Sharing
CORS(app)

api = Api(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

result = ""

def validate_set(user_set):
    if type(user_set) != set:
        return False
    
    return True

class SetAResource(Resource):
    def post(self):
        """
        This function takes the setA from the user, checks if it is empty, and returns
        """
        try:
            data = request.json
            setA = data.get("setA", [])
            if not setA:
                return {"message": "Set is Empty"}, 400

            if not validate_set(set(setA)):
                return {"message": "setA is not a Set!"}, 400
            
            return {"setA": setA}, 200

        except Exception as e:
            error_msg = f"Error fetching the set: {e}"
            logger.error(error_msg)
            return {"message": error_msg}, 500

class SetBResource(Resource):
    def post(self):
        """
        This function takes the setA from the user, checks if it is empty, and returns
        """
        try:
            data = request.json
            setB = data.get("setB", [])
            if not setB:
                return {"message": "Set is Empty"}, 400

            if not validate_set(set(setB)):
                return {"message": "setB is not a Set!"}, 400
            
            return {"setB": setB}, 200

        except Exception as e:
            error_msg = f"Error fetching the set: {e}"
            logger.error(error_msg)
            return {"message": error_msg}, 500

class OperationsResource(Resource):
    def post(self):
        """
        This function takes the setA from the user, checks if it is empty, and returns
        """
        try:
            data = request.json
            operation = data.get("operation", "")
            setA = data.get("setA", [])
            setB = data.get("setB", [])

            if not operation or not setB or not setA:
                return {"message": "Missing parameters"}, 400

            logger.info(f"Operation: {operation}")
            logger.info(f"Set A: {setA}")
            logger.info(f"Set B: {setB}")
            
            global result
            result = main(operation, set(setA), set(setB))
            
            return {"opResult": list(result)}, 200

        except Exception as e:
            error_msg = f"Error fetching the set: {e}"
            logger.error(error_msg)
            return {"message": error_msg}, 500
    
class ResultsResource(Resource):
    def get(self):
        return result, 200

# Here we define the API endpoints
api.add_resource(SetAResource, '/setA')
api.add_resource(SetBResource, '/setB')
api.add_resource(OperationsResource, '/performOperation')
api.add_resource(ResultsResource, '/results')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)