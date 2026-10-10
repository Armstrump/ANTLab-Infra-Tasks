# 同时发4个请求，观察会不会排队
import requests
import time
import json
import os
import threading

url = "http://localhost:8080/v1/chat/completions"
prompt = "你好，请用中文介绍一下你自己"
output_file = "results/run_concurrent.json"

concurrency = 4
results = []
lock = threading.Lock()

def send_request(idx):
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
    with lock:
        results.append({
            "request_id": idx,
            "time_used": round(t1 - t0, 6),
            "tokens": tokens,
            "output": content
        })

threads = []
for i in range(concurrency):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

summary = {
    "concurrency": concurrency,
    "total_requests": len(results),
    "results": results
}

print(json.dumps(summary, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=4)

print(f"\n结果已保存到 {output_file}")
