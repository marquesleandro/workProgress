import numpy as np

# ----------------- IMPORT MSH -----------------------------------
IEN = np.zeros([18,3], dtype = int)
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

x = np.zeros([16,1], dtype = float)
y = np.zeros([16,1], dtype = float)

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




# ----------------------- REMESHING - DELETE NODES ----------------------
# numNodes x neighNodes Loop / min Edges List
minEdges = []

minLength = 0.391
for i in range(0,numNodes):
 xNode = x[i]
 yNode = y[i]

 for j in neighborsNodes[i]:
  xNeighNode = x[j]
  yNeighNode = y[j]

  xLength = xNode - xNeighNode
  yLength = yNode - yNeighNode
  length = float(np.sqrt(xLength**2 + yLength**2))

  if length <= minLength:
   minEdges.append([i,j,length])

minEdges = sorted(minEdges, key = lambda k:k[2]) #sort by min length

print ""
print 'minEdges'
print minEdges



# assembly delete Edges List for duplicates min Nodes
minNodes = []
delEdges = []
for i in range(0,len(minEdges)):
 for j in range(0,len(minEdges[i])-1):
  node = minEdges[i][j]
  if node in minNodes:
   delEdges.append(i)
   break
  else:
   minNodes.append(node)
delEdges = list(set(delEdges))
print ""
print 'delEdges'
print delEdges


# delete delEdges in minEdges List
for i in reversed(delEdges):
 del minEdges[i]
print ""
print 'minEdges'
print minEdges


# assembly delete Nodes List
delNodes = []
for i in range(0,len(minEdges)):

  # delNode is boundaryNode
  if minEdges[i][0] in boundaryNodes:
   delNodes.append(minEdges[i][1])
   node = minEdges[i][0]
   minEdges[i][0] = minEdges[i][1]
   minEdges[i][1] = node
 
  # delNode is within mesh
  else:
   delNodes.append(minEdges[i][0])
   
   xNode1 = x[minEdges[i][0]]
   yNode1 = y[minEdges[i][0]]
   xNode2 = x[minEdges[i][1]]
   yNode2 = y[minEdges[i][1]]
  
   xAVG = (xNode1 + xNode2)/2.0
   yAVG = (yNode1 + yNode2)/2.0

   x[minEdges[i][1]] = xAVG
   y[minEdges[i][1]] = yAVG


delNodes.sort()
print ""
print 'delNodes'
print delNodes




# assembly delete Elements List and rename delete Node -> near Node
deleteElements = []
for i in range(0,len(minEdges)):
 edgesElements = list(set(np.where(IEN==minEdges[i][0])[0]) & set(np.where(IEN==minEdges[i][1])[0]))

 # rename delete Node -> near Node
 IEN = np.where(IEN==minEdges[i][0],minEdges[i][1],IEN)

 for j in range(0,len(edgesElements)):
  deleteElements.append(edgesElements[j])
deleteElements.sort()
print ""
print 'delete IEN Elements'
print deleteElements
print ""
print 'rename delete Node -> near Node'
print IEN




# delete IEN Elements
for e in reversed(deleteElements):
 IEN = np.delete(IEN,e,0)
print ""
print 'delete IEN Elements'
print IEN



# rename all Nodes and delete Coord Nodes using reversed loop
for i in reversed(range(len(delNodes))):
 IEN = np.where(IEN>delNodes[i],IEN-1,IEN)
 x = np.delete(x,delNodes[i],0)
 y = np.delete(y,delNodes[i],0)
print ""
print 'rename all Nodes'
print IEN



# delete boundary nodes elements only
for e in reversed(range(len(IEN))):
 v1 = IEN[e][0]
 v2 = IEN[e][1]
 v3 = IEN[e][2]

 x1 = float(x[v1])
 x2 = float(x[v2])
 x3 = float(x[v3])

 y1 = float(y[v1])
 y2 = float(y[v2])
 y3 = float(y[v3])

 A = 0.5*np.linalg.det(np.array([[1, x1, y1],
                                 [1, x2, y2],
                                 [1, x3, y3]]))

 if A == 0.0:
  IEN = np.delete(IEN,e,0)


print ""
print 'IEN Final'
print IEN

print ""
print 'x Final'
print x

print ""
print 'y Final'
print y
# -----------------------------------------------------------------------




'''

para add um no

# ==========================================
# Code created by Leandro Marques at 03/2019
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to remesh domain

import sys
import numpy as np


def remeshing(_npoints, _nelem, _IEN, _x, _y, _dxmax, _neighbors_nodes, _neighbors_elements):
 for e in range(0, len(_IEN)):
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]

  x1 = np.sqrt((_x[v1] - x[v2])**2)
  x2 = np.sqrt((_x[v2] - x[v3])**2)
  x3 = np.sqrt((_x[v3] - x[v1])**2)

  y1 = np.sqrt((_y[v1] - y[v2])**2)
  y2 = np.sqrt((_y[v2] - y[v3])**2)
  y3 = np.sqrt((_y[v3] - y[v1])**2)

  edge1 = np.sqrt(x1**2 + y1**2)
  edge2 = np.sqrt(x2**2 + y2**2)
  edge3 = np.sqrt(x3**2 + y3**2)

  if edge1 > _dxmax:
   _npoints = _npoints + 1
   vnew = _npoints

   xnew = (_x[v1] + _x[v2])/2.0
   ynew = (_y[v1] + _y[v2])/2.0

   _x.vstack(xnew)
   _y.vstack(ynew)

   IEN1 = [v1,vnew,v3]
   IEN2 = [v2,v3,vnew]
   np.delete(_IEN,e,0)
   _IEN = np.vstack((_IEN,IEN1))
   _IEN = np.vstack((_IEN,IEN2))

   _neighbors_nodes[vnew] = []
   _neighbors_nodes[vnew].extend(IEN1)
   _neighbors_nodes[vnew].extend(IEN2)

   _neighbors_nodes[v1].remove(v2)
   _neighbors_nodes[v2].remove(v1)
   _neighbors_nodes[v1].extend(vnew)
   _neighbors_nodes[v2].extend(vnew)
   _neighbors_nodes[v1] = list(set(_neighbors_nodes[v1]))
   _neighbors_nodes[v2] = list(set(_neighbors_nodes[v2]))
   _neighbors_nodes[vnew] = list(set(_neighbors_nodes[vnew]))

   _nelem = len(_IEN)

   _neighbors_elements[v1].remove(e)
   _neighbors_elements[v2].remove(e)
   _neighbors_elements[v3].remove(e)
   _neighbors_elements[v1].append(_nelem)
   _neighbors_elements[vnew].append(_nelem)
   _neighbors_elements[v3].append(_nelem)
   _neighbors_elements[v2].append(_nelem+1)
   _neighbors_elements[v3].append(_nelem+1)
   _neighbors_elements[vnew].append(_nelem+1)
   _neighbors_elements[v1] = list(set(_neighbors_elements[v1]))
   _neighbors_elements[v2] = list(set(_neighbors_elements[v2]))
   _neighbors_elements[v3] = list(set(_neighbors_elements[v3]))
   _neighbors_elements[vnew] = list(set(_neighbors_elements[vnew]))


---------------------continuar elif para edge2 e edge3 ------------------------------------

def Laplacian_smoothing(_neighbors_nodes, _npoints, _x, _y, _dt):
 vx_laplaciansmooth = np.zeros([_npoints,1], dtype = float)
 vy_laplaciansmooth = np.zeros([_npoints,1], dtype = float)

 for i in range(0,_npoints):
  num_nghb = len(_neighbors_nodes[i])
  x_distance = 0.0
  y_distance = 0.0

  for j in range(0,num_nghb):
   node_nghb = _neighbors_nodes[i][j]

   x_distance = x_distance + (1.0/num_nghb)*(_x[node_nghb] - _x[i])
   y_distance = y_distance + (1.0/num_nghb)*(_y[node_nghb] - _y[i])

  vx_laplaciansmooth[i] = x_distance/_dt
  vy_laplaciansmooth[i] = y_distance/_dt

 return vx_laplaciansmooth, vy_laplaciansmooth


def Velocity_smoothing(_neighbors_nodes, _npoints, _vx, _vy):
 vx_velocitysmooth = np.zeros([_npoints,1], dtype = float)
 vy_velocitysmooth = np.zeros([_npoints,1], dtype = float)

 for i in range(0,_npoints):
  num_nghb = len(_neighbors_nodes[i])

  for j in range(0,num_nghb):
   node_nghb = _neighbors_nodes[i][j]

   vx_velocitysmooth = vx_velocitysmooth + (1.0/num_nghb)*_vx[node_nghb]
   vy_velocitysmooth = vy_velocitysmooth + (1.0/num_nghb)*_vy[node_nghb]


 return vx_velocitysmooth, vy_velocitysmooth

'''
