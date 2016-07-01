from sklearn               import svm
from scipy.misc            import imread
from glob                  import glob
from itertools             import repeat
from sklearn.decomposition import RandomizedPCA

import pickle

pcaComponents = 200

guyImgFiles   = glob('faces/guy-fawkes/*')
otherImgFiles = glob('faces/other/*')

guyImgs         = list(map(imread, guyImgFiles))
otherImgs       = list(map(imread, otherImgFiles))
trainingImgs    = list(map(lambda i: i.reshape((-1)), guyImgs+otherImgs))
trainingClasses = list(repeat(1, len(guyImgs)))+list(repeat(0, len(otherImgs)))

print('images loaded')

pca = RandomizedPCA(n_components=pcaComponents, whiten=True).fit(trainingImgs)
trainingPca = pca.transform(trainingImgs)

print('pca created')

model = svm.SVC(verbose = True)
model.fit(trainingPca, trainingClasses)

print('model trained')

pickle.dump(pca,   open('pca.pickle',   'wb'))
pickle.dump(model, open('model.pickle', 'wb'))

