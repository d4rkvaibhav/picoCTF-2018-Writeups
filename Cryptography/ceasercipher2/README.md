Problem Statement(250 points):

Can you help us decrypt this message? We believe it is a form of a caesar cipher. You can find the ciphertext in /problems/caesar-cipher-2_3_4a1aa2a4d0f79a1f8e9a29319250740a on the shell server.

Solutions:

The message given was "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA".I saw a pattern that if ascii value of given charater is greater than 65 we have to substract 34 to get capital letters and for less than 65 we have to add 60 to get small letters.So i wrote a small piece of code in python3 which you can see below: 

	x="4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"
	s=''
	for i in x:
		
		if(ord(i)<=65):
			s+=chr(ord(i)+60)
		else:
			s+=chr(ord(i)-34)
	print(s)

So the decoded text was :

	picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}

