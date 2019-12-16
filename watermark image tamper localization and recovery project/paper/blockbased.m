function blockbased(host,watermark,alpha)
% blockbased(graylevel_host, color_watermark, alpha)
% e.g. blockbased('lena_256.bmp','logo.jpg',100)

logo = imread(watermark);
host = imread(host);
logo_small = imresize(logo,[37,73]);
logo_gray = rgb2gray(logo_small);
logo_binary = im2bw(logo_gray,graythresh(logo_gray));
% imshow(logo_binary) 

% construct the blocked watermark
number = round(alpha/9);
[row, col] = size(logo_binary);
block_wm = zeros(row*3,col*3);
for i = 1:row
    for j = 1:col
        if logo_binary(i,j) ~= 0
           for m = (3*i - 2) : (3*i)
                for n = (3*j - 2) : (3*j)
                    block_wm(m,n) = number;
                end
           end
        end
    end
end
% imshow(block_wm,[])

% put blocked watermark on host image
[row_block, col_block] = size(block_wm);
host_wm = host;
for i = 1:row_block
    for j = 1:col_block
        temp = double(host(i,j)) + double(block_wm(i,j)); 
        host_wm(i,j) = temp;
    end
end
figure(1), imshow(host_wm,[]);

% extraction same as substitution
end