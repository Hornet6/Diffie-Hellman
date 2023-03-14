#Double Ratchet Algorithm
import hashlib
import nacl
import base64
from Crypto.Cipher import AES
# assumes knowlege of shared key (from diffHell)
sharedKey=89005330586580187460447797262694947558585802190639423605895969138137604727030363533383102327238888063774652063166868052487205726446858692415663309318944713324209073763121067320962543994427197072891573532085233436592698772764104874000444566811890847095969397737937311703687348229853815083445001173331555921481

sharedKey = sharedKey.to_bytes(1024,'big')
# https://nfil.dev/coding/encryption/python/double-ratchet-example/

msg=b"This is a test message to be encrypted!"
import hmac

# x = hmac.new(sharedKey)
# h = hmac.digest(sharedKey,msg)
# print(h)
class Ratchet():
    def __init__(self,key):
        self.key = key
    def next(self, change):

        new_key = hashlib.sha256(self.key + change).digest()
        self.key = new_key
        return new_key

# x = Ratchet(sharedKey)
# print(x.next(b''))
# print(x.next(b''))
# y = Ratchet(sharedKey)
# print(y.next(b''))
# print(y.next(b''))

def pad(msg):
    num = 16 - (len(msg) % 16)
    return msg + bytes([num] * num)
def depad(msg):
    return msg[:-msg[-1]]
from diffHell import DiffHell
class dh_ratchet():
    def __init__(self,local_private,local_public,forign_public):
        self.dh = DiffHell(local_private,local_public)
        self.local_priv_key = local_private
        self.local_pub_key = local_public
        self.forign_pub_key = forign_public
        self.shared_key = self.dh.calculate_shared_key(forign_public)
        self.create_ratchets()
    def create_ratchets(self):  
        self.root_ratchet = Ratchet(sharedKey)
        if self.local_pub_key < self.forign_pub_key:
            self.send_ratchet = Ratchet(self.root_ratchet.next(b''))
            self.recv_ratchet = Ratchet(self.root_ratchet.next(b''))
        elif self.local_pub_key > self.forign_pub_key:
            self.recv_ratchet = Ratchet(self.root_ratchet.next(b''))
            self.send_ratchet = Ratchet(self.root_ratchet.next(b''))
        else:
            print("Matching key error")
    def show(self):
        print("Send key:",self.send_ratchet.key)
        print("Recv key:",self.recv_ratchet.key)
        print("Shared key:",self.shared_key)
    def send(self,msg):
        self.send_ratchet.next(b'')
        key = self.send_ratchet.key
        ciphertxt = AES.new(key, AES.MODE_CBC,iv=b'1234567890123456').encrypt(pad(msg))
        return ciphertxt
    def recv(self,ciphertxt):
        self.recv_ratchet.next(b'')
        key = self.recv_ratchet.key
        data = AES.new(key, AES.MODE_CBC,iv=b'1234567890123456').decrypt(ciphertxt)
        data = depad(data)
        return data

A = DiffHell()
B = DiffHell()


A_ratchet = dh_ratchet(A.get_private_key(),A.get_public_key(),B.get_public_key())

B_ratchet = dh_ratchet(B.get_private_key(),B.get_public_key(),A.get_public_key())

# print("A:")
# A_ratchet.show()
# print("B:")
# B_ratchet.show()
# print(msg)

c = A_ratchet.send(msg)
# print(c)
o = B_ratchet.recv(c)
print(o)
print(o == msg)
