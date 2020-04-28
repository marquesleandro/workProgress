import numpy as np
import remeshing 

# ----------------- IMPORT MSH -----------------------------------
limitLength = 0.391

IEN = np.zeros([16,3], dtype = int)
IEN[0]  = [ 0  , 7  , 9  ]
IEN[1]  = [ 7  , 8  , 9  ]
IEN[2]  = [ 9  , 1  , 0  ]
IEN[3]  = [ 9  , 8  , 11 ]
IEN[4]  = [ 9  , 12 , 1  ]
IEN[5]  = [ 12 , 2  , 1  ]
IEN[6]  = [ 2  , 12 , 3  ]
IEN[7]  = [ 3  , 12 , 11 ]
IEN[8]  = [ 12 , 9  , 11 ]
IEN[9]  = [ 3  , 11 , 4  ]
IEN[10] = [ 4  , 11 , 13 ]
IEN[11] = [ 13 , 11 , 10 ]
IEN[12] = [ 10 , 14 , 13 ]
IEN[13] = [ 13 , 5  , 4  ]
IEN[14] = [ 5  , 13 , 14 ]
IEN[15] = [ 5  , 14 , 6  ]
print 'IEN'
print IEN

x = np.zeros([15,1], dtype = float)
y = np.zeros([15,1], dtype = float)

x[0]  = 0.0
x[1]  = 0.5
x[2]  = 1.0
x[3]  = 1.0
x[4]  = 1.0
x[5]  = 1.0
x[6]  = 1.0
x[7]  = 0.0
x[8]  = 0.0
x[9]  = 0.4
x[10] = 0.2
x[11] = 0.5
x[12] = 0.6
x[13] = 0.8
x[14] = 0.7
print ""
print 'x'
print x


y[0]  = 2.0
y[1]  = 2.0
y[2]  = 2.0
y[3]  = 1.5
y[4]  = 1.0
y[5]  = 0.5
y[6]  = 0.0
y[7]  = 1.6
y[8]  = 0.8
y[9]  = 1.6
y[10] = 0.75
y[11] = 1.25
y[12] = 1.6
y[13] = 0.75
y[14] = 0.25
print ""
print 'y'
print y



numNodes = len(x)
numElements = len(IEN)
print ""
print 'numNodes'
print numNodes
print ""
print 'numElements'
print numElements


boundaryNodes = []
boundaryNodes = [0,1,2,3,4,5,6]
print ""
print 'boundaryNodes'
print boundaryNodes


neighborsNodes = {}
neighborsElements = {}
for i in range(0,numNodes):
 neighborsNodes[i] = []
 neighborsElements[i] = []


neighborsNodes[0]  = [ 1  , 7  , 9  ]
neighborsNodes[1]  = [ 0  , 2  , 9  , 12 ]
neighborsNodes[2]  = [ 1  , 3  , 12 ]
neighborsNodes[3]  = [ 2  , 4  , 11 , 12 ]
neighborsNodes[4]  = [ 3  , 5  , 11 , 13 ]
neighborsNodes[5]  = [ 4  , 6  , 13 , 14 ]
neighborsNodes[6]  = [ 5  , 14 ]
neighborsNodes[7]  = [ 0  , 8  , 9  ]
neighborsNodes[8]  = [ 7  , 9  , 11 ]
neighborsNodes[9]  = [ 0  , 1  , 7  , 8  , 11 , 12 ]
neighborsNodes[10] = [ 11 , 13 , 14 ]
neighborsNodes[11] = [ 3  , 4  , 8  , 9  , 10 , 12 , 13 ]
neighborsNodes[12] = [ 1  , 2  , 3  , 9  , 11 ]
neighborsNodes[13] = [ 4  , 5  , 10 , 11 , 14 ]
neighborsNodes[14] = [ 5  , 6  , 10 ]

neighborsElements[0]  = [ 0  , 2  ]
neighborsElements[1]  = [ 2  , 4  , 5  ]
neighborsElements[2]  = [ 5  , 6  ]
neighborsElements[3]  = [ 6  , 7  , 9  ]
neighborsElements[4]  = [ 9  , 10 , 13 ]
neighborsElements[5]  = [ 13 , 14 , 15 ]
neighborsElements[6]  = [ 15 ]
neighborsElements[7]  = [ 0  , 1  ]
neighborsElements[8]  = [ 1  , 3  ]
neighborsElements[9]  = [ 0  , 1  , 2  , 3  , 4  , 8 ]
neighborsElements[10] = [ 11 , 12 ]
neighborsElements[11] = [ 3  , 7  , 8  , 9  , 10 , 11 ]
neighborsElements[12] = [ 4  , 5  , 6  , 7  , 8  ]
neighborsElements[13] = [ 10 , 11 , 12 , 13 , 14 ]
neighborsElements[14] = [ 12 , 14 , 15 ]
# -----------------------------------------------------------------------

# remeshin delete Nodes
numNodes, numElements, x, y, IEN, neighborsNodes, neighborsNodesALE, neighborsElements, minLengthMesh = remeshing.deleteNodes(numNodes, numElements, x, y, IEN, neighborsNodes, boundaryNodes, limitLength)

print ""
print "numNodes"
print numNodes
print ""
print "numElements" 
print numElements
print ""
print "x"
print x
print ""
print "y"
print y
print ""
print "IEN"
print IEN
print ""
print "neighborsNodes"
print neighborsNodes
print ""
print "neighborsNodesALE"
print neighborsNodesALE
print ""
print "neighborsElements"
print neighborsElements
print ""
print "minLengthMesh"
print minLengthMesh







