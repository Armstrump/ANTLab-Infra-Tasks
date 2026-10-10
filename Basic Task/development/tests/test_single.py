# 先确认llama-server在8080进行中再进行这个
import requests
import time
import json
import os

url = "http://localhost:8080/v1/chat/completions"
prompt = "你好，请用中文介绍一下你自己"
output_file = "results/run_001.json"

payload = {
    "model": "default",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 512
}

t0 = time.perf_counter()
response = requests.post(url, json=payload, timeout=300)
t1 = time.perf_counter()

data = response.json()
content = data["choices"][0]["message"]["content"]
tokens = data["usage"]["completion_tokens"]

result = {
    "prompt": prompt,
    "time_used": round(t1 - t0, 6),
    "tokens": tokens,
    "output": content
}

print(json.dumps(result, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print(f"\n结果已保存到 {output_file}")
