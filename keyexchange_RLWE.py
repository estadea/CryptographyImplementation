import numpy as np
import sys
from numpy.polynomial import polynomial as p


n = 10
q = 2**n - 1

# (x^n + 1) for polynomial divison
N = [1] + [0] * (n-1) + [1] 


# generate polynomial
def generate_polynomial(n,q):
    polynomial = np.floor(np.random.normal(size=(n)))
    while (len(polynomial) != n):
        polynomial = np.floor(np.random.normal(l,size=(n)))
        polynomial = np.floor(p.polydiv(poly,N)[1]%q)
    return polynomial



#Generate A
A = np.floor(np.random.random(size=(n))*q)%q
A = np.floor(p.polydiv(A,N)[1])

#Alice
sA = generate_polynomial(n,q)
eA = generate_polynomial(n,q)

bA = p.polymul(A,sA)%q
bA = np.floor(p.polydiv(sA,N)[1])
bA = p.polyadd(bA,eA)%q


#Bob
sB = generate_polynomial(n,q)
eB = generate_polynomial(n,q)


bB = p.polymul(A,sB)%q
bB = np.floor(p.polydiv(sB,N)[1])
bB = p.polyadd(bB,eB)%q



# Shared Values
sharedAlice = np.floor(p.polymul(sA,bB)%q)
sharedAlice = np.floor(p.polydiv(sharedAlice,N)[1])%q
sharedBob = np.floor(p.polymul(sB,bA)%q)
sharedBob = np.floor(p.polydiv(sharedBob,N)[1])%q




u = np.asarray([0] * n)
i = 0
while (i < len(u)):
	if (len(bB) <= i): break;
	if ( int( bB[i] / (q/4) ) == 0 ): u[i] = 0
	elif (int(bB[i]/(q/2)) == 0): u[i] = 1
	elif (int(bB[i]/(3*q/4)) == 0): u[i] = 0
	elif (int(bB[i]/(q)) == 0): u[i] = 1
	else:
		print("error! (1)")
	i+=1

	
# Alice shared key
i = 0
while (i < len(u)):
	if (u[i] == 0):
		if (sharedAlice[i] >= (q/2) and sharedAlice[i] < ((3*q)/4) ):
			sharedAlice[i] = 0
		else:
			sharedAlice[i] = 1
	elif (u[i] == 1):
		if (sharedAlice[i] >= (q/4) and sharedAlice[i] < (q/2)):
			sharedAlice[i] = 1
		else:
			sharedAlice[i] = 0
	else:
		print("error in alice shared key generation")
	i += 1


# Bob shared key
i = 0
while (i < len(u)):
	if (u[i] == 0):
		if (sharedBob[i] >= (q/2) and sharedBob[i] < ((3*q)/4) ):
			sharedBob[i] = 0
		else:
			sharedBob[i] = 1
	elif (u[i] == 1):
		if (sharedBob[i] >= (q/4) and sharedBob[i] < (q/2)):
			sharedBob[i] = 1
		else:
			sharedBob[i] = 0
	else:
		print("error in bob shared key generation")

	i += 1	


print("\n")
print("Shared Key Alice: ")
print(sharedAlice)
print("Shared Key Bob  : ")
print(sharedBob)


i = 0
while (i < n):
	if (sharedAlice[i] != sharedBob[i]):
		print("Error at index",i)
	i+=1
