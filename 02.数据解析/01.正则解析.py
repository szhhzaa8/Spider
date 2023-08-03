import requests
import re
if __name__ == "__main__":
    url = 'https://www.google.com/search?q=%E9%A3%8E%E6%99%AF%E5%9B%BE&tbm=isch&hl=zh-CN&chips=q:%E9%A3%8E%E6%99%AF+%E5%9B%BE,online_chips:%E8%87%AA%E7%84%B6%E9%A3%8E%E6%99%AF%E8%83%8C%E6%99%AF%E5%9B%BE:SOj05jjkCY0%3D,online_chips:%E5%B1%B1%E6%B0%B4%E9%A3%8E%E6%99%AF:IYmpREl4eow%3D&sa=X&ved=2ahUKEwiAweGL97-AAxXgB0QIHYGKBT0Q4lYoAHoECAEQOA&biw=1440&bih=720'
        headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    # 使用通用爬虫对整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text
