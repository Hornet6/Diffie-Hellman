from Double_Ratchet_Algorithm import dh_ratchet

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

print("=====================================")
print("=====================================")
print("=====================================")
# Testing with multiple messages from A to B

messagesToSend = ["This is a test message 1!","abcdefghijklmnopqrstuvwxyz","This is a test message 3!","This is a test message 4!","abcdefghic"]
encryptedMessages= []


X_ratchet = dh_ratchet()
Y_ratchet = dh_ratchet()

X_pubKey = X_ratchet.get_public_key()
Y_pubKey = Y_ratchet.get_public_key()

# send pub keys

X_ratchet.update_forign_key(Y_pubKey)
Y_ratchet.update_forign_key(X_pubKey)
for i in messagesToSend:
    print(i)
    encryptedMessages.append(X_ratchet.send(i))

print()
print()
# print(encryptedMessages)
# send messages to send
# print(encryptedMessages[0]["key"])
# encryptedMessages[0]["key"] += 4
# print(encryptedMessages[0]["key"])
for i in encryptedMessages:
    x = Y_ratchet.recv(i)
    print(x)