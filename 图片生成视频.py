import cv2
import os

fps = 10 #视频每秒1帧
size = (6*300,4*300) #需要转为视频的图片的尺寸,  可以使用cv2.resize()进行修改
suffix=r'\fig_positron_turn' #文件路径前缀
angle=11
path = r'E:\changmx\bb2019\distribution\2020_1103\figure'
video = cv2.VideoWriter(path+r'\Video_halfPhi_'+str(angle)+'.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)   #视频保存在设定目录下, 格式为 motion-jpeg codec，图片颜色失真比较小
Nturn= 100
for i in range(1,Nturn+1):
    png = cv2.imread(path+suffix+str(i)+'.png')
    # print(path+suffix+str(i)+'.png')
    video.write(png)
    

video.release()
cv2.destroyAllWindows()
print('Video has been made.')
