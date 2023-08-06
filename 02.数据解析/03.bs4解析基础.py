# bs4数据解析原理：
# 实例化一个beautifulSoup对象，并且将页面源码数据加载到该对象中
# 通过调用beautifulSoup对象中相关的属性或方法进行标签定位和数据爬取

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 获取名称
soup = BeautifulSoup(html_doc, 'lxml')
tag = soup.p
print(tag.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['class'])

# 获取内容
print(soup.p.string)

# 属性定位
print(soup.title)
print(soup.find('p', class_="story"))


# 返回符合要求的所有标签（列表）
print(soup.find_all('a'))


# 获取标签之间的文本数据soup.a.text/string/get_text(
print(soup.p.text)

# 获取标签中的属性值
print(soup.a['href'])