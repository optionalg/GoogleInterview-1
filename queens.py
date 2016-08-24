


def queens(qpos, pos):
	cols = []
	rows = []
	diagUD = []
	diagDU = []
	for x,y in qpos:
		cols.append(x)
		rows.append(y)
		diagUD.append(x - y + 7)
		diagDU.append(x + y)
	x,y = pos
	if( x in cols or y in rows or (x - y + 7) in diagUD or (x + y) in diagDU):
		return True
	else:
		return False

if __name__ == "__main__":
	
	qpos = [ (0,0), (4,4) ]
	pos = (2,2)
	print queens(qpos,pos)


