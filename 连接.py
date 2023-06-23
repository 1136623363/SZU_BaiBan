# -*- coding: utf-8 -*-

import re

data = '''data:{"errno":0,"errmsg":"success","logid":"2407785010","data":{"data":{"sessionId":"6341","createTime":1686809832,"serverTime":1686809832,"messageInfos":{"ask":{"messageId":"23293","parentId":"0"},"answer":{"messageId":"23294","parentId":"23293"}}},"type":1}}

data:{"errno":0,"errmsg":"success","logid":"2407785010","data":{"data":{"chunkIndex":0,"sessionId":"6341","messageId":"23294","parentId":"23293","aiId":0,"content":"这个问题并没有一个明确的答案，因为深圳大学和北京大学都是中国顶尖的高校，各有特色和优势。","contentType":"markdown","askType":"text","createTime":1686809832,"finish":0,"isSafe":1},"type":2}}

data:{"errno":0,"errmsg":"success","logid":"2407785010","data":{"data":{"chunkIndex":1,"sessionId":"6341","messageId":"23294","parentId":"23293","aiId":0,"content":"不过，我可以从以下几个方面进行比较：\n\n1. 排名：根据软科中国大学排行榜，深圳大学在2022年的排名为2021年全2，而北京大学则排在前10以内。\n2. 录取难度：在广东省历史类高中考生中，深圳大学的录取难度较低，2022年最低分数为554分，排名是66233；而北京大学的最低分数为683分或以上，排名在88以内。","contentType":"markdown","askType":"text","createTime":1686809832,"finish":0,"isSafe":1},"type":2}}

data:{"errno":0,"errmsg":"success","logid":"2407785010","data":{"data":{"chunkIndex":2,"sessionId":"6341","messageId":"23294","parentId":"23293","aiId":0,"content":"然而，在广东省高中考生中，北京大学的录取难度较高，物理成绩超越深圳大学。\n\n综合以上比较，可以看出深圳大学和北京大学各有优势，具体选择还需根据个人的兴趣和发展目标来决定。","contentType":"markdown","askType":"text","createTime":1686809832,"finish":1,"isSafe":1},"type":2}}
'''

print(data)
# 使用正则表达式提取 "content" 值
contents = re.findall(r'"content":"(.*?)"', data, re.DOTALL)
print(contents)
# 将 "content" 值连接起来
combined_content = ''.join(contents)

print(combined_content)
