# 🚀 Web-AI-Detection-Server

> **基于 YOLOv8 + Flask + Docker 的高性能视觉推理 Web 服务**

本项目提供了一个完整的 AI 图像检测解决方案。通过 Docker 容器化技术，将复杂的深度学习环境（CUDA, PyTorch, Ultralytics）封装，实现跨平台的“秒级”部署。

---

## 🌟 项目核心亮点 (Highlights)

* **⚡ GPU 算力无损穿透**：针对 **WSL2 + NVIDIA RTX 4060** 环境深度优化，推理延迟低至 **70ms**，充分压榨本地显卡性能。
* **📦 生产级容器化**：基于 `python:3.10-slim` 精简镜像，通过 Docker 实现环境的像素级复现，彻底告别“我本地能跑，你那里不行”的尴尬。
* **🛠️ 极致部署体验**：支持通过 **Cloudflare Tunnel** 进行内网穿透，配合自动化别名脚本，实现公网一键发布。
* **📂 规范化工程管理**：严格的 `.gitignore` 配置，仅同步核心代码与配置文件，确保 Git 仓库轻量、专业。

---

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
确保你的 Linux (WSL2 Ubuntu) 系统已安装：
* **Docker Engine** (推荐 24.0+)
* **NVIDIA Container Toolkit** (用于 Docker 调用显卡驱动)

### 2. 获取代码
```bash
git clone [https://github.com/924zbh/Web-AI-Detection-Server.git](https://github.com/924zbh/Web-AI-Detection-Server.git)
cd Web-AI-Detection-Server
3. 构建并运行如果你是第一次运行，请构建镜像（预计耗时 3-5 分钟）：Bashdocker build -t ai-detection-service .
启动容器并挂载图片存放目录：Bashdocker run -d --name ai-worker --gpus all --restart always \
  -p 5000:5000 \
  -v $(pwd)/static/uploads:/app/static/uploads \
  ai-detection-service
4. 访问服务打开浏览器访问：http://localhost:5000🛠️ 技术栈 (Tech Stack)维度技术方案核心算法Ultralytics YOLOv8 (Inference Only)后端框架Flask 3.0.3容器技术Native Docker Engine开发环境WSL2 (Ubuntu 22.04)硬件加速NVIDIA GeForce RTX 4060 (16GB RAM)📂 目录结构说明Plaintext.
├── app.py              # Flask 后端推理核心逻辑
├── Dockerfile          # 多阶段构建镜像配置文件
├── .gitignore          # 动态数据/本地测试文件屏蔽规则
├── static/             # 前端静态资源 (CSS/JS/Images)
│   └── uploads/        # 图片处理工作流目录 (已被忽略追踪)
├── templates/          # Web 界面模板 (磨砂玻璃风格)
└── yolov8n.pt          # 轻量化检测模型权重
👤 作者zbhSchool: Nanchang Vocational UniversityMajor: Artificial IntelligenceGitHub: 924zbh