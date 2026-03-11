🚁 Drone-Object-Detection-Server
基于 YOLOv8 + Flask + Docker 的高性能无人机目标检测云服务器

🌟 项目亮点 (Highlights)
本项目实现了一个完整的 AI 推理闭环，从底层硬件加速到前端可视化展示：

GPU 加速推理：利用 WSL2 穿透技术，在 Docker 容器内调用宿主机 NVIDIA GeForce RTX 4060 算力。

一键式部署：通过 Dockerfile 封装所有环境（CUDA, PyTorch, Ultralytics），解决复杂的依赖问题。

交互式 Web 界面：前端采用蓝色工业风设计，支持拖拽上传图片并实时查看检测结果。

高性能架构：基于 Flask 后端，推理延迟低至 70ms 左右（使用 YOLOv8n 模型）。

🚀 快速开始 (Quick Start)
1. 环境准备
确保你的 Windows 已开启 WSL2，并安装了 Docker Desktop 以及 NVIDIA Container Toolkit。

2. 克隆仓库
3. 构建并运行 (Docker方式)
这是最推荐的方式，不需要在本地配置任何 Python 环境：

4. 访问服务
打开浏览器，访问：
http://localhost:5000

🛠️ 技术栈 (Tech Stack)
Core AI: 

Backend: Flask (Python)

Containerization: Docker (NVIDIA Runtime)

Hardware: NVIDIA RTX 4060 (16GB RAM)

Environment: WSL2 + Ubuntu 22.04

📂 项目结构 (Project Structure)
📸 运行截图 (Demo)
(建议在此处上传一张你浏览器运行成功的截图，重命名为 demo.png 并放在仓库里)

💡 未来计划 (Roadmap)
[ ] 支持实时视频流推理 (RTSP/RTMP)

[ ] 增加检测结果自动保存到数据库的功能

[ ] 适配更精准的 YOLOv8m/l 模型

✍️ 操作建议：
在 WSL2 终端输入 nano README.md。

清空原有内容，把上面这段贴进去。

保存退出后执行：

git add README.md

git commit -m "docs: 更新专业版 README"

git push
