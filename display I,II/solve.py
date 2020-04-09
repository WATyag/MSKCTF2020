import cv2
import numpy as np
#./mctf/lupaza/jpgs/ - путь до папки с кадрами гифки
#qr код появляется на изображениях от 343 до 420

control_img=cv2.imread("./mctf/lupaza/jpgs/frame_343_delay-0.03s.png")
marker=np.ndarray(shape=(3,),buffer=np.array([0,255,0]),offset=0,dtype=int)
gray=np.ndarray(shape=(3,),buffer=np.array([151,151,151]),offset=0,dtype=int)
red=np.ndarray(shape=(3,),buffer=np.array([0,0,255]),offset=0,dtype=int)
black=np.ndarray(shape=(3,),buffer=np.array([0,0,0]),offset=0,dtype=int)
brown=np.ndarray(shape=(3,),buffer=np.array([0,0,62]),offset=0,dtype=int)
white=np.ndarray(shape=(3,),buffer=np.array([255,255,255]),offset=0,dtype=int)
for m in range(344,420):
    img = cv2.imread("./mctf/lupaza/jpgs/frame_"+str(m)+"_delay-0.03s.png")
    x,y=0,0
    for i in img:
        y=0
        for j in i:

            if(img[x,y].tolist()!=control_img[x,y].tolist()):
                control_img[x,y]=marker #отмечаем пиксели которые изменяютя
            y+=1
        x+=1


readed=cv2.imread("./mctf/lupaza/jpgs/frame_383_delay-0.03s.png")
resulted=cv2.imread("./mctf/lupaza/jpgs/frame_344_delay-0.03s.png")

shift=0
for i in range(91,198): #часть рамки вокруг кода, без этого код не сканировался
    for j in range(4,13):
        resulted[j,i]=white

for m in range(345,420):
    img = cv2.imread("./mctf/lupaza/jpgs/frame_"+str(m)+"_delay-0.03s.png")
    x,y=100,0
    for i  in range(241-shift*3,330-shift*3):
        y=13
        for j in range(13,99):
            if (control_img[j,i].tolist()==marker.tolist()):#если пиксель изменялся, а значит нанем нет помехи
                if((img[j,i].tolist()==red.tolist())or(img[j,i].tolist()==gray.tolist())): #собираем черно-белый код
                    resulted[y,x]=black
                else:
                    resulted[y,x]=white
            y+=1
        x+=1
    shift+=1



cv2.imshow("Image", resulted)#выводится читаемый код
cv2.waitKey(0)
cv2.destroyAllWindows()
