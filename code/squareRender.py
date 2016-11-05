import numpy
from PIL import Image
from mayavi import mlab
from scipy import misc


""" Use imshow to visualize a 2D 10x10 random array.
"""
img = Image.open("../images/left1.JPG").convert("L")
#img = misc.imread('left1.JPG')
imgarr = numpy.array(img) 

mlab.imshow(imgarr)

from skimage import data, io, filters

image =imgarr
# ... or any other NumPy array!
edges = filters.sobel(image)
io.imshow(edges)
io.show()