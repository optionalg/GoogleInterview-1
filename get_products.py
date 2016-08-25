

def getProductsAllBut(arr):
	prod = 1
	for i in arr:
		prod = prod * i
	
	result = []
	for i in arr:
		if i != 0:
			result.append(prod/i)
		else:
			result.append(0)
	return result

import random
if __name__ == "__main__":
	arr = [ random.randint(1,100) for i in range(1,10) ]
	print arr
	print getProductsAllBut(arr))
		
