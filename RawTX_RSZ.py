import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff08046ad8001d020819ffffffff0100f2052a010000004341046546f632c8e3800920d6d3756dc14537f277214e51c3f604defd116d9527d54fc25a9bcb74cc854db2befa256d331c89f4fe7a2913d953480d3818b3a86c65c4ac00000000"

m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)


