import requests
from bs4 import BeautifulSoup
import webbrowser
if __name__ == "__main__":
    # Step1: 指定URL
    url = 'https://www.sogou.com/'
    # Step2: 发起请求
    # get方法会返回一个响应对象
    Response = requests.get(url=url)
    # Step3: 获取响应数据,text返回的是字符串形式的响应数据
    page_text = Response.text

    # Step4: 持久化存储
    with open('./sogo.html', "w", encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")
    # 使用BeautifulSoup解析源码
    soup = BeautifulSoup(page_text, "html.parser")

    # 格式化输出源码
    formatted_html = soup.prettify()

    # 打印格式化后的源码
    print(formatted_html)








