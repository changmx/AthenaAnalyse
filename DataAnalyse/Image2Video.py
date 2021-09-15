import cv2
import os
from PIL import Image
import re

fps = 50  #视频每秒帧数

dir = r'D:\bb2021\statLumiPara\2021_0913\1801_59\new1\electron_bunch0_xpx'

name = os.listdir(dir)
for iname in name:
    if 'avi' in iname:
        name.remove(iname)
name.sort(key=lambda x: int(re.match(r'(.*)_([0-9]*).(.*)', x).group(2)))
# print(name)
file = [os.sep.join([dir, iname]) for iname in name]
# print(file)
figure_w = Image.open(file[0]).width
figure_h = Image.open(file[0]).height

video = cv2.VideoWriter(
    os.sep.join([dir, '1.avi']), cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
    fps, (figure_w, figure_h))  #视频保存在设定目录下, 格式为 motion-jpeg codec，图片颜色失真比较小

for ifile in (file):
    print(ifile)
    figure = cv2.imread(ifile)
    video.write(figure)

video.release()
cv2.destroyAllWindows()
print('Video has been made.')
