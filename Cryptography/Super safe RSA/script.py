n=16761353604213888115960721166197232103540704147880530125204843959378923595238269
from math import *
from gmpy2 import *
z=int(sqrt(n))
while(1>0):
	q=next_prime(z)
	print(q)
	if(n%q==0):
		print(q)
		print("yes")
		break
	z=q