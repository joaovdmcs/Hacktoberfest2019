def Feynman(a):
	return ((a*(a+1)*((2*a)+1))/6)

while True:
	a = int(raw_input())
	if a == 0:
		break
	else:
		print Feynman(a)	
