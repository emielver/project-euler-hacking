import time
def SieveOfEratosthenes(n, prime,primesquare, a): 
	for i in range(2,n+1): 
		prime[i] = True
		
	for i in range((n * n + 1)+1): 
		primesquare[i] = False

	prime[1] = False

	p = 2
	while(p * p <= n): 
		if (prime[p] == True): 
			i = p * 2
			while(i <= n): 
				prime[i] = False
				i += p 
		p+=1
	

	j = 0
	for p in range(2,n+1): 
		if (prime[p]==True): 
			a[j] = p 

			primesquare[p * p] = True
			j+=1

# Function to count divisors 
def countDivisors(n): 
	if (n == 1): 
		return 1

	prime = [False]*(n + 2) 
	primesquare = [False]*(n * n + 2) 
	
	a = [0]*n 

	# Calling SieveOfEratosthenes to 
	# store prime factors of n and to 
	# store square of prime factors of n 
	SieveOfEratosthenes(n, prime, primesquare, a) 

	# ans will contain total 
	# number of distinct divisors 
	ans = 1

	# Loop for counting factors of n 
	i=0
	while(1): 
		# a[i] is not less than cube root n 
		if(a[i] * a[i] * a[i] > n): 
			break

		# Calculating power of a[i] in n. 
		cnt = 1 # cnt is power of 
				# prime a[i] in n. 
		while (n % a[i] == 0): # if a[i] is a factor of n 
			n = n / a[i] 
			cnt = cnt + 1 # incrementing power 

		# Calculating number of divisors 
		# If n = a^p * b^q then total 
		# divisors of n are (p+1)*(q+1) 
		ans = ans * cnt 
		i+=1

	# if a[i] is greater than 
	# cube root of n 
	
	n=int(n) 
	# First case 
	if (prime[n]==True): 
		ans = ans * 2

	# Second case 
	elif (primesquare[n]==True): 
		ans = ans * 3

	# Third casse 
	elif (n != 1): 
		ans = ans * 4

	return ans # Total divisors 
start = time.time()
count = 0
for i in range(1, 10 ** 7):
    if countDivisors(i) == countDivisors(i+1):
            count += 1
print(count)
print(time.time() - start)
# This code is contributed 
# by mits 
