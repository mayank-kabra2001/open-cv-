import cv2

#to load image an img
#-1 = to load a colored image 
#0 = to load bw image 
img = cv2.imread('lena.jpg', 1)

# to show image
cv2.imshow('image', img)

#waitkey(amount of seconds after which window is closed)... so 0 means never closed.
k = cv2.waitKey(0) & 0xFF

#if esc is pressed closed if s then save
if k == 27:
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()