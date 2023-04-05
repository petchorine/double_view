import sys
import cv2

# on crée un objet VideoCapture avec 3 arguments :
# - 0 si une seule caméra ou entre 0 et N-1 si N caméras reliées à l'ordinateur
# - "cv2.CAP_ANY" permet une détection automatique de la caméra par défaut
flux = cv2.VideoCapture(0, cv2.CAP_ANY)
# vérifie si le flux est ouvert - sinon sort du programme
if not flux.isOpened():
    print("Le flux ne peut être ouvert")
    sys.exit()
while True:
    # fonction "read" retourne un tuple de 2 valeurs :
    # - True lorsque l'image est lue
    # - un tableau Numpy contenant l'image
    ret, img = flux.read()
    # si erreur - on quitte le programme
    if not ret:
        print("erreur ou fin de la lecture du flux.")
        break
    # sinon prépare l'affichage avec les 2 fonctions "imshow" et "pollkey"
    cv2.imshow('Webcam', img)
    # sort du programme si on appuie sur "q"
    if cv2.pollKey() == ord('q'):
        break
# à la fin de la boucle while, on ferme le flux video avec "release"
flux.release()
# et on ferme toutes les fenêtres
cv2.destroyAllWindows()