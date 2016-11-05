#just some testing stuff
import numpy
from PIL import Image
from mayavi import mlab
from scipy import misc

#cube = misc.imread('../images/left1.JPG')
#misc.imsave('test.png', cube)
#type(cube)
#cube.shape, cube.dtype

from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage.transform import warp, AffineTransform
cube = Image.open("../images/left1.JPG").convert("L")
#img = misc.imread('left1.JPG')
imgarr = numpy.array(cube)

mlab.imshow(imgarr)
print(imgarr)

tform = AffineTransform(scale=(1.3, 1.1), rotation=1, shear=0.7, translation=(210, 50))
image = warp(cube, tform.inverse, output_shape=(350, 350))

coords = corner_peaks(corner_harris(image), min_distance=5)
coords_subpix = corner_subpix(image, coords, window_size=13)

mlab.imshow(coords_subpix)
