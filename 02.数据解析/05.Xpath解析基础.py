# Xpath解析原理
# 1.实例化一个etree的对象，且需要将被解析的源码数据加载到该对象中
# 2.调用etree对象中的Xpath方法结合着Xpath表达式实现标签定位和内容捕获
'''
如何实例化etree对象：      from lxml import etree
    1: 将本地的html文件中的源码加载到etree对象中
        etree.parse(filepath
    2: 可以将从互联网上获取的源码数据加载到该对象中
        etree.HTML('page_text')
    xpath('xpath表达式')
xpath表达式：
    /：表示从根节点开始定位，表示的是一个层级
    //：表示多个层级
        表示从任意位置开始定位
    属性定位：tag[@attrname="attrvalue"]
    索引定位：//div[@class="song"]/p[3]
    取文本：
        1:/text() 获取的是标签中直系的文本内容
        2://text()获取的是标签中非直系的文本内容
    取属性：
        /@attrName   ==>  img/@src
'''

from lxml import etree
if __name__ =="__main__":
    tree = etree.parse('text.html')
    # r = tree.xpath('/html/head/title')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div[@class="song"]/p[3]')
    # r = tree.xpath('//div[@class="tang"]/ul/li[5]/a/text()')[0]       # 添加【0】将列表转换为字符串
    r = tree.xpath('//div[@class="song"]/img/@src')[0]
    print(r)