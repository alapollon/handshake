
import logging as log
import socketserver as ss 
import asyncio as sync
import time as T
from socket import (
    BaseRequestHandler, 
    StreamRequestHandler, 
    ForkingUDPServer, 
    ForkingTCPServer,
) 

log.basicConfig(
    level=loggging.DEBUG, 
    format='%(levelname)s:%(name)s: %(message)s',
    stream= sys.stderr,
    filename="heustricapp.log" 
)

brh= BaseRequestHandler; 
srh= StreamRequestHandler; 
frk_tcp_server= ForkingTCPServer
frk_udp_server= ForkingUDPServer
_log_get= log.getLogger('com.heustricreasoning.app %()s')
ifipv6= has_ipv6
word= htonl
dword= htons
oust= getdefaulttimeout

set_of_expectations= (
    #combine the possibility of socket errors here
    # if a defaulttimeout of return occur, return it's error here 
    "err" 
)
def timeservice()
        pass

 def _tcp_handlr():
    while :
        pass 
 def _https_server():
    while :
        pass



class HandServer(frk_udp_server, frk_tcp_server):
    def __init_(self, local_host_addr: str|None, local_port_addr: int|):
        self.locality=(local_host_addr, local_port_addr)
        self.timedate=
        pass
   def handlr(): 
    pass 