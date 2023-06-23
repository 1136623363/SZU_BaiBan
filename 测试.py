import json
import re
import time

import requests

baiban_headers = {
        "Host": "api.bs.kaixueyouxuan.com",
        "Connection": "keep-alive",
        "Content-Length": "2510",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUxNzYsImV4cCI6MTY4ODk3Mjk2OX0.RYC-mio0ZSeQCppJeH8A6PVKt_499Lf3Tajh_jCKIPU",
        "charset": "utf-8",
        "mp-app-id": "wx6bd5ddbb36f39670",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5115 MMWEBSDK/20230504 MMWEBID/21 MicroMessenger/8.0.37.2380(0x28002537) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "accept": "*/*",
        "Referer": "https://servicewechat.com/wx6bd5ddbb36f39670/57/page-frame.html"
}

def getReply(prompt):
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
    data = {"content":prompt,"sessionId":"","contentType":"text","parentId":"","context":[],"repeat":0,"promptId":""}

    resp = requests.post(url,headers=headers,json=data)
    resp.encoding='utf-8'

    # 使用正则表达式提取 "content" 值
    contents = re.findall('"content":"(.*?)"', resp.text, re.DOTALL)
    print(contents)
    # 将 "content" 值连接起来并去除换行符
    combined_content = ''.join(contents).replace(r'\n', '')

    return combined_content
    # return eval(resp.text.split('\n\n')[-2][5:])['data']['data']['content']


def getCom():
    url = 'https://api.bs.kaixueyouxuan.com/graphql'

    data = {"operationName":"latestReplies",
            "variables":{},
            "query":"query latestReplies($afterComment: String, $afterSubcomment: String) {\n  viewer {\n    user {\n      id\n      userComments(type: RECEIVED, first: 5, after: $afterComment) {\n        edges {\n          node {\n            id\n            content\n            isAnonymous\n            createdAt\n            creator {\n              ...UserFieldsNano\n              profile {\n                nickname\n                __typename\n              }\n              __typename\n            }\n            post {\n              id\n              content\n              createdAt\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        pageInfo {\n          startCursor\n          endCursor\n          hasNextPage\n          __typename\n        }\n        __typename\n      }\n      userSubcomments(type: RECEIVED, first: 5, after: $afterSubcomment) {\n        edges {\n          node {\n            id\n            content\n            isAnonymous\n            createdAt\n            creator {\n              ...UserFieldsNano\n              profile {\n                nickname\n                __typename\n              }\n              __typename\n            }\n            comment {\n              id\n              content\n              createdAt\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        pageInfo {\n          startCursor\n          endCursor\n          hasNextPage\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserFieldsNano on User {\n  id\n  username\n  createdAt\n  __typename\n}"}
    resp = requests.post(url,headers=baiban_headers,json=data)

    return resp.text

def sendReply(commentId,content):
    url = 'https://api.bs.kaixueyouxuan.com/graphql'

    # data = {"operationName":"AddCommentOnComment","variables":{"content":"一楼","isAnonymous":False,"commentId":"Q29tbWVudDozMzk4Njc"},"query":"mutation AddCommentOnComment($content: String!, $commentId: ID!, $replyToId: ID, $isAnonymous: Boolean!) {\n  subcomment: createSubcomment(\n    input: {commentId: $commentId, content: $content, replyToId: $replyToId, isAnonymous: $isAnonymous}\n  ) {\n    ...SubcommentFields\n    __typename\n  }\n}\n\nfragment ProfileFields on Profile {\n  id\n  nickname\n  avatarUrl\n  bio\n  gender\n  grade\n  institute\n  __typename\n}\n\nfragment UserFields on User {\n  id\n  username\n  createdAt\n  profile {\n    ...ProfileFields\n    __typename\n  }\n  verify {\n    id\n    school {\n      id\n      name\n      logoUrl\n      enShort\n      oaAppid\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SubcommentFields on Subcomment {\n  id\n  content\n  isAnonymous\n  createdAt\n  creator {\n    ...UserFields\n    __typename\n  }\n  viewerCanDelete\n  replyTo {\n    id\n    content\n    isAnonymous\n    createdAt\n    creator {\n      ...UserFields\n      __typename\n    }\n    viewerCanDelete\n    likeCount\n    viewerHasLiked\n    viewerHasReported\n    __typename\n  }\n  likeCount\n  replyCount\n  viewerHasLiked\n  viewerHasReported\n  __typename\n}"}
    data = {"operationName":"AddCommentOnComment","variables":{"content":content,"isAnonymous":False,"commentId":commentId},"query":"mutation AddCommentOnComment($content: String!, $commentId: ID!, $replyToId: ID, $isAnonymous: Boolean!) {\n  subcomment: createSubcomment(\n    input: {commentId: $commentId, content: $content, replyToId: $replyToId, isAnonymous: $isAnonymous}\n  ) {\n    ...SubcommentFields\n    __typename\n  }\n}\n\nfragment ProfileFields on Profile {\n  id\n  nickname\n  avatarUrl\n  bio\n  gender\n  grade\n  institute\n  __typename\n}\n\nfragment UserFields on User {\n  id\n  username\n  createdAt\n  profile {\n    ...ProfileFields\n    __typename\n  }\n  verify {\n    id\n    school {\n      id\n      name\n      logoUrl\n      enShort\n      oaAppid\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SubcommentFields on Subcomment {\n  id\n  content\n  isAnonymous\n  createdAt\n  creator {\n    ...UserFields\n    __typename\n  }\n  viewerCanDelete\n  replyTo {\n    id\n    content\n    isAnonymous\n    createdAt\n    creator {\n      ...UserFields\n      __typename\n    }\n    viewerCanDelete\n    likeCount\n    viewerHasLiked\n    viewerHasReported\n    __typename\n  }\n  likeCount\n  replyCount\n  viewerHasLiked\n  viewerHasReported\n  __typename\n}"}

    resp = requests.post(url, headers=baiban_headers, json=data)
    return resp.text


def main():

    comment_text = getCom().replace('false', 'False')
    comment = eval(comment_text)["data"]["viewer"]["user"]["userComments"]["edges"]

    comment_new = [{i['node']['id']: i['node']['content']} for i in comment]
    print(comment_new)

    # with open('comment.json', 'w', encoding='utf-8') as f2:
    #     json.dump(comment_new, f2)

    with open('comment.json', 'r', encoding='utf-8') as f1:
        comment_former = json.load(f1)

    print(comment_former)

    comment_to_reply = [item for item in comment_new if item not in comment_former]

    for i in comment_to_reply:

        # print(list(i.keys())[0], list(i.values())[0])

        commentId = list(i.keys())[0]
        content = getReply('我是一名深圳大学的学生，请您回答我的问题时尽可能地丰富详细，这是我的问题：'+list(i.values())[0])
        # {"errors":[{"message":"rpc error: code = Unknown desc = Internal server error","path":["subcomment"]}],"data":null}
        print(content)
        flag = sendReply(commentId, content)

        if flag.find("rpc error") == -1:
            comment_former.append(i)

    # print(comment_former, comment_new)
    comment_to_check = [item for item in comment_new if item not in comment_former]
    if comment_to_check == []:
        print('最近消息已回复')
        with open('comment.json', 'w', encoding='utf-8') as f2:
            json.dump(comment_new, f2)

if __name__ == '__main__':
    # while True:
    #     try:
    #         main()
    #     except:
    #         print('error')
    #     time.sleep(10)
    print(getCom())


