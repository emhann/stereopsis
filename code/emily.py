#just some testing stuff
import numpy
from PIL import Image
from mayavi import mlab
from scipy import misc
import cv2
import numpy as np

#cube = misc.imread('../images/left1.JPG')
#misc.imsave('test.png', cube)
#type(cube)
#cube.shape, cube.dtype

#from skimage.feature import corner_harris, corner_subpix, corner_peaks
#from skimage.transform import warp, AffineTransform
#cube = Image.open("../images/left1.JPG").convert("L")
#img = misc.imread('left1.JPG')
#imgarr = numpy.array(cube)

#mlab.imshow(imgarr)
#print(imgarr)

#tform = AffineTransform(scale=(1.3, 1.1), rotation=1, shear=0.7, translation=(210, 50))
#image = warp(cube, tform.inverse, output_shape=(1200, 800))

#coords = corner_peaks(corner_harris(image), min_distance=10)
#coords_subpix = corner_subpix(image, coords, window_size=20)

#mlab.imshow(coords_subpix)
#print(coords_subpix)
filename = '../images/left1.JPG'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.imwrite('subpixel5.png',img)
