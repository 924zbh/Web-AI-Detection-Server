from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8l.pt')

# 任务 B：识别视频流（验证实时性）

model.track(conf=0.7, half=True, imgsz=640, source='0', show=True, device=0)
