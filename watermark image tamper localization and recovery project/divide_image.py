from PIL import Image
import cv2
import numpy
import sys
import io
#A function that can cut image into small pieces
def cut_image(image):
	width,height=image.size
	item_width=int(width/86)
	'item_width=int(width/1)'
	box_list=[]
	count=0
	for j in range(0,86):
		for i in range(0,86):
			count+=1
			box=(i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width)
			box_list.append(box)
	'print(count)'
	'print("It process successfully")'
	image_list=[image.crop(box) for box in box_list]
	print(image_list[1])
	
	return image_list

def save_images(image_list):
	index=1
	
	for image in image_list:
		image.save(r'C:\Users\Zhipeng Wang\Desktop\testResult\result'+str(index)+'.png')
		index+=1

def get_RGB(image):
	np_im = numpy.array(im)
	print(np_im[0][0])
	print (np_im.shape)

if __name__ == '__main__':
	#open an image
	image=Image.open(r'C:\Users\Zhipeng Wang\Desktop\logo.png').convert('LA')
	#image.show()
	image.save(r'C:\Users\Zhipeng Wang\Desktop\gray_logo.png')
	#image=cv2.imread(r'C:\Users\Zhipeng Wang\Desktop\logo.jpg')
	#split the image
	image_list=cut_image(image)
	save_images(image_list)

