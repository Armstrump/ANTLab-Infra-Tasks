import requests
import time
import json
import os

url = "http://localhost:8080/v1/chat/completions"
prompt = "你好，请用中文介绍一下你自己"

results = []

for run in range(3):
    payload = {
        "model": "default",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 256
    }
    start = time.perf_counter()
    response = requests.post(url, json=payload, timeout=300)
    end = time.perf_counter()
    data = response.json()
    tokens = data["usage"]["completion_tokens"]
    results.append({
        "run": run + 1,
        "total_time_seconds": round(end - start, 6),
        "generated_tokens": tokens
    })

summary = {"concurrency": 1, "runs": results}
print(json.dumps(summary, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open("results/baseline_single.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)
