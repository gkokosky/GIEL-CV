import matplotlib.pyplot as click
import matplotlib.image as np

file = 'sexygiel.jpg'
logo = np.imread(file)

click.imshow(logo)
click.show()