import os, time, cv2, sys
import numpy as np
from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO

app = Flask(__name__)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 路径配置
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RES_DIR = os.path.join(BASE_DIR, 'static', 'uploads', 'results')
os.makedirs(RES_DIR, exist_ok=True)

# 加载模型 (开启半精度加速)
model = YOLO('yolov8l.pt') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    # 1. 检查文件
    file = request.files.get('image')
    if not file:
        return jsonify({"status": "error", "error": "未收到图片"}), 400

    try:
        # 2. 【核心优化】从请求流中直接读取二进制数据到内存
        file_bytes = file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"status": "error", "error": "图片解码失败"}), 400

        # 3. 推理 (直接传递内存中的图像数组)
        # imgsz=640 与前端压缩尺寸对齐，half=True 开启 4060 的半精度加速
        results = model.predict(source=img, device=0, imgsz=640, half=True,conf=0.7)
        
        # 4. 在内存中绘制结果图
        res_img = results[0].plot()

        # 5. 保存结果图到硬盘 (用于前端展示)
        ts = time.strftime("%Y%m%d_%H%M%S")
        res_filename = f"res_{ts}.jpg"
        res_path = os.path.join(RES_DIR, res_filename)
        cv2.imwrite(res_path, res_img)

        # 6. 立即返回结果
        return jsonify({
            "status": "success", 
            "res_url": f"static/uploads/results/{res_filename}"
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)