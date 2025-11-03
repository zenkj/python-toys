#!/bin/sh

# pip install mitmproxy   # 安装mitmproxy/mitmweb/mitmdump三个Python工具

# 客户端在初始化OpenAI时配置base_url为http://172.31.16.182:8080/v1
# 访问http://172.31.16.182:8081，查看所有的访问openai的消息内容
mitmweb -m reverse:https://api.openai.com --web-host=172.31.16.182
