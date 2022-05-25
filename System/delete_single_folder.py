import os
import shutil

for root, dirs, files in os.walk(
        r'D:\OneDrive\模拟数据',
        topdown=False):
    # for name in files:
    #     print(os.path.join(root, name))
    for name in dirs:
        # print(os.path.join(root, name))
        if 'single' in name:
            print(os.path.join(root, name))
            shutil.rmtree(os.path.join(root, name))