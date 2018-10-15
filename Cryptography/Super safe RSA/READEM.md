Peoblem Statement:

Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with nc 2018shell2.picoctf.com 3609.

Solution :
i got the following data :
	
	c: 19474669958697898483768380499982060217038494985407624948963596074034125281014421
	n: 25132405989001317956087767778734083918050854186063214627718037281542891163684097
	e: 65537

Problem Statement(425 points):

Wow, he made the exponent really large so the encryption MUST be safe, right?! Connect with nc 2018shell2.picoctf.com 29661.

Solutions:

I tried all attacks but can't get any result.So in the i used https://www.alpertron.com.ar/ECM.HTM and cracked the factor of n.

After 12 min 55 sec i got the facors :

	158 754754 453572 149934 540516 805858 365529 (39 digits) × 158309 627169 945915 479670 296299 307350 953193 (42 digits)

So we got our p and q

	p=158754754453572149934540516805858365529
	q=158309627169945915479670296299307350953193 
	t=(p-1)*(q-1)
	import gmpy2
	d = gmpy2.invert(e,t)

	# Decryption
	decimalmessage = pow(c,d,n)
	print(decimalmessage)
	hexmessage= hex(decimalmessage)
	print(hexmessage)
	print(hexmessage[2:].decode("hex"))
	print(bytes.fromhex(hexmessage).decode())

The program returned the flag:

	picoCTF{us3_l@rg3r_pr1m3$_1335}

