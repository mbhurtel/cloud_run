import gradio as gr
import requests

import os.path as osp
import sys
sys.path.append(osp.abspath(osp.join(osp.dirname(__file__), '..')))

from main import main

BASE_URL = "http://localhost:4000"

OPERATIONS = ["Union", "Intersection", "Difference"]

def clean_input(user_set):
    return list(set(user_set.split(',')))

def get_inputs_and_process(operation, setA, setB):
    operation = operation.lower()
    setA = clean_input(setA)
    setB = clean_input(setB)

    # Here we call the api endpoints (setA)
    response = requests.post(f"{BASE_URL}/setA", json={"setA": setA})

    if response.status_code == 200:
        result = response.json()
        setA = result.get("setA", [])
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

    # Here we call the api endpoints (setB)
    response = requests.post(f"{BASE_URL}/setB", json={"setB": setB})

    if response.status_code == 200:
        result = response.json()
        setB = result.get("setB", [])
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

    # Now we call the performOperation endpoint
    payload = {
        "operation": operation,
        "setA": setA,
        "setB": setB,
    }
    
    response = requests.post(f"{BASE_URL}/performOperation", json=payload)
    if response.status_code == 200:
        result = response.json()
        return result.get("opResult", "No result returned from API.")
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"
    
def initialize_UI_project():
    inputs = [
        gr.Dropdown(
            OPERATIONS,
            label="User Operation",
            info="Please select a set operation."
        ),
        gr.Textbox(
            label="Set A",
            info="Enter the content of set A with comma separated value"
        ),
        gr.Textbox(
            label="Set B",
            info="Enter the content of set B with comma separated value"
        )
    ]

    output = gr.Textbox(label="Results")
    app = gr.Interface(
        fn=get_inputs_and_process,
        inputs=inputs,
        outputs=output,
        title="Set Operations",
        description="Select an operation, provide Set A and Set B, and the get the result."
    )

    return app

app = initialize_UI_project()
app.launch()
