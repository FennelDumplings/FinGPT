import requests
import json

from flask import Flask, render_template, request
from forms import CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

#修改成自己的api key和secret key
API_KEY = "vXCshPOYbCf1DBYq1aElp7ZH"
SECRET_KEY = "WehpyWELLbYeKBiBh6GxHsVvPvC9PnNO"

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def query(s):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    #注意message必须是奇数条
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": s
            }
            #,
            #{
            #    "role": "assistant",
            #    "content": "你好，有什么我可以帮助你的吗？"
            #}
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    res = requests.request("POST", url, headers=headers, data=payload).json()
    print(res['result'])
    return res['result']


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm()
    if form.validate_on_submit():
        comment_text = form.comment.data
        # 处理文本内容，可以进行存储或其他操作

        return query(comment_text)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
