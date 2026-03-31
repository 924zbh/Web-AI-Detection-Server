# 🚁 Drone-Object-Detection-Server (Web Edition)

> **基于 YOLOv8 + Flask + Docker 的全流程无人机视觉检测方案**

本项目专为 AI 开发者及学术研究设计，实现了从底层硬件加速到前端可视化展示的完整闭环。目前已在 **Ubuntu 22.04 (WSL2) + 原生 Docker Engine** 环境下经过深度测试。

---

## 🌟 项目亮点 (Highlights)

* **📦 纯粹 Linux 环境**：直接运行于原生 Docker Engine，摆脱 Docker Desktop 的资源损耗，推理响应更迅捷。
* **⚡ GPU 穿透技术**：通过 **NVIDIA Container Toolkit** 实现宿主机与容器间的算力无损穿透，推理延迟低至 **70ms**。
* **🛠️ 自动化运维**：推荐配合 `.bashrc` 别名脚本，实现容器销毁、镜像构建、服务重启与 Cloudflare 隧道打通的自动化流转。
* **📂 专业代码管理**：精细化 `.gitignore` 配置，确保 GitHub 仓库只保留核心逻辑，本地保留测试图片与运行日志。

---

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
确保你的 Linux (WSL2 Ubuntu) 系统已安装：
* **Docker Engine** (docker-ce)
* **NVIDIA Container Toolkit** (用于 Docker 调用 GPU 驱动)

### 2. 克隆指定分支
```bash
git clone -b web-image-detection [https://github.com/924zbh/Drone-Object-Detection.git](https://github.com/924zbh/Drone-Object-Detection.git)
cd Drone-Object-Detection
3. 构建并运行如果您是第一次运行，请先构建 Docker 镜像：巴什docker build -t drone-cv .
启动集装箱（建议挂载本地static/uploads 目录以便持久化图片）：巴什docker run -d --name drone-worker --gpus all --restart always \
  -p 5000:5000 \
  -v $(pwd)/static/uploads:/app/static/uploads \
  drone-cv
4. 访问服务打开浏览器访问：（http://localhost:5000或通过您的 Cloudflare 域名访问）🛠️ 技术栈（技术堆栈）维度技术方案核心算法Ultralytics YOLOv8（推理）顶层框架Flask 3.0.3容器技术原生 Docker 引擎方便环境WSL2（Ubuntu 22.04）硬件设施NVIDIA GeForce RTX 4060（16GB 显存）📂 目录结构说明纯文本.
├── app.py              # Flask 后端核心逻辑
├── Dockerfile          # 生产级环境镜像配置文件
├── .gitignore          # 动态数据/权重忽略规则
├── static/             # 前端静态资源 (CSS/JS)
│   └── uploads/        # 检测图片存放地 (挂载点)
├── templates/          # HTML 模板 (磨砂玻璃 UI)
└── yolov8n.pt          # 预训练模型权重
.
作者924zbh学校：南昌职业大学专业：人工智能