def quicksort(l):
  if l:
    left = [x for x in l if x < l[0]]
    right = [x for x in l if x > l[0]]
    if len(left) > 1:
      left = quicksort(left)
    if len(right) > 1:
      right = quicksort(right)
    return left + [l[0]] * l.count(l[0]) + right
  return []

pares = []
impares = []

for o in range(int(raw_input())):
  numero = int(raw_input())
  if (numero%2) == 0:
    pares.append(numero)
  else:
    impares.append(numero)

pares_ord = quicksort(pares)
impares_ord = quicksort(impares)

for g in range(len(pares)):
  print pares_ord[g]
for l in range(len(impares)-1,-1,-1):
  print impares_ord[l]  
