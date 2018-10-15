x="4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"
s=''
for i in x:
	
	if(ord(i)<=65):
		s+=chr(ord(i)+60)
	else:
		s+=chr(ord(i)-34)
print(s)