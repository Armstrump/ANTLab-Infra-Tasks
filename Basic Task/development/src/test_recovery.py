# 关掉服务再重启观察能否自行恢复
import requests
import time
import json
import os
import subprocess

url = "http://localhost:8080/v1/chat/completions"
prompt = "你好"

def check_service():
    try:
        r = requests.post(url, json={
            "model": "default",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 16
        }, timeout=10)
        return r.status_code == 200
    except:
        return False

results = []

# 1. 确认服务正常
results.append({"step": "before", "service_ok": check_service()})

# 2. 关掉 llama-server 进程
subprocess.run(["pkill", "-f", "llama-server"])
time.sleep(2)

# 3. 确认服务已退出
results.append({"step": "killed", "service_ok": check_service()})

# 4. 重启服务
subprocess.Popen(
    ["bash", "-c", "cd ~/llama.cpp && ./build/bin/llama-server -m ~/models/Qwen3-0.6B-Q8_0.gguf --host 0.0.0.0 --port 8080"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
time.sleep(10)

# 5. 确认服务恢复
results.append({"step": "recovered", "service_ok": check_service()})

print(json.dumps(results, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open("results/recovery_test.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
