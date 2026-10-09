import requests
import time
import json
import os

url = "http://localhost:8080/v1/chat/completions"

# 读文件
file_path = "../提示词与输入文档/输入文档/办公输入01-项目会议与进度资料.md"
with open(file_path, "r", encoding="utf-8") as f:
    file_content = f.read()

prompt = "请总结以下文档的主要内容：\n\n" + file_content

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

result = {
    "file": file_path,
    "prompt_length": len(prompt),
    "total_time_seconds": round(end - start, 6),
    "output": content
}

print(json.dumps(result, ensure_ascii=False, indent=4))

os.makedirs("results", exist_ok=True)
with open("results/run_file.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("\n结果已保存到 results/run_file.json")
