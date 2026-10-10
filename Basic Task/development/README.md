# 开发区域
- 所选方向：Infra
- 最终分支：master
- 最终 commit SHA：1960806
## 项目简介

本项目为 ANTLab Infra 方向基础任务：为不超过 10 人的小工作室搭建本地 GPU 推理服务，支持办公文档处理和辅助编程，并开发性能测试、文件存储、前端展示与服务恢复功能。

## 系统结构

- `src/`：测试脚本（单请求、多并发、文件读取、异常恢复）和前端页面
- `configs/`：服务启动配置
- `tests/`：功能验证和异常恢复测试
- `results/`：原始数据、汇总统计
- `reports/`：书面报告

## 环境依赖

- WSL 2 + Ubuntu 24.04
- CUDA 13.2
- llama.cpp (b11528-e60eff95f)
- 模型：Qwen3-0.6B-GGUF Q8_0

## 运行方法

1. 启动服务：`cd ~/llama.cpp && ./build/bin/llama-server -m ~/models/Qwen3-0.6B-Q8_0.gguf --host 0.0.0.0 --port 8080`
2. 单请求测试：`python3 src/test_single.py`
3. 多并发测试：`python3 src/test_concurrent.py`
4. 文件读取测试：`python3 src/test_file.py`
5. 异常恢复测试：`python3 src/test_recovery.py`
6. 前端展示：`cd src/frontend && python3 -m http.server 3000`，浏览器打开 `http://localhost:3000`

## 报告与数据位置

- 报告：`reports/基础阶段考核报告.md`
- 原始数据：`results/*.json`
