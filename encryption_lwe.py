import sys
import numpy
import random
import math

cardset=10

B=[]
e=[]
s = input("Enter a secret value: ")
M = input("Enter a Message to encrypt (0-8): ")
q = input("Enter a prime number that is greater or equal to 53: ")

def bits(val):
	l = [0]*(8)

	l[0]=val & 0x1
	l[1]=(val & 0x2)>>1
	l[2]=(val & 0x4)>>2
	l[3]=(val & 0x8)>>3
	return l

def encrypt(A,B,M,q):
	u=0
	v=0
	sample= random.sample(range(cardset-1), cardset//4)
	print(sample)
	for x in range(0,len(sample)):
		u=u+(A[sample[x]])

		v= v+B[sample[x]]


	v=v+math.floor(q//2)*M
	return u%q,v%q

	
def decrypt(u,v,q):
	res=(v-s*u) % q


	if (res>q//2):
		return 1

	return 0

A = random.sample(range(q), cardset)

for x in range(0,len(A)):
	e.append(random.randint(1,4))
	B.append((A[x]*s+e[x])%q)

bit = bits(M)

u1,v1=encrypt(A,B,bit[0],q)
u2,v2=encrypt(A,B,bit[1],q)
u3,v3=encrypt(A,B,bit[2],q)
u4,v4=encrypt(A,B,bit[3],q)


print("Message:",M)
print("Public Key A:",A)
print("Public Key B:",B)
print("Errors e:",e)
print("Secret key s:",s)
print("Prime number q:",q)

print("\nCalculation of u and v")
print("u1,v1:",u1,v1)
print("u2,v2:",u2,v2)
print("u3,v3:",u3,v3)
print("u4,v4:",u4,v4)

print("\nDecryption\nMessage was: ")
print(decrypt(u4,v4,q),decrypt(u3,v3,q),decrypt(u2,v2,q),decrypt(u1,v1,q))


