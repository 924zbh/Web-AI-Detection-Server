#!/bin/bash

# 1. 进入项目目录
cd "$(dirname "$0")" || exit

echo "🚀 正在检查并构建 Docker 镜像..."
docker build -t drone-server .

echo "🔥 正在启动 RTX 4060 加速容器..."
# 如果已有同名容器在跑，先停掉
docker stop drone-instance 2>/dev/null || true
docker rm drone-instance 2>/dev/null || true

# 启动容器
docker run -d \
  --name drone-instance \
  --gpus all \
  -p 5000:5000 \
  drone-server

echo "✅ 服务已在后台启动！"
echo "🌐 请访问: http://localhost:5000"
echo "📝 输入 'docker logs -f drone-instance' 查看运行日志"
