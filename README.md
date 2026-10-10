# ANTLab Infra Tasks

## 提交信息

| 项目 | 内容 |
|---|---|
| 所选方向 | Infra（大模型推理优化） |
| 完成阶段 | 基础阶段 + 进阶阶段 |
| 最终分支 | master |
| 最终版本标签 | submission-v1 |
| 最终 commit SHA | 1361ab3 |
| 该 SHA 指向的版本 | 包含全部源码、实验数据、报告与配图的定版提交 |
| 完成日期 | 2026-10-10 |

## 定位入口

- 基础任务：`Basic Task/development/`
- 进阶任务：`Advanced Task/development/`

## 文件索引

| 内容 | 位置 |
|---|---|
| 基础任务报告 | `Basic Task/development/reports/基础阶段考核报告.md` |
| 进阶任务报告 | `Advanced Task/development/reports/进阶阶段考核报告.md` |
| 基础任务源码 | `Basic Task/development/src/` |
| 进阶任务源码 | `Advanced Task/development/src/` |
| 基础任务数据 | `Basic Task/development/results/` |
| 进阶任务数据 | `Advanced Task/development/results/` |
| 前端展示 | `Advanced Task/development/src/frontend/index.html` |

## 做了什么

- 基础任务：在 WSL 2 + CUDA 环境中编译 llama.cpp，部署 Qwen3-0.6B-GGUF 模型；开发单请求、多并发、文件读取、异常恢复四类测试脚本；搭建前端展示页面；撰写完整技术报告。
- 进阶任务：尝试复用同一文档的 KV 缓存，写了结果级缓存和 slot 保存/恢复两版脚本；实测发现 llama-server 的缓存粒度是“整个请求”，无法复用文档级 KV；如实记录实验数据和分析结论。
