def genPrimes(limit):
  # this is consider the limit also in the list, eg in genPrimes(5)  5 is also a prime
  limit = limit +1
  bools = []
  primes = []
  
  # generate a list of booleans all set to True initially
  # the list is indexed from 2 to limit representing all numbers
  # e.g. [True, True, True, True] = [2, 3, 4, 5]
  for i in range(0, limit):
    bools.append(True)

   
  # loop from 2 to limit setting the composite numbers to False
  # we start from 2 because we know 1 is not a prime number
  for i in range(2, limit):
    if bools[i]:
      for j in range(i*2, limit, i):
        bools[j] = False

  #print(bools)       
  # now generate the list of primes only where
  # there is a True value in the bools list
  for p in range(2, len(bools)):
    if (bools[p]):
      primes.append(p)
      
  return primes
    
print(genPrimes(101))
