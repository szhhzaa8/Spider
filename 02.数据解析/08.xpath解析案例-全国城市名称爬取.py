import requests
from lxml import etree
if __name__ == "__main__":
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    hot_li_list = tree.xpath('//dic[@class="bottom"]/ul/li') # 热门城市列表
    all_city_names = []
    # 解析得失热门城市名称
    for li in hot_li_list:
        hot_city_name = li.path('./a/text()')[0]
        all_city_names.append(hot_city_name)

    # 解析的是全部城市名称
    city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_name_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)

    print(all_city_names, len(all_city_names)

    '''
    同时获取热门城市和全部城市
      ===>>  tree.xpath('//dic[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
      ‘|’ 表示"或"的意思
    '''