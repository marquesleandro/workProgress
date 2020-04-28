# ==========================================
# Code created by Leandro Marques at 04/2020
# Gesar Search Group
# State University of the Rio de Janeiro
# e-mail: marquesleandro67@gmail.com
# ==========================================

# This code is used to remesh


import numpy as np


# ----------------------- REMESHING - DELETE NODES ----------------------
def deleteNodes(_numNodes, _numElements, _x, _y, _IEN, _neighborsNodes, _boundaryNodes, _limitLength): 

 # numNodes x neighNodes Loop / min Edges List
 minEdges = []
 for i in range(0,_numNodes):
  xNode = _x[i]
  yNode = _y[i]
 
  for j in _neighborsNodes[i]:
   xNeighNode = _x[j]
   yNeighNode = _y[j]
 
   xLength = xNode - xNeighNode
   yLength = yNode - yNeighNode
   length = float(np.sqrt(xLength**2 + yLength**2))
 
   if length <= _limitLength:
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
   if minEdges[i][0] in _boundaryNodes:
    delNodes.append(minEdges[i][1])
    node = minEdges[i][0]
    minEdges[i][0] = minEdges[i][1]
    minEdges[i][1] = node
  
   # delNode is within mesh
   else:
    delNodes.append(minEdges[i][0])
    
    xNode1 = _x[minEdges[i][0]]
    yNode1 = _y[minEdges[i][0]]
    xNode2 = _x[minEdges[i][1]]
    yNode2 = _y[minEdges[i][1]]
   
    xAVG = (xNode1 + xNode2)/2.0
    yAVG = (yNode1 + yNode2)/2.0
 
    _x[minEdges[i][1]] = xAVG
    _y[minEdges[i][1]] = yAVG
 
 
 delNodes.sort()
 print ""
 print 'delNodes'
 print delNodes
 
 
 
 
 # assembly delete Elements List and rename delete Node -> near Node
 deleteElements = []
 for i in range(0,len(minEdges)):
  edgesElements = list(set(np.where(_IEN==minEdges[i][0])[0]) & set(np.where(_IEN==minEdges[i][1])[0]))
 
  # rename delete Node -> near Node
  _IEN = np.where(_IEN==minEdges[i][0],minEdges[i][1],_IEN)
 
  for j in range(0,len(edgesElements)):
   deleteElements.append(edgesElements[j])
 deleteElements.sort()
 print ""
 print 'delete IEN Elements'
 print deleteElements
 print ""
 print 'rename delete Node -> near Node'
 print _IEN
 
 
 
 
 # delete IEN Elements
 for e in reversed(deleteElements):
  _IEN = np.delete(_IEN,e,0)
 print ""
 print 'delete IEN Elements'
 print _IEN
 
 
 
 # rename all Nodes and delete Coord Nodes using reversed loop
 for i in reversed(range(len(delNodes))):
  _IEN = np.where(_IEN>delNodes[i],_IEN-1,_IEN)
  _x = np.delete(_x,delNodes[i],0)
  _y = np.delete(_y,delNodes[i],0)
 print ""
 print 'rename all Nodes'
 print _IEN
 
 
 
 # delete boundary nodes elements only
 for e in reversed(range(len(_IEN))):
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]
 
  x1 = float(_x[v1])
  x2 = float(_x[v2])
  x3 = float(_x[v3])
 
  y1 = float(_y[v1])
  y2 = float(_y[v2])
  y3 = float(_y[v3])
 
  A = 0.5*np.linalg.det(np.array([[1, x1, y1],
                                  [1, x2, y2],
                                  [1, x3, y3]]))
 
  if A == 0.0:
   _IEN = np.delete(_IEN,e,0)
 
 
 print ""
 print 'IEN Final'
 print _IEN
 
 print ""
 print 'x Final'
 print _x
 
 print ""
 print 'y Final'
 print _y


 _numNodes = len(_x)
 _numElements = len(_IEN)

 neighborsNodes = {}
 neighborsNodesALE = {}
 neighborsElements = {}
 npts = []
 for i in range(0, _numNodes):  
  neighborsNodes[i] = []
  neighborsNodesALE[i] = []
  neighborsElements[i] = []
  npts.append(i)


 length = []
 for e in range(0, _numElements):
  v1 = _IEN[e][0]
  v2 = _IEN[e][1]
  v3 = _IEN[e][2]
 
  neighborsNodes[v1].extend(_IEN[e])  
  neighborsNodes[v2].extend(_IEN[e])  
  neighborsNodes[v3].extend(_IEN[e])  

  neighborsNodes[v1] = list(set(neighborsNodes[v1]))
  neighborsNodes[v2] = list(set(neighborsNodes[v2]))
  neighborsNodes[v3] = list(set(neighborsNodes[v3]))

  neighborsNodesALE[v1].extend(_IEN[e])  
  neighborsNodesALE[v2].extend(_IEN[e])  
  neighborsNodesALE[v3].extend(_IEN[e])  
    
  neighborsNodesALE[v1] = list(set(neighborsNodesALE[v1]))
  neighborsNodesALE[v2] = list(set(neighborsNodesALE[v2]))
  neighborsNodesALE[v3] = list(set(neighborsNodesALE[v3]))

  neighborsElements[v1].append(e)  
  neighborsElements[v2].append(e)  
  neighborsElements[v3].append(e)  

  x_a = _x[v1] - _x[v2]
  x_b = _x[v2] - _x[v3]
  x_c = _x[v3] - _x[v1]
  
  y_a = _y[v1] - _y[v2]
  y_b = _y[v2] - _y[v3]
  y_c = _y[v3] - _y[v1]
  
  length1 = np.sqrt(x_a**2 + y_a**2)
  length2 = np.sqrt(x_b**2 + y_b**2)
  length3 = np.sqrt(x_c**2 + y_c**2)

  length.append(length1)
  length.append(length2)
  length.append(length3)
  
 minLengthMesh = min(length)

 return _numNodes, _numElements, _x, _y, _IEN, neighborsNodes, neighborsNodesALE, neighborsElements, minLengthMesh
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
