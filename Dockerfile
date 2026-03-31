# 1. 建议使用更轻量但兼容性极好的基础镜像
FROM python:3.10-slim

# 2. 合并安装系统依赖，减少镜像层数
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. 分两步复制：先复制依赖文件（如果有 requirements.txt 的话）
# 如果没有，直接 RUN pip 也没问题，但加上 --upgrade 确保 YOLO 处于最佳状态
RUN pip install --no-cache-dir --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir flask flask-cors ultralytics numpy opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

# 4. 复制项目文件
COPY . /app

# 5. 声明端口
EXPOSE 5000

# 6. 使用 python 直接启动即可（slim 镜像中 python 默认就在环境变量里）
# 加上 -u 参数可以实时刷新日志，方便你用 docker logs -f 查看
CMD ["python", "-u", "app.py"]