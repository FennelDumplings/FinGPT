import requests
import json

#修改成自己的api key和secret key
API_KEY = "vXCshPOYbCf1DBYq1aElp7ZH"
SECRET_KEY = "WehpyWELLbYeKBiBh6GxHsVvPvC9PnNO"

s = """一家公司在最近半年的财报数据如下，
营业收入: 5亿2千万；
净利润：8千万；
每股收益：0.1元；
净资产收益率：10%；
库存周转率：12次/年；
应收账款周转率：8次每年；
现金流量净额：7千万。
针对上述财报数据，请给出分析、建议和预警。"""


def main():
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

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
