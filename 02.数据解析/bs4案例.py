import requests
from bs4 import BeautifulSoup
import re
def split_text_into_lines(text, line_length):
    lines = [text[i:i+line_length] for i in range(0, len(text), line_length)]
    return lines
if __name__ == "__main__":
    # 爬取三国演义所有章节标题和章节内容
    # 对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
    page_text = requests.get(url=url, headers=headers).content

    # 在首页中解析出章节标题和详情页的url
    # 1.实例化BeautifulSoup对象，将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt', "w", encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com/'+li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        # 解析出详情页中的相关内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        paragraphs = div_tag.find_all('p')  # 找到所有段落
        # 解析到了章节的内容
        content = '\n\n'.join(paragraph.get_text() for paragraph in paragraphs)  # 将段落分隔为两个换行符
        content = re.sub(r'\xa0', ' ', content)
        lines = split_text_into_lines(content, 37)  # 将段落内容分为37个字的若干行
        formatted_content = '\n'.join(lines)  # 将分行后的内容重新连接成字符串
        fp.write(title+':'+'：\n'+ formatted_content +'\n\n' )
        print(title,"爬取成功")



