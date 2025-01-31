import cv2 as cv 
import matplotlib.pyplot as plt 

import numpy as np
import sys

def rect(index):
	def box(x, y):
		return index[x][y] and index[x-1][y-1] and index[x-1][y] \
		and index[x][y-1] and index[x][y+1] and index[x+1][y-1] and index[x+1][y] and index[x+1][y+1]
		
	row, col = index.shape 
	lr = [row, col]
	bx = [0, 0]
	
	for x in range(1, row-1):
		for y in range(1, col-1):
			if box(x, y):
				if x < lr[0]:
					lr[0] = x 
				if y < lr[1]:
					lr[1] = y 
				if x > bx[0]:
					bx[0] = x 
				if y > bx[1]:
					bx [1] = y 
	return lr, bx 
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: python extract.py srcImg, dstImg")
		exit(-1)
	
	srcpath = sys.argv[1]
	dstpath = sys.argv[2]
	
	srcImage = cv.imread(srcpath)
	if srcImage == np.array([]):
		print(" no file "+srcImg)
		exit(-1)
	
	#cv.imshow("src", srcImage)

	hsv = cv.cvtColor(srcImage, cv.COLOR_BGR2HSV)


	th = cv.inRange(hsv, (0, 90, 90), (150, 220, 220))



	index = th==255

	lr, bx = rect(index)

	dstImage = np.zeros((bx[0]-lr[0]+1, bx[1]-lr[1]+1, 3), np.uint8)
	for x in range(lr[0], bx[0]):
		for y in range(lr[1], bx[1]):
			dstImage[x-lr[0]][y-lr[1]] = srcImage[x][y]

#dstImage[:, :] = (255,255,255)

#dstImage[index] = srcImage[index]

# cv.imshow("dst", dstImage)

#print(dstImage.shape)

	cv.imwrite(dstpath, dstImage)

#cv.waitKey(0)

	plt.imshow(dstImage)
	plt.show()

