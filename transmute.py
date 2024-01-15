import secrets
import hashlib

t = secrets.token_hex(8)

def transmute(t):
    b = t.encode()
    
    h2 = hashlib.new('sha512_256', b).hexdigest()
    h3 = hashlib.sha3_256(b).hexdigest()
    
    b23 = (h2 + h3).encode()
    b32 = (h3 + h2).encode()
    
    h223 = hashlib.new('sha512_256', b23).hexdigest()
    h232 = hashlib.new('sha512_256', b32).hexdigest()
    h323 = hashlib.sha3_256(b23).hexdigest()
    h332 = hashlib.sha3_256(b32).hexdigest()
    
    u = h223[32:36] + h232[32:36] + h323[32:36] + h332[32:36]
    
    return u

u = transmute(t)
v = transmute(u)

print(t)
print(u)
print(v)
