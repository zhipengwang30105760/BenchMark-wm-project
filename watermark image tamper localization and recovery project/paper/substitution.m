function substitution(host,watermark,place)
% substitution(graylevel_host, color_watermark, place_to_be_replaced)
% e.g. substitution('lena_256.bmp','logo.jpg',6)
% places 7 6 5 4 3 2 1 0

logo = imread(watermark);
host = imread(host);
logo_half = imresize(logo,[100,130]);
logo_gray = rgb2gray(logo_half);
logo_binary = im2bw(logo_gray,graythresh(logo_gray));

% Using LSB Bit subsititution
% logo size
[row col] = size(logo_binary);

host_wm = host;
for i = 1:row
    for j = 1:col
        % convert to its 8 bit binary
        temp_bi = dec2bin(double(host(i,j)),8); 
        
        % replace
        temp_bi(8-place) = num2str(logo_binary(i,j));
        
        host_wm(i,j) = bin2dec(temp_bi);
    end
end
figure(1), imshow(host_wm,[]);

% extract the watermark
water_ex = ones(row,col);
for i = 1:row
    for j = 1:col
            % convert to its 8 bit binary
            temp_bi = dec2bin(double(host_wm(i,j)),8);
            
            % extract from Bit position
            pos = temp_bi(8-place);   
            water_ex(i,j) = bin2dec(pos);   
    end
end
figure(2), imshow(water_ex,[]);

% Median filtering watermarked image
filter = fspecial('average', 3);
avg_wm = imfilter(host_wm,filter);
figure(3), imshow(avg_wm,[]);

water_ex_from_ave = ones(row,col);
for i = 1:row
    for j = 1:col
            % convert to its 8 bit binary
            temp_bi = dec2bin(double(avg_wm(i,j)),8);
            
            % extract from Bit position
            pos = temp_bi(8-place);
            water_ex_from_ave(i,j) = bin2dec(pos);   
    end
end
figure(4), imshow(water_ex_from_ave,[]);

end

