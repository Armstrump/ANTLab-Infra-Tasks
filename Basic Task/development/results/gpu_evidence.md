# GPU 驻留证据

## 1. WSL 中 GPU 识别

nvidia-smi 输出：
- GPU: NVIDIA GeForce RTX 5070 Ti Laptop GPU
- 显存: 12227 MiB
- 驱动版本: 610.62
- CUDA UMD Version: 13.3

## 2. llama.cpp 编译产物识别 GPU

启动 llama-server 时的日志：
ggml_cuda_init: found 1 CUDA devices (Total VRAM: 12226 MiB):
  Device 0: NVIDIA GeForce RTX 5070 Ti Laptop GPU, compute capability 12.0
Available devices:
  CUDA0: NVIDIA GeForce RTX 5070 Ti Laptop GPU (12226 MiB, 11026 MiB free)

## 3. 结论

模型计算层和 KV 缓存均驻留在 GPU 上。
