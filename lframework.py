try:
  import cv2 as V2
except ModuleNotFoundError:
  !pip install opencv-python
  import cv2 as V2

class Lframework():
  def __init__(self, path):
    self.count = V2.CAP_PROP_FRAME_COUNT or 0
    self.w = asarray([]);


  #todo check journal entry 0031
  async def cap_stream_data(self):
    if path is not None:
      run(self.w([ lambda path: V2.VideoCapture.set(self.count, path) & Discrete(V2.VideoCapture.read(path)[1])
       for i in range(self.count)]))
      for i in enumerate(self.w)
            yield i
