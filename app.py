import gradio as gr
import pickle
import numpy as np

scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('regressor.pkl','rb'))

def calculate_goldrate(usd_inr):
    scaled_input = scaler.transform(np.array(usd_inr).reshape(1,-1))
    return round(model.predict(scaled_input)[0][0],2)

demo = gr.Interface(
    fn=calculate_goldrate,
    inputs=["number"],
    outputs=["number"],
    title="Gold Rate Calculator"
)

demo.launch(server_name="0.0.0.0", server_port=7860, share=False)