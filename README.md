Pierwsza komórka (Jak będzie problem to podziel ją na osobne komórki).

from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/Colab Notebooks
!rm -rf ./ESRGAN
!git clone https://github.com/matematyknauka/ESRGAN.git
%cd /content/drive/MyDrive/Colab Notebooks/ESRGAN
!pip install opencv-python-headless torch torchvision moviepy pillow numpy
!rm -rf ./LR/img/*
!rm -rf ./results/film/*
!rm -rf ./results/img/*

Koniec pierwszej komórki

Druga komórka

import film_na_klatki as fkl
import img_modul as im
import klatki_na_sekunde as ks
import laczenie as L

fkl.film_na_klatki("./LR/film/Kamil_sd.mp4", "./LR/img")
im.img_modul("./LR/img", "./results/img")
L.laczenie("./results/img", "./results/film", ks.klatki_na_sekunde("./LR/film/Kamil_sd.mp4"))

Koniec drugiej komórki
