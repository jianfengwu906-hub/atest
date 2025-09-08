import json
import requests

url = "https://sesaadmin.nie.netease.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
            result = response.text
            try:
                start = result.find('{')
                end = result.rfind('}') + 1
                json_str = result[start:end]
                result=json.loads(json_str)
            except (ValueError, AttributeError) as e:
                json_str=None
                
    else:
            print(f"请求失败，状态码：{response.status_code}")
            print("响应内容：", response.text)
except requests.exceptions.RequestException as e:
        print(f"请求异常：{str(e)}")
except json.JSONDecodeError:
        print("响应内容非JSON格式：", response.text)
