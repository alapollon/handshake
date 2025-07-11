

from cv2 import CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, calcOpticalFlowPyrLK, imread,  VideoCapture
from cv2 import Canny, calcOpticalFlowPyrLK, goodFeaturesToTrack, Laplacian, VideoCapture
from inference import PlaneInference as pid
from numpy import one, array
from collections import ChainMap
import asyncio, functools, pathlib, os


class framework(): 
    def __init__(self, training: boolean, path, n_frames):
        self.fit=training
        self.count=n_frames
        self.stored_sample_names=sorted(set(media.name for media in self.path.iterdir() if p.is_dir()))
        self.paths_identity_for_sample= dict((name, idx) for idx, name in enumerate(self.stored_sample_names))
        self.w=[None]
        pass

    def get_file_and_sample_name(self):
        media_paths=list(self.path.glob( '*/*.mp4'| '*/*.avi'))
        samples=[ sample.parent.name for sample in media_paths ]
        return media_paths, samples 
    

    def __call__(self):
        media_paths, samples= self.get_file_and_sample_name()
        while True:
            presets=list(zip(media_paths, samples))
            try: 
                if self.training:
                    random.shuffle(presets)

                for media_path, samples in presets:
                    media=frames_from_media_file(path, self.n_frames) 
                    preset_label=self.stored_sample_names[name]
                    yield media,label 
                    pass 
            except: 
                    pass 


