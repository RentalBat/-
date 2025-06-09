def factor(x):
	p = 2
	while x>2:
		if x%p==0:
			x/=p
			print(p)

		else:
			p+=1

number = 450
factor(number)
