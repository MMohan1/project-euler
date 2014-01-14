def largest_palindrom():
	l = [] 
	for i in range(100,1000):
		for j in range(100,1000):
			prod = i * j 
			prod_str = str(prod)
			if len(prod_str) == 6 and prod_str == prod_str[::-1]:
				l.append(prod)
	l.sort()
	l.reverse()
	print l[0]

if __name__ == '__main__':
	largest_palindrom()
