import os
import shutil 

folder_path = './'  # 要操作的文件夹的路径

# 列出文件夹下所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('_mask.png'):   # 如果文件是png且以'_mask.png'结尾
        new_filename = filename.replace('_mask.png', '.png')
        # 重命名
        os.rename(os.path.join(folder_path, filename), 
                  os.path.join(folder_path, new_filename))
