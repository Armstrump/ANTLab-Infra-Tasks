# 用slot保存/恢复，测试同一文档第二次请求能不能复用KV
import requests
import time
import json
import os

url = "http://localhost:8080/v1/chat/completions"
save_url = "http://localhost:8080/slots/0?action=save"
restore_url = "http://localhost:8080/slots/0?action=restore"

doc_path = "../../Basic Task/提示词与输入文档/输入文档/办公输入01-项目会议与进度资料.md"
with open(doc_path, "r", encoding="utf-8") as f:
    doc = f.read()

def ask(question):
    prompt = question + "\n\n文档内容：\n" + doc
    payload = {
        "model": "default",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 128,
        "id_slot": 0
    }
    t0 = time.perf_counter()
    response = requests.post(url, json=payload, timeout=300)
    t1 = time.perf_counter()
    data = response.json()
    return {
        "question": question,
        "time_used": round(t1 - t0, 6),
        "output": data["choices"][0]["message"]["content"]
    }

# 第一次：算文档+问题1
r1 = ask("这个项目的交付时间是什么时候？")
print("第一次:", r1["time_used"], "秒")

# 保存slot 0的状态
requests.post(save_url, json={"filename": "slot0.bin"})
print("slot已保存")

# 第二次：同一文档，换问题2
r2 = ask("这个项目的成员有哪些？")
print("第二次:", r2["time_used"], "秒")

# 第三次：同一文档，换问题3
r3 = ask("这个项目的目标是什么？")
print("第三次:", r3["time_used"], "秒")

result = {
    "run1": r1["time_used"],
    "run2": r2["time_used"],
    "run3": r3["time_used"],
    "note": "同一文档不同问题，slot 0保持复用"
}
os.makedirs("results", exist_ok=True)
with open("results/slot_compare.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
