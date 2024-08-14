def klatki_na_sekunde(path):
    import cv2
    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps