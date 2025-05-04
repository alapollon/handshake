
try: 
    import socketserver as ss 
except ImportError: 
     
import asyncio as sync
import time as T
from ss import BaseRequestHandler, 
                StreamRequestHandler, 
                ForkingUDPServer, 
                ForkingTCPServer,
import logging as log

log.basicConfig(
    level=loggging.DEBUG, 
    format='%(levelname)s:%(name)s: %(message)s',
    stream= sys.stderr,
    filename="heustricapp.log" 
)

appserv_addr = ('localhost', 7000)
eventual = asyncio.get_event_loop
base = BaseRequestHandler; 
stream = StreamRequestHandler; 
fork_tcp_server = ForkingTCPServer
fork_udp_server = ForkingUDPServer
get_log = log.getLogger('com.heustric_reasoning.app %()s')


def __init__(self):
   self.origins = {}

async def link(self): 
    self 
    