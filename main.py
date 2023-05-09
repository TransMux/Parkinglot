import gradio as gr

from utils.ui import load_json, json_files

with gr.Blocks() as demo:
    with gr.Accordion("Database Debug", open=False):
        with gr.Row():
            json_a = gr.JSON(load_json("./data/db/车辆信息.json"), label="车辆信息")
            json_b = gr.JSON(load_json("./data/db/停车场信息.json"), label="停车场信息")
            json_c = gr.JSON(load_json("./data/db/停车记录.json"), label="停车记录")

        json_refresh = gr.Button(value="刷新")

        json_refresh.click(json_files, outputs=[json_a, json_b, json_c])

if __name__ == '__main__':
    demo.launch()
