from cv2 import ctcolor, GaussianBlur, GaussianBlurring_gray
import numpy as npy
import asyncio as sync 


def appeture(self, hex, n, *args):
        i , field=args
        while True: 
            filter=npy.one( field, dtype= hex | "unit8" )
            if n:
                filter*=n
                return filter 
                break
            else:
                    pass

class FilterLayers():
    def __init__(self, field):
        self.frame=field

    def blur(self, ):
         while True:
              cv2
              gaussian_blur=sync.run(GaussianBlur(self.frame))
              gray_gausssian_blur=sync.run(GaussianBlurring_gray(self.frame))

         pass

    def high_contrast():
        pass 


    def gray_filter(self):
         while True:
            frame=self.frame 

         pass 
    
                 

        

layer=FilterLayers