Problem Statement(250 points):

We ran into some weird puzzles we think may mean something, can you help me solve one? Connect with nc 2018shell2.picoctf.com 40440

Solution:

The output of the terminal when log in to the given service was :

	0x7069636f4354467b64305f755f6b6e30775f7468335f7740795f325f5253405f35643338336531307dL <type 'long'>
	Hello, Welcome to RSA Madlibs
	Keeping young children entertained, since, well, nev3r
	Tell us how to fill in the blanks, or if it's even possible to do so
	Everything, input and output, is decimal, not hex
	#### NEW MADLIB ####
	q : 93187
	p : 94603
	##### WE'RE GONNA NEED THE FOLLOWING ####

So we have to answer some questions to get the flag but in the first line i saw a hexadecimal number.i was curious to know why it is there so i converted it to string and surprisingly it was the flag:

	picoCTF{d0_u_kn0w_th3_w@y_2_RS@_5d383e10}

