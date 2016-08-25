





import math
def eggDrop( h ):
	x = math.ceil( 0.5 * ( math.sqrt( 8*float(h) + 1 ) - 1 ) )
	return x


if __name__ == "__main__":
	print eggDrop(100)       
