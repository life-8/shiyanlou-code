for a in range(1,101):
	b = a % 7
	if b == 0:
		continue
	c = a % 10
	if  c == 7:
		continue
	d = a // 10
	if d == 7:
		continue
	print(a)

