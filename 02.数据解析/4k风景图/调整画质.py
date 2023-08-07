from PIL import Image

# 打开已获取的图片
image_path = '/Users/zhs/PycharmProjects/爬虫/02.数据解析/4k风景图/护眼 森林 绿色树林 高清风景 4k壁纸.jpg'  # 替换为您的图像路径
image = Image.open(image_path)

# 定义目标分辨率（4K 分辨率）
target_width = 3840
target_height = 2160

# 调整图像大小
resized_image = image.resize((target_width, target_height), Image.LANCZOS)  # 使用 Lanczos 插值算法

# 保存调整后的图像
output_path = 'output_image.jpg'  # 替换为输出图像路径
resized_image.save(output_path)

print("图像调整完成并保存到", output_path)
