
def applyOp(val, op, num):
	if op == "+":
		return val + num
	elif op == "*":
		return val * num
	elif op == "/":
		return val / num
	elif op == "-":	
		return val - num

def check(path, current, nums, ops, target, results):
	#print path, current, nums, ops, target, results
	if ( current == target ):
		results.append(path)
		return
	elif ( len(nums) == 0):
		return
	else:
		for op in ops:
			for num in nums:
				new_path = path[:]
				new_nums = nums[:]
				new_nums.remove(num)
				new_path.append(op)
				new_path.append(num)
				new_current = applyOp(current, op, num )
				check( new_path, new_current, new_nums, ops, target, results)


def Ops(ops, nums, target):
	results = []	
	for num in nums:
		path = [num]
		current = num
		new_nums = nums[:]
		new_nums.remove(num)
		check( path, current, new_nums, ops, target, results)
	return results



if __name__ == "__main__":
	ops = ["*", "/", "-", "+"]
	nums = [2,3,4,5,6]
	target = 5
	print Ops(ops, nums, target)
