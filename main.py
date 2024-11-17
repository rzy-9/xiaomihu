from PIL import Image


def split_image(image_path, rows, cols, output_folder):
    # 打开图片
    img = Image.open(image_path)
    img_width, img_height = img.size

    # 计算每个小图片的宽度和高度
    tile_width = (img_width+1) // cols
    tile_height = img_height // rows
    temp=0
    print(img_width, img_height)


    # 按照行列进行切割
    for row in range(rows):
        result = 0
        for col in range(cols):
            # 计算每个子图片的左上角和右下角的坐标
            left = col * tile_width
            top = row * tile_height
            right = (col + 1) * tile_width
            bottom = (row + 1) * tile_height
            result = row // 3


            temp=(temp % 66)+1

            # 裁剪出子图片
            tile = img.crop((left, top, right, bottom))
            # 保存子图片
            tile.save(f"{output_folder}/20221517_18_{temp:03}_{result}.jpg")

# 调用函数，设定图片路径，行数，列数，输出文件夹
split_image("tupian3.jpg", 36, 22, "14")
