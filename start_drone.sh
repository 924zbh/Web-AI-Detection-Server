#!/bin/bash

# --- 核心修改：自动定位脚本所在目录 ---
# 无论你把项目文件夹放在哪，这行代码都能自动找到它，不需要写死路径
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT" || exit

# 1. 变量定义
IMAGE_NAME="drone-server"
REMOTE_IMAGE="ghcr.io/924zbh/drone-detection:v1.0"
CONTAINER_NAME="drone-instance"

echo "📂 自动识别到项目路径: $PROJECT_ROOT"
echo "🚀 正在检查并构建本地 Docker 镜像..."
docker build -t $IMAGE_NAME .

echo "🔥 正在清理旧容器..."
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "🍀 正在启动加速容器..."
docker run -d \
  --name $CONTAINER_NAME \
  --gpus all \
  -p 5000:5000 \
  $IMAGE_NAME

echo "✅ 服务已在后台启动！"
echo "🌐 请访问: http://localhost:5000"
echo "📝 查看日志: docker logs -f $CONTAINER_NAME"

# 2. 新增：云端同步判断逻辑
echo ""
read -p "是否同时将更新推送到 GitHub 云端? (y/n): " confirm
if [ "$confirm" == "y" ]; then
    echo "⬆️ 正在推送到 GitHub Packages..."
    docker tag $IMAGE_NAME $REMOTE_IMAGE
    docker push $REMOTE_IMAGE
    echo "✨ 云端镜像已同步成功！"
else
    echo "👌 已跳过云端推送，仅在本地运行。"
fi
