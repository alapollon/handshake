
try: 
    import socketserver as ss 
except ImportError: 
     
import asyncio as sync
import time as T

import socket
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
get_log = log.getLogger('com.heustricreasoning.app %()s')
ip6 = has_ipv6
word = htonl
dword = htons
oust = getdefaulttimeout

set_of_expectations = (
    #combine the possibility of socket errors here
    # if a defaulttimeout of return occur, return it's error here 
    "err" 
)

class HandServer(ForkingUDPServer):
    pass

async def get_hostname_by_ip(link):
    await host = socket.gethostbyaddr(link)
    return host

async def get_host_services (porto, protocoltypeb):
    await service = socket.getservbyport(porto, protocoltypeb)
    if service is err 
    return service 

async def get_localhost_netlink():
    await localpid 


async def link(self): 
    self 
    