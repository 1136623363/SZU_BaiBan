import requests

url = 'https://api.bs.kaixueyouxuan.com/graphql'
headers = {
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
data = {
    "operationName": "Posts",
    "variables": {
        "orderBy": "LATEST",
        "schoolId": "U2Nob29sOjE",
        #"after":"eyJpZCI6MTQ4MDU5LCJ0IjoxNjg2Mzc0MTA5MjYyfQ"
    },
    "query": "query Posts($schoolId: ID, $topicId: ID, $subtopicId: ID, $keyword: String, $orderBy: PostOrder, $after: String, $excludeTopicId: ID) {\n  posts(\n    filter: {schoolId: $schoolId, topicId: $topicId, subtopicId: $subtopicId, keyword: $keyword, excludeTopicId: $excludeTopicId}\n    orderBy: $orderBy\n    first: 10\n    after: $after\n  ) {\n    edges {\n      node {\n        ...PostFields\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    pageInfo {\n      hasPreviousPage\n      hasNextPage\n      startCursor\n      endCursor\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ProfileFields on Profile {\n  id\n  nickname\n  avatarUrl\n  bio\n  gender\n  grade\n  institute\n  __typename\n}\n\nfragment UserFields on User {\n  id\n  username\n  createdAt\n  profile {\n    ...ProfileFields\n    __typename\n  }\n  verify {\n    id\n    school {\n      id\n      name\n      logoUrl\n      enShort\n      oaAppid\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SubtopicFields on Subtopic {\n  id\n  name\n  description\n  weight\n  iconUrl\n  isDeleted\n  isWishEnabled\n  isForceContact\n  __typename\n}\n\nfragment TopicFields on Topic {\n  id\n  name\n  description\n  weight\n  iconUrl\n  isDeleted\n  isWishEnabled\n  isForceContact\n  subtopics {\n    edges {\n      node {\n        ...SubtopicFields\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PostFields on Post {\n  id\n  content\n  images\n  isAnonymous\n  creator {\n    ...UserFields\n    __typename\n  }\n  contact {\n    contact\n    expiredAt\n    __typename\n  }\n  topic {\n    ...TopicFields\n    __typename\n  }\n  subtopic {\n    ...SubtopicFields\n    __typename\n  }\n  createdAt\n  updatedAt\n  isPinned\n  viewerCanUpdate\n  viewerCanDelete\n  likeCount\n  commentCount\n  viewerHasLiked\n  viewerHasMarked\n  school {\n    id\n    name\n    enShort\n    logoUrl\n    __typename\n  }\n  viewerHasReported\n  comments(first: 3, order: RANK) {\n    totalCount\n    edges {\n      node {\n        id\n        content\n        isAnonymous\n        createdAt\n        creator {\n          ...UserFields\n          __typename\n        }\n        viewerCanDelete\n        likeCount\n        viewerHasLiked\n        viewerHasReported\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}"
}

resp = requests.post(url,headers=headers,json=data)

print(resp.text)