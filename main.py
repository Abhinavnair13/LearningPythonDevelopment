import cv2

source = "Profile pic.jpeg"
src= cv2.imread(source)
scale_percent = int(input("Enter the scale percent by which you want to rescale (%) "))
type(src.shape)
new_width = int(src.shape[1]*scale_percent/100)
new_height = int(src.shape[0]*scale_percent/100)
output = cv2.resize(src,(new_width,new_height))
cv2.imwrite("new image.jpg",output)
cv2.waitKey(0)
