from sklearn    import svm
from scipy.misc import imread
from glob       import glob
from itertools  import repeat

import pickle

guyImgFiles   = glob('faces/guy-fawkes/*')
otherImgFiles = glob('faces/other/*')

guyImgs   = list(map(imread, guyImgFiles))
otherImgs = list(map(imread, otherImgFiles))

trainingImgs = list(map(lambda i: i.reshape((-1)), guyImgs+otherImgs))
trainingClasses = list(repeat(1, len(guyImgs)))+list(repeat(0, len(otherImgs)))

print('images loaded')

model = svm.SVC(verbose = True)
model.fit(trainingImgs, trainingClasses)

print('model trained')

pickle.dump(model, open('model.pickle', 'wb'))

