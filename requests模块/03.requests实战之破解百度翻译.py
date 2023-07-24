import json
import requests
if __name__ == "__main__":
    post_url = "https://fanyi.baidu.com/sug"
    # 进行UA伪装
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    # post请求参数处理
    word = input("enter a word:")
    data = {
        "kw":"word"
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    dic_obj = response.json()
    print("over!!!")
    # 持久化存储
    fileName = word+".json"
    fp = open(fileName, "w", encoding="utf-8")
    json.dump(dic_obj, fp=fp, ensure_ascii=False)






