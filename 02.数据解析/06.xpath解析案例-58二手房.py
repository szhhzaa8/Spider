import requests
from lxml import etree
if __name__ == "__main__":
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    url = 'https://bj.58.com/ershoufang/?PGTID=0d000000-0000-03cd-bcb6-813a4124e455&ClickID=1'
    page_text = requests.get(url=url, headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    # 存储的是div标签对象
    div_list = tree.xpath('//section[@class="list"]/div')
    fp = open('58.txt', 'w', encoding='utf-8')
    for div in div_list:
        title = div.xpath('.//div[@class="property-content"]/div[@class="property-content-detail"]/div[@class="property-content-title"]/h3[@class="property-content-title-name"]/text()')[0]

        print(title)
        fp.write(title+'\n')