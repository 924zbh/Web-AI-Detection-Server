# 使用 Ultralytics 作为底座
FROM ultralytics/ultralytics:latest

# 安装 Web 框架
RUN pip install flask

# 设置工作目录并复制你的代码
WORKDIR /app
COPY . /app

# 暴露端口
EXPOSE 5000

# 启动服务器
CMD ["python3", "app.py"]
