#trying to add all list together and calculate the mean value, and extract authentication data
from PIL import Image
import numpy

index = 1
final_value = 0
block_mean = []

for i in range(3175):
   im = Image.open(r"C:\Users\Zhipeng Wang\Desktop\testResult\result" +str(index) +".png")
   index += 1 
   np_im = numpy.array(im)
   length, width = im.size
   'print(im)'
   'print(length)'
   'print(width)'
   'print(np_im[0][0])'
   summary = 0
   'print(sum(np_im[0][0]))'


   for i in range(length):
      for j in range(width):
         summary += sum(np_im[i][j])
         #print(summary)
         #print(np_im[i][j])
   final_value += summary / 16
   block_mean.append(final_value)
   final_value = 0 
   
'print(block_mean)'
i = 0;
recovery_data = []
'print(len(block_mean))'

while i != (3174 - i):
   recovery_data += (block_mean[i], block_mean[3174 - i])
   i += 1

recovery_data += recovery_data
'print (bin(255)[2:])'

#now we get the combination of M1, M2
'recovery_data.sort()'
'print (recovery_data[0])'
print (len(recovery_data))


#this step we get the mean value of the image
'print(int(final_value))'
#convert it binary value, now it is a string, we have to convert it to integer
'mean_value = bin(int(final_value))[2:]'
#in this time, the value still as string
'recovery_bits = mean_value[0:8]'
'print (type(mean_value))'
'print(recovery_bits)'
'print(mean_value)'
#for step 3, since we didn't have the secret key, we would assume that mapping is M1 to B1 directly
#now we jump to step 3
#we will get the k-bit authentication data Ai for each Bi, there are two different elements in authentication data
#we got four authentication bits instead of 8 bits, what should we do??????????????\
"""
im = Image.open(r"C:\\Users\Zhipeng Wang\\Desktop\\testResult\\result" +str(3174) +".png")
np_im = numpy.array(im)
print (sum(np_im[2][2]))
value = bin(int(sum(np_im[0][0])))[2:7]
new_value = int(value)
print(new_value)
result = 0
for i in range(5):
   result += 1*pow(2,i-1)
print(bin(int(result)))
"""
#since we set all part is gray so that all the 5 MSB is 11111, decimal value would be 11111, by simplifying authentication data, we use {0,1},1xor1xor1xor, 1, the second 1 is the middle number
#then, we get the authentication data a1 = 0, a2 = 1


#embedd all the data into the original image, recovery to 1 LSB of each pixel, authentication to 2 LSB, 3 LSB of each pixel, first we insert authentication data
'im = Image.open(r"C:\\Users\\Zhipeng Wang\\Desktop\\testResult\\result1.png")'
#now it is the time to insert recovery data in there
#change the value to string and concatenate them together
data = ""
for i in recovery_data:
   'print(bin(int(i)))'
   re_data = bin(int(i))[2:10]
   'print(re_data)'
   'break'
   data += re_data
'print(data)'
#now we just insert the authentication data and recovery data

im = Image.open(r"C:\Users\Zhipeng Wang\Desktop\gray_logo.png")
length, width = im.size
np_im = numpy.array(im)
#print(np_im)
count = 0

"""
for i in range(length):
   for j in range(width):
      print(np_im[i][j])
"""
#question when get the new binary value, how to convert it into numpy array?
#new_np = numpy.empty([400,400, 2], dtype = str)
#new_np = numpy.zeros(shape=(400,2))
'print(len(data))'

for i in range(length):
   for j in range(width):
      if count < len(data):
         
         value1 = bin(int(np_im[i][j][0]))
         value2 = bin(int(np_im[i][j][1]))
         
         'print("This is %d", jishu)'
      
         new1 = str(value1)[0:-1] + data[count]
         
         
         #print(str(value2)[0:-1])
         new2 = str(value2)[0:-1] + data[count + 1]
         'print(new2)'
         count += 2
         #we need to figure out how to insert string into numpy array
         
         np_im[i][j][0] = int(new1[2:],2)
         
         
         #print(bin(int(np_im[i][j][1]))[2:-1])
         np_im[i][j][1] = int(new2[2:],2)
         #print(np_im[i][j][1])
     

#print (np_im[0][0])
img = Image.fromarray(np_im)
#im.show(img)
#img.save(r"C:\Users\Zhipeng Wang\Desktop\logo_watermark.png")



#print(type(data))
#print(data[0])

