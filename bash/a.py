from ctypes import *

global EcdhPriKey, EcdhPubKey
loader = cdll.LoadLibrary
lib = loader("./microchat/dll/libecdh_x64.so")
priKey = bytes(bytearray(2048))
pubKey = bytes(bytearray(2048))
lenPri = c_int(0)
lenPub = c_int(0)
pri = c_char_p(priKey)
pub = c_char_p(pubKey)
pLenPri = pointer(lenPri)
pLenPub = pointer(lenPub)
nid = 713
bRet = lib.GenEcdh(nid, pri, pLenPri, pub, pLenPub)
if bRet:
    EcdhPriKey = priKey[:lenPri.value]
    EcdhPubKey = pubKey[:lenPub.value]
else:
    print('error')

