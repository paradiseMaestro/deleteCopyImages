import os
import cv2
import numpy as np
# print(os.listdir())
import shutil















# q = os.listdir('w')
# # print(q)

# i = 0
# img = cv2.imread('./w/'+str(i)+'.jpg', cv2.COLOR_BGR2RGB)
# img1 = cv2.imread('./w/'+str(i+1)+'.jpg', cv2.COLOR_BGR2RGB)

# print(np.array(img) == np.array(img))
# while( i < len(q)-1):
#     img = cv2.imread('./w/'+str(i)+'.jpg', cv2.COLOR_BGR2RGB)

#     i = i + 1



# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------

from PIL import Image
from PIL import ImageChops

# image_one = Image.open('q.jpg')
# image_two = Image.open('w.jpg')

# diff = ImageChops.difference(image_one, image_two)

# if diff.getbbox():
#     print("no")
# else:
#     print("yes")


def IsTrue(el1,el2):
    diff = ImageChops.difference(Image.open(el1), Image.open(el2))
    if diff.getbbox():
        return False
    else:
        return True

# print(
#     IsTrue(
#         'q.jpg','w.jpg'
#     )
# )



# i = 0 

# while(True):
#     q = os.listdir('w')
#     if(len(q)==1):
#         break
#     t = 1
#     listOfCopy = []
#     while (t < len(q)-1):
#         if(IsTrue('./w/' + q[0], './w/' + q[t]) ):
#             listOfCopy.append('./w/' + q[t])
#         t = t + 1
#     print(listOfCopy)
#     if(len(listOfCopy)==0):
#         pass
#     if(len(listOfCopy)==1):
#         pass
#     else:
#         n = 0
#         while (n < len(listOfCopy) -1):
#             os.remove(listOfCopy[n])
#             n = n + 1
#     shutil.move('./w/' + q[0], './TrueWomen/' + str(i) + '.jpg')
#     i = i + 1
#     # print(i)





i = 0 

while(True):
    q = os.listdir('w')
    if(len(q)==0):
        pass
    if(len(q)==1):
        shutil.move('./w/' + q[0], './TrueWomen/' + str(i) + '.jpg')
        pass
    t = 1
    listOfCopy = []
    while (t < len(q)-1):
        if(IsTrue('./w/' + q[0], './w/' + q[t]) ):
            os.remove('./w/' + q[t])
        t = t + 1
    shutil.move('./w/' + q[0], './TrueWomen/' + str(i) + '.jpg')
    i = i + 1
    # print(i)











# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------
# --------------------------------------------------------------

























































# q = os.listdir('w')

# i = 0
# while( i < len(q)-1):
#     img = cv2.imread('./w/'+q[i], cv2.IMREAD_UNCHANGED)
#     image_one = Image.open('./w/'+q[i])
#     t = 0
#     W = os.listdir('./Women')

#     tr = True
#     while( t < len(W)-1):
#         image_two = Image.open('./Women/'+W[t])
#         diff = ImageChops.difference(image_one, image_two)
#         if diff.getbbox():
#             print("no")
#             tr = True
#         else:
#             print("yes")
#             tr = False
#         t = t + 1
#     # break
#     t = 0
#     if(tr):
#         cv2.imwrite('./Women/'+str(i)+'.jpg',img)
#     else:
#         pass
#     i = i + 1







































# from PIL import Image



# i = 0

# while( i < len(q)-1):
#     # im = Image.open(q[i])
#     # rgb_im = im.convert('RGB')
#     # rgb_im.save('../q/'+str(i) + '.jpg')
#     os.rename(q[i], '../q/'+str(i) + '.jpg')
#     i = i + 1











# import cv2
# img = cv2.imread('0.jpg', cv2.IMREAD_UNCHANGED)
# resized_image = cv2.resize(img, (255, 255)) 
# cv2.imwrite("file.jpg",resized_image)



# q = './Female Faces/0.jpg'
# w = './m/0.jpg'

# i = 0
# while( i <= 2639):
#     img = cv2.imread('./Male Faces/'+str(i)+'.jpg', cv2.IMREAD_UNCHANGED)
#     resized_image = cv2.resize(img, (255, 255)) 
#     cv2.imwrite('./m/'+str(i)+'.jpg',resized_image)
#     i = i + 1
# # 2639


































