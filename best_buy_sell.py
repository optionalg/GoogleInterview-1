

def best_buy_sell(arr):
	best = arr[1] - arr[0]
	minBefore = arr[0]
	for x in arr[1:]:
		best = max(best, x - minBefore)
		minBefore = min( x, minBefore)
	return best


if __name__ == "__main__":
	print best_buy_sell([10,5,50,1,10])
	print best_buy_sell([10,9,8,7,6,5])
