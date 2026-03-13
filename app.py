from flask import Flask, request, send_file
from ultralytics import YOLO
import io
from PIL import Image
import numpy as np

app = Flask(__name__)

# 在启动时加载模型，避免每次请求都重新加载，提高速度
# 它会识别并利用你的 RTX 4060
model = YOLO('yolov8l.pt')

@app.route('/')
def index():
    # 返回我们刚才创建的网页首页
    try:
        return send_file('index.html')
    except Exception as e:
        return f"找不到 index.html 文件，请确保它在同一目录下。错误: {str(e)}"

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "请上传图片", 400

    file = request.files['image']
    
    # 1. 读取上传的图片
    img = Image.open(file.stream)

    # 2. 使用 GPU (device=0) 进行推理
    # results 是一个列表，包含检测到的框、类别等信息
    results = model.predict(source=img, device=0, save=False,imgsz=640)

    # 3. 将检测框画在图片上 (plot() 返回的是 BGR 格式的 numpy 数组)
    res_plotted = results[0].plot()

    # 4. 转换格式：OpenCV 的 BGR 格式转为 PIL 的 RGB 格式
    res_img = Image.fromarray(res_plotted[:, :, ::-1])

    # 5. 将处理后的图片保存到内存缓冲区，直接发回给浏览器
    img_io = io.BytesIO()
    res_img.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    # host='0.0.0.0' 让局域网内的其他设备也能通过你的 IP 访问
    app.run(host='0.0.0.0', port=5000)
