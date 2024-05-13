from PIL import Image
import numpy as np

image_path = r'F:\Users\Win\Desktop\wechat\unet_42-master\images\data\Training_Labels\000001_03_01_088.rf.e2e6e422b6e08766fba5def020203024.png'  # 图片路径


image = Image.open(image_path).convert('L')  # convert('L')表示转换为灰度图
gray_image = np.array(image)

# 将所有非零像素值设为128
gray_image[gray_image > 0] = 128

# 保存结果
result_image = Image.fromarray(gray_image)
result_image.save('result.png')