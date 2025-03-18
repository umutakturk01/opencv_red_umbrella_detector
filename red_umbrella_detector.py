import cv2
import numpy as np
import imutils 
 



img = cv2.imread("image.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#burada renk aralığını tanımlıyoruz
kirmizi_alt_deger = np.array([0,120,100])
kirmizi_ust_deger = np.array([10, 255, 255])
#range komutu ile aralığı aktif ediyoruz
mask = cv2.inRange(hsv,kirmizi_alt_deger,kirmizi_ust_deger)
#contoursları buluyoruz
cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#imutils alanı bulmamıza yardımcı oluyor
cnts = imutils.grab_contours(cnts)
sayac = 0
for c in cnts:
    #alan verisini alıyoruz
    alan = cv2.contourArea(c)
    print('Alan:  ', alan)
    #alan karşılaştırması yapıyoruz şemsiyeyi bulmak için
    if alan > 1000: sayac += 1
    #alanı boyuyoruz
    cv2.drawContours(img,[c],-1,(0,255,0),3)

print("Kırmızı şemsiye sayısı = ", sayac)

while True:
      cv2.imshow("Image", img)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break