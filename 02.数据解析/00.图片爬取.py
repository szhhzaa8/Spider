import requests
if __name__ == "__main__":
    url = 'https://t7.baidu.com/it/u=27018761,936335273&fm=193&f=GIF'
    # content二进制
    img_data = requests.get(url=url).content
    with open('./baidu.jpg', 'wb') as fp:
        fp.write(img_data)