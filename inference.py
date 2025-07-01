from cv2 import Canny, goodFeaturesToTrack
from collections import namedtuple
from queue import Queue

def calculate_canny_edges(): 
    pass


class PlaneInference():
   def __init__(self, data_name, ):
    self.category=namedtuple(data_name, ['edge', 'shapes', 'histogram','distance', 'limits', 'limits_count'])
    
    def kernel(*args):
        from scipy import sparse
        appetature, filter, frame=args 
        resolution=None 
        corners=goodFeaturesToTrack
        matrix=one(frame, dtype="unit8")
        while True: 
           pass 
        #todo in thought process  
        if None:
            sparse_matrix=sparse.csr_matrix(matrix)
        pass 



