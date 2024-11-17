import cv2
import numpy as np
import os

# 读取图像
image = cv2.imread('data.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 使用高斯模糊去除噪点
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# 2. 边缘检测（Canny）
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

# 3. 霍夫变换检测线条
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

# 创建彩色图像用于绘制线条（方便观察）
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# 4. 绘制检测到的线条
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 5. 进行轮廓检测（在没有明显噪声的情况下）
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建输出文件夹
output_dir = 'digital'
os.makedirs(output_dir, exist_ok=True)

# 设定矩形大小的合理范围
min_width, max_width = 50, 90  # 最小和最大宽度
min_height, max_height = 50, 90  # 最小和最大高度

# 6. 分割小矩形并保存
rect_count = 0
for i, contour in enumerate(contours):
    # 获取矩形边界
    x, y, w, h = cv2.boundingRect(contour)

    # 过滤掉尺寸不符合的矩形
    if min_width <= w <= max_width and min_height <= h <= max_height:
        # 提取并保存每个小矩形
        cropped = image[y+2:y + h-2, x+2:x + w-2]
        cv2.imwrite(os.path.join(output_dir, f'rectangle_{rect_count}.png'), cropped)
        rect_count += 1

# 显示结果
cv2.imshow('Detected Lines and Rectangles', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
