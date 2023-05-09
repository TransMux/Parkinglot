import gradio as gr

from storage import car_entry, car_leave
from utils.ui import load_json, json_files

with gr.Blocks() as demo:
    with gr.Accordion("Database Debug", open=False):
        with gr.Row():
            json_a = gr.JSON(load_json("./data/db/车辆信息.json"), label="车辆信息")
            json_b = gr.JSON(load_json("./data/db/停车场信息.json"), label="停车场信息")
            json_c = gr.JSON(load_json("./data/db/停车记录.json"), label="停车记录")

        json_refresh = gr.Button(value="刷新")

        json_refresh.click(json_files, outputs=[json_a, json_b, json_c])

    with gr.Tab("API Debug"):
        with gr.Row():
            with gr.Column():
                # def car_entry(car_id: str, car_type: str, car_image: Optional[str, Path], car_park: str):
                car_id = gr.Textbox(label="车牌号")
                car_type = gr.Radio(["小型车", "中型车", "大型车"], label="车辆类型")
                car_image = gr.Image(label="车辆图片")
                car_park = gr.Radio(["停车场1", "停车场2", "停车场3"], label="停车场")

                car_entry_button = gr.Button("车辆入场")
                car_entry_button.click(car_entry, [car_id, car_type, car_image, car_park])

            with gr.Column():
                # def car_leave(car_id: str, car_image: Optional[str, Path]):
                car_leave_id = gr.Textbox(label="车牌号")
                car_leave_image = gr.Image(label="车辆图片")

                car_leave_button = gr.Button("车辆离场")
                car_leave_button.click(car_leave, [car_leave_id, car_leave_image])

if __name__ == '__main__':
    demo.launch()
