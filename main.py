import gradio as gr
from litellm import completion
import os

def get_model_response(api_key, user_input):
    os.environ['GROQ_API_KEY'] = api_key
    response = completion(
        model="groq/llama3-8b-8192",
        messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

def create_gradio_interface():
    with gr.Blocks() as demo:
        with gr.Row():
            api_key_input = gr.Textbox(
                label="API KEY",
                placeholder="Enter API KEY here",
                type="password"
            )
        with gr.Row():
            user_input = gr.Textbox(
                label="Enter your prompt",
                placeholder="...",
                lines=2
            )
        with gr.Row():
            output = gr.Textbox(label="Answer:", lines=5, interactive=False)
        with gr.Row():
            submit_btn = gr.Button("Submit")
            clear_btn = gr.Button("Clear")


        submit_btn.click(get_model_response, inputs=[api_key_input, user_input], outputs=output)
        clear_btn.click(lambda: "", None, output)

    demo.launch(server_name="0.0.0.0", server_port=8080)

create_gradio_interface()
