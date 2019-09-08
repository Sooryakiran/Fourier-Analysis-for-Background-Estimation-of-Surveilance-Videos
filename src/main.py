import cv2
import numpy as np
import utils
import fourrier

path = "../Tests/test2.mp4"
cap = cv2.VideoCapture(path)
ret, now = cap.read()

images = []
i = 1

background = np.zeros_like(now) + 0.5
num_updates = np.zeros_like(now) + 1

while(i>=1):

    ret, now = cap.read()
    now = utils.blur(now)

    # manage image bundle
    images.append(cv2.cvtColor(now,cv2.COLOR_BGR2GRAY)/255)
    if len(images) > 10:
        images.pop(0)

    # get motion detection
    i+=1

    # frame skip
    if i%4 == 1:
        motion = fourrier.image_fft(np.asarray(images))[0, :, :]
        thresh = utils.white_mask(motion)

        masked = now.copy()
        for i in range(3):
            masked[:, :, i] = masked[:, :, i] * thresh/255

        # update mean background
        current_background = now - masked
        background_delta = (current_background/255 - background)/(num_updates + 1e-4)
        background = background + background_delta
        num_updates[thresh != 1] = num_updates[thresh != 1] + 1

        # output
        cv2.imshow("Input Video", now)
        cv2.imshow("Exctracted background", background)

        cv2.waitKey(1)
