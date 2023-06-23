import re
import base64

text = '''
{
  "node": {
    "id": "Q29tbWVudDozMzMzODc",
    "content": "是不是吃太辣导致的，我不怎么能吃辣的，老板没听到给我加了辣椒，晚上也会肚子疼，第二天菊花爆炸",
    "isAnonymous": false,
    "createdAt": "2023-06-10T06:38:29.007Z",
    "creator": {
      "id": "VXNlcjo0Mjc1",
      "username": "",
      "createdAt": "2022-05-08T16:09:52.534Z",
      "profile": {
        "id": "UHJvZmlsZTo0Mjc1",
        "nickname": "143",
        "avatarUrl": "https://cdn-v4.szlikeyou.com/img/avatar/4275/e9d17d5c-633a-44f3-97a2-b2d0db821e98/tmp_f2303a9d2d530fa11ca5e44b9d038d35909a8e6abe325d26.jpg",
        "bio": "",
        "gender": "MALE",
        "grade": 2021,
        "institute": "材料学院",
        "__typename": "Profile"
      },
      "verify": {
        "id": "VmVyaWZ5OjQyNzU",
        "school": {
          "id": "U2Nob29sOjE",
          "name": "深圳大学",
          "logoUrl": "https://cdn-config.szlikeyou.com/MiniProgram/icons/szu/logo.png",
          "enShort": "szu",
          "oaAppid": "wxfcf7b19fdd5d9770",
          "__typename": "School"
        },
        "__typename": "Verify"
      },
      "__typename": "User"
    },
    "viewerCanDelete": false,
    "likeCount": 0,
    "viewerHasLiked": false,
    "viewerHasReported": false,
    "__typename": "Comment"
  },
  "__typename": "CommentEdge"
}
'''

# 使用正则表达式匹配Base64加密部分
pattern = r'"content": "(.*?)"'
matches = re.findall(pattern, text)

if len(matches) > 0:
    # 找到了匹配的部分
    content = matches[0]

    # 编码非ASCII字符
    content = content.encode('utf-8')

    # 解码Base64
    decoded_content = base64.b64decode(content).decode('utf-8')
    print("解码后的内容：", decoded_content)
else:
    print("未找到匹配的Base64加密部分。")


# 编码非ASCII字符
content = content.encode('utf-8')
print("编码后的内容：", content)

# 解码Base64
decoded_content = base64.b64decode(content).decode('utf-8')
print("解码后的内容：", decoded_content)
