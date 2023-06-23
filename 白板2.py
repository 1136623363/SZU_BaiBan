import requests

url = "https://api.bs.kaixueyouxuan.com/graphql"

headers= {
    "Host": "api.bs.kaixueyouxuan.com",
    "Connection": "keep-alive",
    "Content-Length": "1905",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUxNzYsImV4cCI6MTY4ODk3Mjk2OX0.RYC-mio0ZSeQCppJeH8A6PVKt_499Lf3Tajh_jCKIPU",
    "charset": "utf-8",
    "mp-app-id": "wx6bd5ddbb36f39670",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; Redmi K30 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5115 MMWEBSDK/20230504 MMWEBID/21 MicroMessenger/8.0.37.2380(0x28002537) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/json",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "accept": "*/*",
    "Referer": "https://servicewechat.com/wx6bd5ddbb36f39670/57/page-frame.html"
}

data = {
    "operationName": "Comments",
    "variables": {
        "postId": "UG9zdDoxNDgwNTk",
        "order": "LATEST"
    },
    "query": "query Comments($postId: ID!, $order: PostCommentOrder!, $after: String) {\n  comments(postId: $postId, first: 10, order: $order, after: $after) {\n    edges {\n      node {\n        ...CommentFields\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      startCursor\n      endCursor\n      hasPreviousPage\n      hasNextPage\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ProfileFields on Profile {\n  id\n  nickname\n  avatarUrl\n  bio\n  gender\n  grade\n  institute\n  __typename\n}\n\nfragment UserFields on User {\n  id\n  username\n  createdAt\n  profile {\n    ...ProfileFields\n    __typename\n  }\n  verify {\n    id\n    school {\n      id\n      name\n      logoUrl\n      enShort\n      oaAppid\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SubcommentFields on Subcomment {\n  id\n  content\n  isAnonymous\n  createdAt\n  creator {\n    ...UserFields\n    __typename\n  }\n  viewerCanDelete\n  replyTo {\n    id\n    content\n    isAnonymous\n    createdAt\n    creator {\n      ...UserFields\n      __typename\n    }\n    viewerCanDelete\n    likeCount\n    viewerHasLiked\n    viewerHasReported\n    __typename\n  }\n  likeCount\n  replyCount\n  viewerHasLiked\n  viewerHasReported\n  __typename\n}\n\nfragment CommentFields on Comment {\n  id\n  content\n  images\n  isAnonymous\n  createdAt\n  creator {\n    ...UserFields\n    __typename\n  }\n  viewerCanDelete\n  likeCount\n  subcommentCount\n  viewerHasLiked\n  viewerHasReported\n  subcomments(first: 2) {\n    pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      __typename\n    }\n    edges {\n      node {\n        ...SubcommentFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}"
}
resp = requests.post(url,headers=headers,json=data)

print(resp.text)