from red_black_tree import build_tree
'''
def generate() :
	mylist = range(10)
	for i in mylist:
		yield i*i
'''
def search(generator, verify):
	root = build_tree([item for item in range(1000000)])
	vertex = root
	while vertex:
		yield vertex.value
		if verify(vertex):
			vertex = vertex.left
		else:
			vertex = vertex.right
'''
def main():
	searcher = search(lambda: for i in range(10) yield i*i, lambda vertex: vertex.value > 5)
	print([item for item in searcher])
	#print(root.value)
'''
if __name__ == '__main__':
	build_tree([1,2,3,4,5,6,7,8])