from ultralytics import YOLO
import os

def run_inference():
    # 1. 加载模型（如果本地没有，它会自动下载）
    model = YOLO('yolov8n.pt')

    # 2. 执行推理
    # source='bus.jpg' 使用你目录下的示例图
    # save=True 会将识别结果保存到 runs/detect 目录下
    # device=0 强制使用你的第一块显卡 (RTX 4060)
    print("正在启动 RTX 4060 进行推理...")
    results = model.predict(project='.',name='runs/detect',source='bus.jpg', save=True, device=0)

    # 3. 打印结果摘要
    for result in results:
        boxes = result.boxes
        print(f"成功识别到 {len(boxes)} 个目标！")
        print(f"结果已保存至: {result.save_dir}")

if __name__ == "__main__":
    run_inference()
