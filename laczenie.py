from os.path import join
import cv2
import os

def laczenie(katalog_foto, katalog_film, fps):
    height, width, layers = cv2.imread(join(katalog_foto, os.listdir(katalog_foto)[0])).shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(join(katalog_film, "film.mp4"), fourcc, fps, (width, height))
    for img in os.listdir(katalog_foto):
        img = cv2.imread(join(katalog_foto,img))
        video.write(img)
# Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated
