import requests
from lxml import etree
import os
if __name__ =="__main__":
    url = 'https://pic.netbian.com/4kfengjing/'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    page_text = response.text

    # 数据解析：src的属性值，alt的属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')

   # 创建一个文件夹
    if not os.path.exists('4k风景图'):
        os.mkdir('4k风景图')
    for li in li_list:
        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name =li.xpath('./a/img/@alt')[0] + '.jpg'

        #   请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = '4k风景图/' + img_name
        with open(img_path, 'wb') as fp:
           fp.write(img_data)
           print(img_name, "下载成功")

