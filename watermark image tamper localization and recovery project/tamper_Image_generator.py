from PIL import Image
import numpy

image=Image.open(r'C:\Users\Zhipeng Wang\Desktop\logo_watermark.png')

#length, width = image.size
#np_im = ["0", "0"]
#print (np_im[0][0])

#we generate the first sample that large part of image is tampered
"""
np_im1 = numpy.array(image)
for i in range(299):
   for j in range(299):
       np_im1[i][j] = ["0", "0"]
img1 = Image.fromarray(np_im1)
img1.show()
"""
#img1.save(r"C:\Users\Zhipeng Wang\Desktop\tampered_image_sample1.png")


#the second sample is that only small part are tampered

np_im2 = numpy.array(image)
#print(np_im2[0][0])
"""
for i in range(10):
       for j in range(10):
             np_im2[i][j] = [0,128] 
img2 = Image.fromarray(np_im2)
img2.show()
"""

for i in range(0, 50):
   for j in range(0, 50):
       np_im2[i][j] = ["255", "255"]
img2 = Image.fromarray(np_im2)

img2.show()

img2.save(r"C:\Users\Zhipeng Wang\Desktop\tampered_image_sample2.png")
