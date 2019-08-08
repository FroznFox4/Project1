import numpy as np
import cv2
from mss.linux import MSS as mss
import base64
import pickle
from io import BytesIO
from PIL import Image

# rgb img -> witeandblack img
def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    return processed_image

def new_image_string():
#   ScreenShot
    mon = {'top': 600, 'left': 130, 'width': 100, 'height': 130}
    sct = mss()
    
    while True:
        img = sct.grab(mon)
        img = np.array(img)
        img = process_image(img)
        
    #    visualise
        cv2.imshow('hello', img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    #img -> base64
    pil_img = Image.fromarray(img)
    buff = BytesIO()
    pil_img.save(buff, format="PNG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
    return(new_image_string)

if __name__ == '__main__':
    new_image_string()
