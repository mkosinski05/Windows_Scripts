import xml.etree.ElementTree as ET
import sys

mydict = {}

def parse_node ( node, D ): 
	for child in node:
		try :
			print( child.attrib['TEXT'])
			D[child.attrib['TEXT']] = {}
			parse_node (child, D[child.attrib['TEXT']])
		except :
			pass
	
def printTree(tree, d = 0):
	if (tree == None or len(tree) == 0):
		print ("\t" * d, "-")
	else:
		for key, val in tree.items():
			if (isinstance(val, dict)):
				print ("\t" * d, key)
				printTree(val, d+1)
			else:
				print ("\t" * d, key, str('(') + val + str(')'))
if __name__ == "__main__":
	if len(sys.argv[1:]) > 0:
		#print(sys.argv[1])
		tree = ET.parse(sys.argv[1])
		root = tree.getroot()
		#print(root[0].tag)
		parse_node(root, mydict)
		printTree(mydict)