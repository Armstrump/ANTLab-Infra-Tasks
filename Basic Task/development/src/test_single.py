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

start = time.perf_counter()
response = requests.post(url, json=payload, timeout=300)
end = time.perf_counter()

data = response.json()
content = data["choices"][0]["message"]["content"]
generated_tokens = data["usage"]["completion_tokens"]

result = {
    "prompt": prompt,
    "total_time_seconds": round(end - start, 6),
    "generated_tokens": generated_tokens,
    "output": content
}

print(json.dumps(result, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print(f"\n结果已保存到 {output_file}")
