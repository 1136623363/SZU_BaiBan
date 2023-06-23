import time

import requests

def chatgpt(prompt):
    burp0_url = "http://10.10.10.135:3002/api/chat-process"
    burp0_headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://10.10.10.135:3002",
        "Referer": "http://10.10.10.135:3002/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close"
    }

    burp0_json={"options": {"conversationId": "9bcd54ce-23ba-49e0-b19b-cc73bc62bbb8", "parentMessageId": "1da7cd4a-b87c-4aa7-a7ab-86b8f7986af7"},
                "prompt": prompt
    }

    resp = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)

    # print(resp.text.split('\n')[-1])
    return eval(resp.text.split('\n')[-1])["text"]

start = time.time()
print(chatgpt("你是基于gpt几的，今天是几号，你能推送给我今天的头条吗"))
end = time.time()
print(f'{end -start}')