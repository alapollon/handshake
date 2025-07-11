
import asynchat, coroutines, logging, socketserver 

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


