import cv2
import sys

from os         import listdir
from os.path    import isfile, join
from glob       import glob
from scipy.misc import imread, imsave

guyImgPath   = 'imgs/guy-fawkes'
guyFacePath  = 'faces/guy-fawkes'

otherImgPath  = 'imgs/other'
otherFacePath = 'faces/other'

guyImgs   = glob(guyImgPath+'/*')
otherImgs = glob(otherImgPath+'/*')

cascPath = '/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

def findFaces(imgs, outDir):
    faceIndex = 0

    for imgPath in imgs:
        try:
            img = imread(imgPath)

            faces = faceCascade.detectMultiScale(
                img,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                print('saving face %d from image %s' % (faceIndex, imgPath))
                faceFilename = outDir+('/face_%04d.png' % faceIndex)
                face = img[y:y+h, x:x+w]
                face = cv2.resize(face, (64, 64))
                imsave(faceFilename, face)
                faceIndex += 1

        except:
            print('Error: ', sys.exc_info())

        if faceIndex >= 1000:
            break

findFaces(guyImgs,   guyFacePath);
findFaces(otherImgs, otherFacePath);
