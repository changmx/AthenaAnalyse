import cv2
import os
from PIL import Image

fps = 60  #视频每秒帧数

path = r'D:\bb2021\statLumiPara\2021_0909\1230_23\figure_distribution\fixPoint\electron_bunch0_xpx\1230_23_electron_bunch0_xpx_'
figure_ini_path = path + '0.png'
figure_ini_read = Image.open(figure_ini_path)
figure_w = figure_ini_read.width
figure_h = figure_ini_read.height

video = cv2.VideoWriter(
    path + r'Video_xpx' + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
    fps, (figure_w, figure_h))  #视频保存在设定目录下, 格式为 motion-jpeg codec，图片颜色失真比较小
Nturn = 2048
for i in range(Nturn):
    png = cv2.imread(path + str(i) + '.png')
    # print(path+suffix+str(i)+'.png')
    video.write(png)
    if i % 100 == 0:
        print(i)

video.release()
cv2.destroyAllWindows()
print('Video has been made.')
