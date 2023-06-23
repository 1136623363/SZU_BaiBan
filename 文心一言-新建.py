import requests

url = 'https://wanhua.baidu.com/chat/completion?appname=newapp&ut=Redmi+K30+Pro_12_31_Xiaomi&ua=1080_2270_android_1.2.0.10_440&bdvc=0&zid=H0pmQJITDkhvKzVQR4m1p7M5Rv8r03Eym7iQTPQdGy3W-44g42bn-65JQ1bvT9QwnJ-x0y58SICxk4xav2uiKfg&uid=guHiig8I280G8-8u0u-1a_u12a_HO2iq0aSkijao2a8Y9WMxJkD1MVJuA&cfrom=1000813a&from=1019105u&scheme=baiduwanhua&network=1_-1&c3_aid=A00-VHBYZQSZ4HMKGOWDL72FJCNHLQDONLFG-AYWALG4W&ds_stc=0.7595&ds_lv=7&jt=31%24eyJrIj4iNyI0Iix5IkciRUhFQkhCRU9QUVJTVFVRTlMiLSJ3biJAIjk%2FQkE%2FREdHSUlKQ0giQiI6NyJVIk5UVzY0OTw8Ojw9OD4iNyIvKyJKIkNDREUiQyI9IlUiUExTLjgiLyJvIkEiPHJUMGJWRlFoaGA%2Fam1QR045RmVFQFdrSW8pOFdLVXRjVHpONDU%2BQkhDZWZWYzVJXmNRdDlkQnlyOmlmc3JhKTt4UVRXbzExVTdhTTw%2BMmtjbz92LjVoZE5SRik9S29iYVxkQzh5UEQrYkcqR2hjXTgpa0J2bm1rSnhteXY%2FbSk5cHRXPWF0XEpBXUlrbmU0ZlMsVDNBP1pPOFM8Z1lSSjBWYi1kMWV2XkFaRCxgNTBKMGJiPztrQldURHhWdTtcXXV3WDRTYStfXltaTk5gTTRtLmc9cTRpQ1I6dV02U3oxZFtwXy9hXWkpSlUwcF9pNzwtTUg7cTA2b3c2Oll5QC5sWj5ddGNRPDBjR2V6XEM9XWV1PEBlSUZ6NVo9OlRTV2tuQ05iKXY8d0h5Mjw2THFFS0Ixa3c0bHdzL3BbVjlgU2RyVVYxO3hiSlVpY29HPVtsUmR2Z1JPbEtzTTdZYlk6W1l6QkczNklYUXxiNj1oPUpxZVFPeVtDaFBJYGpJOWNOZENCQDJEW3ovejZlNnFtNkA9OmhBPnw0NHw2PDw%2BPXFDcERHQkZGRHV6R0pQLStQTTFRM2VnOzY6PCJ9'

headers = {
    # 'Host': 'wanhua.baidu.com',
    'Cookie': 'BAIDUCUID_BFESS=guHiig8I280G8-8u0u-1a_u12a_HO2iq0aSkijao2a8Y9WMxJkD1MVJuA; BAIDUCUID=guHiig8I280G8-8u0u-1a_u12a_HO2iq0aSkijao2a8Y9WMxJkD1MVJuA; BDUSS=o5b2hqb1pjU1ctVDV1YTJHUkpVZXpaSDl4a0JNYi1EQjVGaUdhSmY4T3VZSDlrRUFBQUFBJCQAAAAAAAAAAAEAAADbA8ZZ4Mix8sfjs8fT6cDWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK7TV2Su01dkWE; BDUSS_BFESS=o5b2hqb1pjU1ctVDV1YTJHUkpVZXpaSDl4a0JNYi1EQjVGaUdhSmY4T3VZSDlrRUFBQUFBJCQAAAAAAAAAAAEAAADbA8ZZ4Mix8sfjs8fT6cDWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK7TV2Su01dkWE; __bid_n=1882352e1e57472c027669; BAIDUID=D2999E068FFCB2C6E57DDDCFF9005C2A:FG=1; BAIDUID_BFESS=D2999E068FFCB2C6E57DDDCFF9005C2A:FG=1; ab_sr=1.0.1_ZTFmMTE3NmFhZTc2ZTY1MTdkMDZlZDA0MzFhZjA5OWMyOWI1YjRlMjU5NmY5ZTdiNDZhOTc2MzNhYmQyY2U4NmI3NTQxYWFiZjZkNjk2NjZlZTY4YjIzMDA2NDcxN2U3MjJhMjA0YzI5Y2MxODBkMmVhYzBhYjc1YzJlNWZhOGRjNjMzNmRjOTU1NGE0OWQwOTlmYTBkZGQ3YzYzODNhNQ==',
    # 'Content-Length': '111',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    'Accept': 'text/event-stream',
    'Acs-Token': '1686315789175_1686379923585_UMBp6LD4evqHH/l70lMIZpkHNqA+XImE2+MHFKxBp/EUMNMqWv4e2FQV7dJg8rAED7VpTUyyZ5UuUutdJdgzcLKtVd/hbPGuKJC3mcK+CZ9wHSwZ0ArPhosBw/8fpUCyaPrf4xIPijnuYzNfDUfFlCKeNkwijhj3ralalkFTQQQdX4EGPz9qrWnHe5BcGNaSzCgyOEP7Wy0eWmQKskaGJqj1sWJBbbnOm8ptM5pyoSVK4AR/QGVEQWSi4cPMbarxBCj+sj1WflUUFQaImdtTbwJ24SZ5fPGZBcJUrGMvgaG+JaSY2UfhfwKT8nYaM2lTKoYDwbxazJRupqgv+qtJncRrj1w8M4A/zRyTeOJQWG+jGYi3BWms0zI/N9vMqwVdp1jPIX8Wze840JSZDGACZzJNghRTOdSK2hwEljag1X/ZSy4GAnTdTk9x+G3rnv5xILbWJH+F7Y2VE3aLBhLkHjwEJlx3Tgeg4C6LugwKP6VFH1/gGZHaS+2kUpCDLz7Ju6wXUlxhJzGxj1l0zEGKqXkxGvUQp87HXZ70u4Nf3vh0HYurvlgs9rZ4MfXZQWNr6X1+mbo9lSAMJJzxbCj7B8hlU/6vlNxhd7sg0kEqgmG/OQ8Ie9MigD2HCHKJorvx',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.28 light/1.0 newapp/1.2.0.10 (Baidu; P1 12)',
    'Content-Type': 'application/json',
    'Origin': 'https://wanhua.baidu.com',
    'X-Requested-With': 'com.baidu.newapp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'X-From-H3-Trnet': 'true',
    'X-Bd-Traceid': 'fe38d046d71d41999cde96d858b4d1b5',
    # 'Referer': 'https://wanhua.baidu.com/talk/chat',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'close'
}
data = {"content":"今天是几号","sessionId":"","contentType":"text","parentId":"","context":[],"repeat":0,"promptId":""}

resp = requests.post(url,headers=headers,json=data)
resp.encoding='utf-8'

# print(resp.text)
# print(resp.text.split('\n\n'))
print(eval(resp.text.split('\n\n')[-2][5:])['data']['data']['content'])



# print(resp.json())