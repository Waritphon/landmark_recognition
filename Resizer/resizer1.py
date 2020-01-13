#usage
#place this python script in the same directory as image directory
#this script will make a subfolder to store the resized image

########## This resizer will solely use old fashioned resize ##########

########## Set path here #########
PATH = 'resized'
########## Set path here #########
import cv2, os, multiprocessing


def resize(img):
    if img[-1] != 'g': return
    #print(img)
    try:
        image = cv2.imread(img)
        image = cv2.resize(image, (320, 240))
        cv2.imwrite(PATH+'/'+img, image)
        print('resized '+img)
    except Exception as e:
        print('error at: '+ img)
        print(e)

if __name__ == '__main__':
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    pool = multiprocessing.Pool(processes=50)
    pool.map(resize, os.listdir())
    print('done resizing!!')