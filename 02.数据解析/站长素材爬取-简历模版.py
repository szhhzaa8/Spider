import requests
from lxml import etree

if __name__ == "__main__":
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url = 'https://sc.chinaz.com/jianli/tongyong.html'
    page_text1 = requests.get(url=url, headers=headers).text
    tree1 = etree.HTML(page_text1)
    href_list = tree1.xpath(
        '//div[@class="main_list jl_main masonry"]/div[@class="box col3 ws_block masonry-brick"]/a/@href')
    fp = open('简历模版.txt', 'w', encoding='utf-8')

    for href in href_list:
        page_text2 = requests.get(url=href, headers=headers).text
        tree2 = etree.HTML(page_text2)
        download_href_list = tree2.xpath('//div[@class="clearfix mt20 downlist"]/ul/li/a/@href')

        # Check if there are any download links before accessing them
        if download_href_list:
            model_name = tree2.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
            fp.write(model_name + ' ' + download_href_list[0] + '\n')

    fp.close()







