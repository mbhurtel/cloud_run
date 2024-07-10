import gradio as gr

import os.path as osp
import sys
sys.path.append(osp.abspath(osp.join(osp.dirname(__file__), '..')))

from main import main

OPERATIONS = ["Union", "Intersection", "Difference"]

def validate_input(user_set):
    return set(user_set.split(','))

def get_inputs_and_process(operation, setA, setB):
    operation = operation.lower()
    setA = validate_input(setA)
    setB = validate_input(setB)

    result = main(operation, setA, setB)
    return str(result)
    
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
