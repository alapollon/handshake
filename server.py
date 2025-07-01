import coroutines
import socketserver
import asyncio as sync
import socket  
import time 
import logging as log

log.basicConfig(
    level=loggging.DEBUG, 
    format='%(levelname)s:%(name)s: %(message)s',
    stream= sys.stderr,
    filename="heustricapp.log" 
)

base= BaseRequestHandler; 
stream= StreamRequestHandler; 
get_log = log.getLogger() 

ip6 = has_ipv6
word = htonl
dword = htons

def start_daemon():
    
    pass 