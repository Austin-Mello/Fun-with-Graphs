import sys

# ---------------------------------------
# CLASSES
# ---------------------------------------

class Node: 
	def __init__(self):
		self.length = -1
		self.subpaths = 0

class Edge:
	def __init__(self):
		self.parent = 0
		self.child = 0
		self.weight = 0

if __name__ == '__main__':

	# ---------------------------------------
	# MAIN VARIABLES
	# ---------------------------------------

	#Declare longest path variable.
	longest = 0
	#Declare number of subpaths variable.
	subpaths = 0

	# ---------------------------------------
	#SCRAPING THE FILE
	# ---------------------------------------

	#Iterator for identifying the current line of the text file.
	#Only really necessary for line 1, but there ya go.
	i = 0

	#Load up the classes and adjacency matrix.
	for lines in sys.stdin.read().splitlines():
		#Scrape off the first line.
		if i < 1:
			#Build the nodes and edges classes and the matrix.
			numbers = lines.split(" ")
			N = int(numbers[0])
			M = int(numbers[1])

			#Build the list of Node classes.
			nodes = [Node() for j in range(N)]
			

			#Build the matrix of Edge classes.
			matrix = [[Edge() for j in range(M)] for k in range(M)]

			#Make the root node's subpath = 1 and length = 0.
			#It's a special boy that must be handled with care.
			nodes[0].subpaths = 1
			nodes[0].length = 0

			i += 1

		#Scrape off the other lines.
		else:
			#Fill the node and edge classes.
			
			#Grab edge/node properties
			numbers = lines.split(" ")
			parent = int(numbers[0])
			child = int(numbers[1])
			weight = int(numbers[2])

			matrix[parent - 1][child - 1].weight = weight
			matrix[parent - 1][child - 1].parent = parent
			matrix[parent - 1][child - 1].child = child

	# -------------------------------------------------
	# BELLMAN-FORD ALGORITHM
	# -------------------------------------------------

	#Examine each row.
	for x in range(len(nodes)):
		
		# print('-------\n')
		# print(x)
		#Examine each column.
		for y in range(len(nodes)):
			
			#If the weight != 0, relax that edge.
			if matrix[x][y].weight != 0:

				#If the parent's length + edge weight is greater that the 
				#child's length, swap it out with parent's length + weight.
				if nodes[x].length + matrix[x][y].weight > nodes[y].length:
					nodes[y].length = nodes[x].length + matrix[x][y].weight

					#Also, transfer the parent's subpath counter to the child.
					nodes[y].subpaths = nodes[x].subpaths

					#Update the longest distance, if necessary.
					if nodes[y].length > longest:
						longest = nodes[y].length

					#Update the greatest number of subpaths, if necessary.
					if nodes[y].subpaths > subpaths:
						subpaths = nodes[y].subpaths

				#If the parent's length + edge weight equals the child's length
				#add the parent's subpaths to the child's subpaths.
				elif nodes[x].length + matrix[x][y].weight == nodes[y].length:
					nodes[y].subpaths += nodes[x].subpaths

					#Update the greatest number of subpaths, if necessary.
					if nodes[y].subpaths > subpaths:
						subpaths = nodes[y].subpaths

	sys.stdout.write('The longest path is: ' + str(longest) + 
	'\nThe total longest paths is: ' + str(subpaths))








