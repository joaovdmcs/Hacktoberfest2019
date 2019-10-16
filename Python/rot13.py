def Rot13(String):
	nova_string = ""
	for i in range(len(String)):
		if String[i] != " ":
			
			if ord("A") <= ord(String[i]) and ord(String[i]) <= ord("Z"):
				novoC = ord(String[i])+13
				if ord("Z") < novoC:
					novoC = novoC - 26
					nova_string = nova_string + chr(novoC)
				else:
					nova_string = nova_string + chr(novoC)		
			
			elif ord("a") <= ord(String[i]) and ord(String[i]) <= ord("z"):
				 novoC = ord(String[i])+13
				 if ord("z") < novoC:
					 novoC = novoC - 26
					 nova_string = nova_string + chr(novoC)
				 else:
					 nova_string = nova_string + chr(novoC)
			else:
				 nova_string = nova_string + String[i]
		else:
			nova_string = nova_string + String[i]
	
	return nova_string				 

while True:
	try:
		a = raw_input()
		print Rot13(a)
	except EOFError:
		break	
	
