

from cv2 import CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, calcOpticalFlowPyrLK, imread,  VideoCapture
from cv2 import Canny, calcOpticalFlowPyrLK, goodFeaturesToTrack, Laplacian, VideoCapture
from inference import PlaneInference as pid
from numpy import one, array
from collections import ChainMap
import asyncio, functools, pathlib, os 

def symbol(path):
    get=os.path
    if get.filepath(path):
        onpath=path
        return onpath
    elif get.isdir(path):
        items=os.listdir(path)
        return items 

def width(data):
    frame_width=int(cap.get(CAP_PROP_FRAME_WIDTH))
    return frame_width

def height(data):
    frame_height=int(cap.get(CAP_PROP_FRAME_HEIGHT))
    return frame_height


class Discrete(object):
  def __init__(self, frame, *args):
    self.inference=object
     
  def compose(self, data):
    frame_width=width(data)
    frame_height=height(data)
    pass 
     

class Lframework(): 
    def __init__(self):
        self.count=None
        self.w=[None]
        pass

    def process(self, path):
        while True:
            s=symbol(path)
            try: 
                if s :
                    cap=imread
                    try:
                        pass
                    except :  
                        pass

                elif s:
                    cap=VideoCapture.read
                    fps=cap.get()
                    self.w[(lambda path:self.count+=cap.get()) i for i in cap(path)[1]]

            except: 
                    pass 
                
