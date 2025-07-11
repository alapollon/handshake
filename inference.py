from cv2 import Canny, goodFeaturesToTrack
from collections import namedtuple
from queue import Queue
from numpy import array, zeros
import filters 
import tensorflow as tf
import lframework

refractions= tf.keras.Sequential([
    
]) 

enclosures= tf.keras.Sequential([

])


class PlaneInferenceData():
   def __init__(self, ds_name, ):
        self.category=namedtuple(ds_name, ['edge', 'shapes', 'histogram','distance', 'limits_count'])
        pass 
    
    def kernel(dimensions: set=(None, None, None, 3), args):
        path, parts, shuffle =args
        try: 
            output_signature=(tf.TensorSpec(shape = dimensions, dtype=tf.float32), tf.TensorSpec(shape=dimensions, dtype=tf.int16))
            ds=tf.data.Dataset.from_generator(lframework.Framework(path, parts, shuffle), output_signature=output_signature)
        except :
            pass 
            
        
        



