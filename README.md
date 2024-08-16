#FILMY Skopiuj lijniki 1, 2, 3,...,24 do Google Colab. W tym celu otwórz ten plik w odpowiednim formacie np. https://github.com/matematyknauka/ESRGAN/blob/main/README.md?plain=1
#Konfiguracja
from google.colab import drive #Podłączanie Dysku
drive.mount('/content/drive') #Google
%cd /content/drive/MyDrive/Colab Notebooks #Przejście do katalogu głównego Google Colab
!rm -rf ./ESRGAN #Usunięcie katalogu ESRGAN o ile go posiadasz w katalogu głównym Google Colab
!git clone https://github.com/matematyknauka/ESRGAN.git #Sklonowanie repozytorium
%cd /content/drive/MyDrive/Colab Notebooks/ESRGAN #Przejście do sklonowanego katalogu ESRGAN
!pip install opencv-python-headless torch torchvision moviepy pillow numpy #Instalacja pakietów
!rm -rf ./LR/img/* #Opróżnienie katalogu /ESRGAN/LR/img
!rm -rf ./results/film/* #Opróżnienie katalogu /ESRGAN/results/film
!rm -rf ./results/img/* #Opróżnienie katalogu /ESRGAN/results/img
#Koniec konfiguracji

#Skrypt superrozdzielczości Importy ze skryptów .py
import film_na_klatki as fkl
import img_modul as im
import klatki_na_sekunde as ks
import laczenie as L
#Metody z plików
fkl.film_na_klatki("./LR/film/Kamil_sd.mp4", "./LR/img")
im.img_modul("./LR/img", "./results/img")
L.laczenie("./results/img", "./results/film", ks.klatki_na_sekunde("./LR/film/Kamil_sd.mp4"))
#Koniec skryptu superrozdzielczości
