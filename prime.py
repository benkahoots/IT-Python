def isPrime(num):
	max = int(num ** 1/2) + 1
	for i in range(2, max):
		if num % i == 0:
			return False
			
	return True
	
count = 0
for i in range(2, 100000):
	if isPrime(i) == True:
		count += 1
		
		print (i)
		
print ("Total Primes %s" %count)
