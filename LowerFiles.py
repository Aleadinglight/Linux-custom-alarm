import os

rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):
  print('Found directory: %s' % dirName)

  for fname in fileList:
    print('\t%s' % fname)
    new_fname = fname.lower()
    src=dirName+'/'+fname
    dst=dirName+'/'+new_fname
    print(src, dst)
    os.rename(src, dst)
