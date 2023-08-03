import requests
import json

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    param = {
        'cname':'',
            'pid':'',
        'keyword': input("请输入查询地址："),
        'pageIndex': '1',
        'pageSize': '100'
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.post(url=url, params=param, headers=headers)
    list_data = response.json()
    fp = open('KFC查询.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False, indent=4)
    print("over!!!")