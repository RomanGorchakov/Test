p = 0.2
a = 3.4
w = 0
summ = 0

while w < 16:
  p1 = 0
  w += 1
  p += a
  if w % 4 == 0:
    p1 = p * 2.5
    summ += p1
    print (w, p1, summ)
  else:
    summ += p
    print (w, p, summ)
