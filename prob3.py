def largest_prime():
	num = 600851475143L
	new_num = num
	largest_prime = 0
	counter = 2
	while(counter * counter <= new_num):
		if(new_num%counter ==0):
			new_num = new_num / counter
			largest_prime = counter
		else:
			counter += 1
	if new_num > largest_prime:
		largest_prime = new_num
	print largest_prime

if __name__ == '__main__':
	largest_prime()
