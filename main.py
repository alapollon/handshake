from cv2 import goodFeaturesToTrack
from collections import namedtuple
import mimetypes, argparse, queue
import torch



def main():
    hosts=[None]
    while True:
        from server import start 
        for ip in hosts:
            start(ip)
            

    pass 