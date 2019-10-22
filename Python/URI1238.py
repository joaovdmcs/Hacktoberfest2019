for i in range(int(raw_input())):
  a,b = map(str,raw_input().split())

  if len(a) <= len(b):
    menor = a.split()
    a1 = a.split()
    maior = b.split()
    b1 = b.split()
  else:
    menor = b.split()
    a1 = a.split()
    maior = a.split()
    b1 = b.split()  

  String = ""
  for i in range(len(menor[0])):
    String = String + a1[0][i] + b1[0][i]

  if len(a) != len(b):
    for k in range(len(maior[0])-len(menor[0])+1,len(maior[0])):
      String += maior[0][k]

  print String
