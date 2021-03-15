import cv2
import matplotlib.pyplot as plt
import numpy as np
import playsound
from PIL import Image
from matplotlib import animation

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

VidCap = cv2.VideoCapture(r'BadApple30fps.mp4')
plt.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg.exe'

def Update(i):
    try:
        _, frame = VidCap.read()
        ax1.clear()
        ImgArray = np.array(Image.fromarray(frame).convert('L'))
        ax1.matshow(ImgArray)
    except Exception as Err:
        if type(Err) == AttributeError:
            print('Song has finished')
            exit()
        print(Err)
        exit()


ani = animation.FuncAnimation(fig, Update, interval=((1 / 10) * 1000), save_count=2190)
ani.save('animation.mp4', writer='ffmpeg')
playsound.playsound(r'SyncAudio.mp3', False)
plt.show()
