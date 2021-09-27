import dropbox
import time
import random
import cv2

startTime = time.time()

def takeSnapShot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    
    while(result):
        ret, frame = videoCaptureObject.read()
        imageName = 'img'+str(number)+'.png'
        cv2.imWrite(imageName, frame)
        startTime = time.time
        result = False

    return imageName

    print('Snapshot has been successfully taken')

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(imageName):
    accessToken = '74-gnWLkl4cAAAAAAAAAAYbWHePBcNAyLX5KQkPjXTvC_1HASt4ldXmMbaT-02PB'
    file = imageName
    fileFrom = file
    fileTo = '/securityCamera/'+imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(fileFrom, 'rb')as f:
        dbx.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
        print('File successfully uploaded!')

def main():
    while(True):
        if((time.time()-startTime)>=10):
            name = takeSnapShot()
            uploadFiles(name)
    


main()
