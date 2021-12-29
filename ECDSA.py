
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.signature import Signature

#generation key
privateKey = PrivateKey()
print(privateKey.curve.name)
print('priv_key=', privateKey.secret)
print('\n')

publicKey = privateKey.publicKey()
print('public key:')
print('x=', publicKey.point.x)
print('y=', publicKey.point.y)
print('\n')

message = "New message on ecdsa"
signature = Ecdsa.sign(message, privateKey)

print(signature)
print('r=', signature.r)
print('s=', signature.s)
print('\n')

result=Ecdsa.verify(message, signature, publicKey)
print('result', result)

result=Ecdsa.verify("Hello",signature,publicKey)
print('mal_res=', result)
