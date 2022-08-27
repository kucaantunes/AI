import cv2
import time
import numpy as nump
from matplotlib import pyplot as plot

figura = plot.figure()
auxiliar = figura.add_subplot(111)
coracaobeat_counter = 128


captured = cv2.cv2.VideoCapture(0)

captured.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)

captured.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

captured.set(cv2.CAP_PROP_FPS, 60)


coracaobeatvalues = [0]*coracaobeat_counter
timescoracaobeat = [time.time()]*coracaobeat_counter





while(True):
    
    x, y, w, h = 950, 300, 500, 500
    ret, frame = captured.read()
    picture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imagemmcut = picture[y:y + h, x:x + w]
   
    coracaobeatvalues = coracaobeatvalues[1:] + [nump.average(imagemmcut)]
    timescoracaobeat = timescoracaobeat[1:] + [time.time()]
    
    
    auxiliar.plot(timescoracaobeat, coracaobeatvalues)
    figura.canvas.draw()
    plotimagemm = nump.fromstring(figura.canvas.tostring_rgb(),
                                dtype=nump.uint8, sep='')
    plotimagemm = plotimagemm.reshape(figura.canvas.get_width_height()[::-1] + (3,))
    plot.cla()
    
    cv2.imshow('Graph', plotimagemm)
    cv2.imshow('Crop', imagemmcut)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captured.release()
cv2.destroyAllWindows()