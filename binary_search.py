import time

def binary_search(arr, el):
	mx = len(arr)-1
	mn = 0
	arr.sort()
	while True:
		if mx == mn:
			if arr[mx] == el:
				return True
			else:
				return False
		else:
			mid = (mx - mn)/2 + mn
			if arr[mid] == el:
				return True
			elif arr[mid] < el:
				mn = mid + 1
				mx = mx
			elif arr[mid] > el:
				mx = mid
				mn = mn

import random
if __name__ == "__main__":
	tests = 10000
	passed = 0
	for i in range(0,tests):
		arr = [random.randint(0,1000) for r in xrange(100)] # v1
  		el = random.randint(0,1000)
		truth = binary_search(arr, el)
		if truth == ( el in arr ):
			passed = passed + 1
	
	print "Passed: {}/{}".format(passed,tests)
			
