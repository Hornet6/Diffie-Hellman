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
        self.key = str(key).encode()
    def next(self):
        new_key = hashlib.sha256(self.key).digest()
        self.key = new_key
        return new_key

def pad(msg):
    num = 16 - (len(msg) % 16)
    return msg + bytes([num] * num)
def depad(msg):
    return msg[:-msg[-1]]
from diffHell import DiffHell
class dh_ratchet():
    def __init__(self):
        self.dh = DiffHell()
        self.local_priv_key = self.dh.get_private_key()
        self.local_pub_key = self.dh.get_public_key()
    def create_ratchets(self):  
        # print(self.shared_key)
        self.root_ratchet = Ratchet(self.shared_key)
        if self.local_pub_key < self.forign_pub_key:
            self.send_ratchet = Ratchet(self.root_ratchet.next())
            self.recv_ratchet = Ratchet(self.root_ratchet.next())
        elif self.local_pub_key > self.forign_pub_key:
            self.recv_ratchet = Ratchet(self.root_ratchet.next())
            self.send_ratchet = Ratchet(self.root_ratchet.next())
        else:
            print("Matching key error")
            self.show()
    def show(self):
        print("Local Pub key:",self.local_pub_key)
        print("Forign Pub key:", self.forign_pub_key)
        print("Send key:",self.send_ratchet.key)
        print("Recv key:",self.recv_ratchet.key)
        print("Shared key:",self.shared_key)
    def send(self,msg):
        byteMsg = str.encode(msg)
        self.update_local_keys()
        self.send_ratchet.next()
        key = self.send_ratchet.key
        ciphertxt = AES.new(key, AES.MODE_CBC,iv=b'1234567890123456').encrypt(pad(byteMsg))
        return {"ciphertxt":ciphertxt,"key":self.get_public_key()}
    def recv(self,msg):
        forign_public = msg["key"]
        ciphertxt = msg["ciphertxt"]
        self.update_forign_key(forign_public)
        self.recv_ratchet.next()
        key = self.recv_ratchet.key
        byteData = AES.new(key, AES.MODE_CBC,iv=b'1234567892123456').decrypt(ciphertxt)
        byteData = depad(byteData)
        data = byteData.decode()
        return data
    def update_local_keys(self):
        self.dh = DiffHell()
        self.local_priv_key = self.dh.get_private_key()
        self.local_pub_key = self.dh.get_public_key()
        self.shared_key = self.dh.calculate_shared_key(self.forign_pub_key)
        self.create_ratchets()
    def update_forign_key(self,forign_public):
        self.forign_pub_key = forign_public
        self.shared_key = self.dh.calculate_shared_key(forign_public)
        self.create_ratchets()
    def get_public_key(self):
        return self.dh.get_public_key()
    # this might be unnecessary
    def get_private_key(self):
        return self.dh.get_public_key()

# rootRatchet = Ratchet(53185350083465880337277094726544417046403934236491268741464018409430564952049516567183021652243668020573645457407762475398739831342735623538588156679325862993602673324296176122430735148946455069036220377955986823078367436270389081982120794227842437893561908801640322213081980343575223985855680670575815914109 )
# rootRatchet2 = Ratchet(53185350083465880337277094726544417046403934236491268741464018409430564952049516567183021652243668020573645457407762475398739831342735623538588156679325862993602673324296176122430735148946455069036220377955986823078367436270389081982120794227842437893561908801640322213081980343575223985855680670575815914109 )

# for i in range(3):
#     sendRatchet = Ratchet(rootRatchet.next())
#     print(sendRatchet.next())
# for i in range(3):
#     sendRatchet = Ratchet(rootRatchet2.next())
#     print(sendRatchet.next())

s = dh_ratchet()
r = dh_ratchet()

s_pubKey = s.get_public_key()
r_pubKey = r.get_public_key()

s.update_forign_key(r_pubKey)
r.update_forign_key(s_pubKey)

m="A LONG test message that hopefully wont break at index 9"
c = s.send(m)
o = r.recv(c)
print(o)
print(o==m)
for i in range(len(o)):
    if o[i]!= m[i]:
        print(i)



# A_ratchet = dh_ratchet()

# B_ratchet = dh_ratchet()

# A_pubKey = A_ratchet.get_public_key()
# B_pubKey = B_ratchet.get_public_key()

# # send pub keys

# A_ratchet.update_forign_key(B_pubKey)
# B_ratchet.update_forign_key(A_pubKey)

# # A needs to send :
# # new public key
# # MAC
# # the encrypted message



# cypherText = A_ratchet.send(msg)
# mac = ""
# newPublicKey = A_ratchet.get_public_key()
# # On reciving a message:
# # 
# o = B_ratchet.recv(newPublicKey,cypherText)

# print(o)
# print(o == msg)

# print("=====================================")
# print("=====================================")
# print("=====================================")
# # Testing with multiple messages from A to B

# messagesToSend = ["This is a test message 1!","This is a test message 2!","This is a test message 3!","This is a test message 4!"]
# encryptedMessages= []


# X_ratchet = dh_ratchet()
# Y_ratchet = dh_ratchet()

# X_pubKey = X_ratchet.get_public_key()
# Y_pubKey = Y_ratchet.get_public_key()

# # send pub keys

# X_ratchet.update_forign_key(Y_pubKey)
# Y_ratchet.update_forign_key(X_pubKey)
# for i in messagesToSend:
#     print(i)
#     m=X_ratchet.send(msg)
#     encryptedMessages.append([X_ratchet.get_public_key(),"",m])
# # print(encryptedMessages)
# # send messages to send

# for i in encryptedMessages:
#     x = Y_ratchet.recv(i[0],i[2])
#     print(x)