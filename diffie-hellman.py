import sys
import random
import math
from Crypto.Util import number

p = number.getPrime(9,None)   #generating 9 bits prime
g = random.randint(5,200)
x = random.randint(0,p-1)
y = random.randint(0,p-1)

aliceKey = pow(g,x,p)
bobKey = pow(g,y,p)

print "g : " +str(g)
print "p : " +str(p)
print "Alice's public key: " +str(aliceKey)
print "Bob's public key : " +str(bobKey)

alicePriv = pow(bobKey,x,p)
bobPriv = pow(aliceKey,y,p)

if bobPriv != alicePriv:
	print "Woah! Something is terribly wrong."
else:
	print "Alice's and Bob's shared secret: " +str(alicePriv)

print "\n---Brute force---"  #Now we'll find a shared secret with brute-force

for X in range(0,p-1):
	alicePublic = pow(g,X,p)
       	if alicePublic == aliceKey:
               	break

secret = pow(bobKey,X,p)
print "\nFound! Alice's and Bob's shared secret: " +str(secret)
