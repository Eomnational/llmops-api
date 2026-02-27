import os

from flask import request
from openai import OpenAI

from internal.schema.app_schema import CompletionReq


class AppHandler:
    """应用控制器"""

    def ping(self):
        print("ping:" + "pong")
        return {"ping": "pong"}

    def completion(self):
        """聊天接口"""
        # 1. 获取请求参数POST
        req = CompletionReq()
        if not req.validate():
            return req.error
        query = request.json.get("query")
        # 2. 调用聊天模型生成回复
        client = OpenAI(
            api_key=os.getenv("API_KEY"),
            base_url=os.getenv("BASE_URL"),
        )
        # 3. 返回回复结果
        completion = client.chat.completions.create(
            model="qwen3-coder-next",
            messages=[
                {"role": "system", "content": "你是千问开发的模型，请根据用户的问题进行回答："},
                {"role": "user", "content": query}
            ],
        )
        content = completion.choices[0].message.content
        return content
