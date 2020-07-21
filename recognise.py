# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pyttsx3


def nothing(x):
    pass


#image_x, image_y = 200, 200
image_x, image_y = 64, 64

import tensorflow as tf

#from keras.models import load_model

#classifier = tf.keras.models.load_model('Trained_model_2.h5')
classifier = tf.keras.models.load_model('Trained_model.h5')

#def sentence(arr):
#    result = ''
#    for i in arr:
#        result += str(i)
#    return result    

def speak(sen):
    # initialisation
    engine = pyttsx3.init()
    
    # testing
    engine.say(sen)
    engine.runAndWait()
     
arr_sentence = []
def predictor():
    import numpy as np
    from keras.preprocessing import image
#    test_image = image.load_img('1.png', target_size=(200, 200))
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    keypress = cv2.waitKey(1) & 0xFF
    if result[0][0] == 1:        
        if keypress == ord("a"):
            arr_sentence.append('A')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][1] == 1:
        if keypress == ord("a"):
            arr_sentence.append('B')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][2] == 1:
        if keypress == ord("a"):
            arr_sentence.append('C')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][3] == 1:
        if keypress == ord("a"):
            arr_sentence.append('D')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][4] == 1:
        if keypress == ord("a"):
            arr_sentence.append('E')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][5] == 1:
        if keypress == ord("a"):
            arr_sentence.append('F')    
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][6] == 1:
        if keypress == ord("a"):
            arr_sentence.append('G') 
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][7] == 1:
        if keypress == ord("a"):
            arr_sentence.append('H')   
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][8] == 1:
        if keypress == ord("a"):
            arr_sentence.append('I')  
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][9] == 1:
        if keypress == ord("a"):
            arr_sentence.append('J') 
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][10] == 1:
        if keypress == ord("a"):
            arr_sentence.append('K')    
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][11] == 1:
        if keypress == ord("a"):
            arr_sentence.append('L')  
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][12] == 1:
        if keypress == ord("a"):
            arr_sentence.append('M')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][13] == 1:
        if keypress == ord("a"):
            arr_sentence.append('N')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][14] == 1:
        if keypress == ord("a"):
            arr_sentence.append('O')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][15] == 1:
        if keypress == ord("a"):
            arr_sentence.append('P')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][16] == 1:
        if keypress == ord("a"):
            arr_sentence.append('Q')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][17] == 1:
        if keypress == ord("a"):
            arr_sentence.append('R')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][18] == 1:
        if keypress == ord("a"):
            arr_sentence.append('S')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][19] == 1:
        if keypress == ord("a"):
            arr_sentence.append('T')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][20] == 1:
        if keypress == ord("a"):
            arr_sentence.append('U')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][21] == 1:
        if keypress == ord("a"):
            arr_sentence.append('V')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][22] == 1:
        if keypress == ord("a"):
            arr_sentence.append('W')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][23] == 1:
        if keypress == ord("a"):
            arr_sentence.append('X')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][24] == 1:
        if keypress == ord("a"):
            arr_sentence.append('Y')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
    elif result[0][25] == 1:
        if keypress == ord("a"):
            arr_sentence.append('Z')
#        print(*arr_sentence)
#        return sentence(arr_sentence)
#    print(arr_sentence)    
    if keypress == ord("s"):
        arr_sentence.append(" ")
    if keypress == ord("d"):
        arr_sentence.pop()        
    sentence = ''.join(arr_sentence)   
    if keypress == ord("t"):
        speak(sentence)
    return sentence

#-------------------------------------------------------
def predictor_letter():
    import numpy as np
    from keras.preprocessing import image
#    test_image = image.load_img('1.png', target_size=(200, 200))
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)

    if result[0][0] == 1:
        return('A')
    elif result[0][1] == 1:
        return('B')
    elif result[0][2] == 1:
        return('C')
    elif result[0][3] == 1:
        return('D')
    elif result[0][4] == 1:
        return('E')
    elif result[0][5] == 1:
        return('F')
    elif result[0][6] == 1:
        return('G')
    elif result[0][7] == 1:
        return('H')
    elif result[0][8] == 1:
        return('I')
    elif result[0][9] == 1:
        return('J')
    elif result[0][10] == 1:
        return('K')
    elif result[0][11] == 1:
        return('L')
    elif result[0][12] == 1:
        return('M')
    elif result[0][13] == 1:
        return('N')
    elif result[0][14] == 1:
        return('O')
    elif result[0][15] == 1:
        return('P')
    elif result[0][16] == 1:
        return('Q')
    elif result[0][17] == 1:
        return('R')
    elif result[0][18] == 1:
        return('S')
    elif result[0][19] == 1:
        return('T')
    elif result[0][20] == 1:
        return('U')
    elif result[0][21] == 1:
        return('V')
    elif result[0][22] == 1:
        return('W')
    elif result[0][23] == 1:
        return('X')
    elif result[0][24] == 1:
        return('Y')
    elif result[0][25] == 1:
        return('Z')  


cam = cv2.VideoCapture(0)

#cv2.namedWindow("Trackbars")
#
#cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
#cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
#cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
#cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
#cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

cv2.namedWindow("test")

img_counter = 0

sentence_text = ''
letter_text = ''
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)    
    img = cv2.rectangle(frame, (425, 100), (625, 300), (0, 255, 0), thickness=2, lineType=8, shift=0)
    lower_blue = np.array([0, 48, 80], dtype = "uint8")
    upper_blue = np.array([20, 255, 255], dtype = "uint8")
    imcrop = img[102:298, 427:623]
    hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2GRAY)
    hsv = cv2.GaussianBlur(hsv, (7, 7), 0)
    cv2.putText(frame, sentence_text, (30, 350), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
    cv2.putText(frame, letter_text, (30, 450), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
    #------------------------------------------------------

#    keypress1 = cv2.waitKey(1) & 0xFF
#    if keypress1 == ord("n"):
#        cv2.putText(frame, sentence_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        
    
    ret,mask = cv2.threshold(hsv,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("test", frame)
    cv2.imshow("mask", mask)

    img_name = "1.png"
    save_img = cv2.resize(mask, (image_x, image_y))
    cv2.imwrite(img_name, save_img)
    print("{} written!".format(img_name))
    sentence_text = predictor()
    letter_text = predictor_letter()

#    if cv2.waitKey(1) == 27:
#        break
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord("q"):
            break

cam.release()
cv2.destroyAllWindows()