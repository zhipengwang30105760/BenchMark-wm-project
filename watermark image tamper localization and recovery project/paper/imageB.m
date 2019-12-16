%image binarization
%we first read an image and convert it to grayscale image
img=imread('cai.jpg');
gray_img=rgb2gray(img);
figure,imshow(gray_img)
% custom threshold value
threshold = 100; 
% if threshold < 0 || threshold > 255
%     error('You input an invalid number');
% end
%get the image binarization based on different threshold value
result = gray_img > threshold;
figure,imshow(result)
