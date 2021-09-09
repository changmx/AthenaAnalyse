import cv2
import os
from PIL import Image

fps = 20  #视频每秒帧数

path = r'D:\bb2021\statLumiPara\2021_0909\1230_23\figure_distribution\fixPoint\electron_bunch0\1230_23_electron_bunch0_'
figure_ini_path = path + '0_xpx.png'
figure_ini_read = Image.open(figure_ini_path)
figure_w = figure_ini_read.width
figure_h = figure_ini_read.height

video = cv2.VideoWriter(
    path + r'\Video_xpx' + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
    fps, (figure_w, figure_h))  #视频保存在设定目录下, 格式为 motion-jpeg codec，图片颜色失真比较小
Nturn = 2048
for i in range(Nturn):
    png = cv2.imread(path + str(i) + '_xpx.png')
    # print(path+suffix+str(i)+'.png')
    video.write(png)
    if i % 100 == 0:
        print(i)

video.release()
cv2.destroyAllWindows()
print('Video has been made.')
