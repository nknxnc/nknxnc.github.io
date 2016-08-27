#!/usr/bin/python3
from binascii import unhexlify, hexlify
import hashlib
from ecdsa.keys import der
from ecdsa.curves import find_curve
from ecdsa.numbertheory import inverse_mod
from ecdsa.util import sigencode_string, sigdecode_string

def sign(hash, random_k, pk, G):
    n = G.order()
    k = random_k % n
    p1 = k * G
    r = p1.x()
    if r == 0:
        raise RuntimeError("amazingly unlucky random number r")
    s = (inverse_mod(k, n) *
       (hash + (pk * r) % n)) % n
    if s == 0:
        raise RuntimeError("amazingly unlucky random number s")
    return r, s    

def get_G(public_key):
    str1, empty = der.remove_sequence(der.unpem(PUBLIC_KEY.strip()))
    str2, point_str_bitstring = der.remove_sequence(str1)
    oid_pk, rest = der.remove_object(str2)
    oid_curve, empty = der.remove_object(rest)
    curve = find_curve(oid_curve)
    return curve.generator
    
def get_k(s1,s2,hash1,hash2):
    n = G.order();
    k_i = ((hash1 - hash2) * inverse_mod((s1 - s2), n))%n
    return k_i
    
def get_privkey(k,s1,hash1,r): 
    n = G.order()
    key = ((k * s1 - hash1) * inverse_mod(r, n))%n
    return key
    
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEgTxPtDMGS8oOT3h6fLvYyUGq/BWeKiCB
sQPyD0+2vybIT/Xdl6hOqQd74zr4U2dkj+2q6+vwQ4DCB1X7HsFZ5JczfkO7HCdY
I7sGDvd9eUias/xPdSIL3gMbs26b0Ww0
-----END PUBLIC KEY-----
"""
G = get_G(PUBLIC_KEY)

hash1 = int(hashlib.sha256('time').hexdigest(),16)
hash2 = int(hashlib.sha256('help').hexdigest(),16)
hash3 = int(hashlib.sha256('read flag.txt').hexdigest(),16)
sig1 ="c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156c0cbebcec222f83dc9dd5b0d4d8e698a08ddecb79e6c3b35fc2caaa4543d58a45603639647364983301565728b504015d"
sig2 ="c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156cfd7287caf75247c9a32e52ab8260e7ff1e46e55594aea88731bee163035f9ee31f2c2965ac7b2cdfca6100d10ba23826"
r1,s1 =  sigdecode_string(unhexlify(sig1), G.order())
r2,s2 =  sigdecode_string(unhexlify(sig2), G.order())

k = get_k(s1, s2, hash1, hash2, G)
private_key = get_privkey(k, s1, hash1, r1, G)
r3, s3 =  sign(hash3, k, private_key, G)

print 'read flag.txt:' + hexlify(sigencode_string(r3, s3, G.order()))
