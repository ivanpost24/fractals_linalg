import numpy as np
import matplotlib.pyplot as plt

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle 
from collections import deque
from dataclasses import dataclass
from matplotlib.transforms import Affine2D
from matplotlib.patches import Polygon

#This function performs an affine transformation on a polygon
def transform_polygon(transform: Affine2D, poly: Polygon) -> Polygon:
    return Polygon(transform.transform(poly.get_verts()))

#Creates a unit square as the starting square
def unit_square() -> Polygon:
    return Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])

#This will be used later
MIN_LEG = 0.01


def main() -> None:
    #Declaring all variables
    alpha = 30
    alpha_rad = np.radians(alpha)
    cos_alph = np.cos(alpha_rad)
    sin_alph = np.sin(alpha_rad)
    
    #The affine transformations that both rotate and scale the square 
    counter_clockwise_transform = Affine2D.from_values(cos_alph**2, cos_alph*sin_alph, -cos_alph*sin_alph, cos_alph**2, 0, 1)

    clock_wise_transform= Affine2D.from_values(sin_alph**2, -cos_alph*sin_alph, cos_alph*sin_alph, sin_alph**2, cos_alph **2, 1 + cos_alph*sin_alph)

    #Creating a pythagorus tree 
    tbprocessed = deque([unit_square()]) #Making a double ended queue for squares
    
    #Setting the basics of the plot including the limits of the axes
    fig, axe = plt.subplots()
    axe.set_xlim(-5, 5)
    axe.set_ylim(0, 5)
    axe.set_aspect("equal") #Ensures the picture isn't warped or stretched weirdly


    while tbprocessed: 
        rect = tbprocessed.pop() #Removes one item from the end of the double ended queue

        #The rectangles transformed
        cctrans = transform_polygon(counter_clockwise_transform, rect)
        cwtrans = transform_polygon(clock_wise_transform, rect)

        #Checks that the width and height of the square is less than 0.01 to ensure the code doesn't run forever
        if MIN_LEG < cctrans.get_tightbbox().width and MIN_LEG < cctrans.get_tightbbox().height:
            #Appends a new vector with its starting point to the double ended queue
            tbprocessed.appendleft(cctrans)

        if MIN_LEG < cwtrans.get_tightbbox().width and MIN_LEG < cwtrans.get_tightbbox().height:
            tbprocessed.appendleft(cwtrans)
        
        #Creatinga new rectangle
        axe.add_patch(rect)

    plt.show()

if __name__ == '__main__':
    main()
