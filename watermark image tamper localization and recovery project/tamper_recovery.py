from PIL import Image
import numpy

img = Image.open(r"C:\Users\Zhipeng Wang\Desktop\tampered_image_sample2.png")
#img = Image.open(r"C:\Users\Zhipeng Wang\Desktop\tampered_image_sample1.png")
'img.show()'
length, width = img.size
np_im = numpy.array(img)
'print(np_im)'

data = ""
count = 0
#get the last bit from each pixel
for i in range(length):
    for j in range(width):
        if count < 50784:
            'print(np_im[i][j])'
            
            data += str(bin(int(np_im[i][j][0])))[-1]
            data += str(bin(int(np_im[i][j][1])))[-1]
            count += 2
    
#print(data)

#parse the long sting into 8 bits for each, create a list to save it
recovery_data = []
i = 2
'print(len(data))'
#during this stage, we get all the information bits out and convert them into integer

while i < len(data):
    recovery_data.append(int(data[i:i+8],2))
    i += 8

#the number is matched
#print(len(recovery_data))
#print(recovery_data)
i = 0
real_recovery_data = [[] for i in range(0,3174)]
j=0

while j < 3174:
    real_recovery_data[j].append([recovery_data[j], recovery_data[j+3174]])
    j += 1

"""
for i in range(29):
    print(real_recovery_data[i])
    """
print(real_recovery_data[293])
#object1 = real_recovery_data[299]
#print(object1)

target = object1[0][1]
#print(target[0][1])

for i in range(16):
    for j in range(16):
        np_im[i][j] = [target * 1/ 100, target * 99/ 100]
        
img2 = Image.fromarray(np_im)
img2.show()

#img2.save(r"C:\Users\Zhipeng Wang\Desktop\recovered_image.png")

    
    
