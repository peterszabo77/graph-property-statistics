import numpy as np
from itertools import permutations 
import os, shutil
import string
from graphviz import Digraph
import matplotlib as mpl

N_RANDOMIZATIONS = 1000 # number of randomizations
N = 10 # dominance matrix size

GRAPHSAVEDIR = 'graphs'
GRAPHVIZENGINE = 'circo' # 'neato', 'fdp', 'circo' or 'dot'

RANDOMSEED = 0

np.random.seed(RANDOMSEED)

# create/clean save directory
try:
	shutil.rmtree(GRAPHSAVEDIR)
except:
	pass
os.mkdir(GRAPHSAVEDIR)

def getDomMatrix(N, r): # N-matrix size, r-randomness measure [between 0 (complete hierarchy) and 1 (complete randomness)]
	# m[i,j] = 1 means i is dominant over j
	m = np.zeros((N,N))
	for i in range(N):
		for j in range(i+1,N):
			if np.random.rand()<r:
				m[i,j] = np.random.choice([1,-1])
			else:
				m[i,j] = 1
			m[j,i] = -m[i,j]
	return m

def getDomIndex(m):
# for all i,j,k triplets check whether the sign of 
# hierarchical if m[i,j]
	dom_index = 0
	permutationlist = list(permutations(range(N),3))
	for i,j,k in permutationlist:
		hierarchical = False
		if m[i,j]==1 and m[j,k]==1 and m[i,k]==1:  # i->j->k hierarchical if i->k
			hierarchical = True
		if m[i,j]==-1 and m[j,k]==-1 and m[i,k]==-1:  # i<-j<-k hierarchical if i<-k
			hierarchical = True
		if m[i,j]==1 and m[j,k]==-1:  # i->j<-k is always hierarchical
			hierarchical = True
		if m[i,j]==-1 and m[j,k]==1:  # i<-j->k is always hierarchical
			hierarchical = True
		dom_index += int(hierarchical)
	dom_index /= len(permutationlist)
	return dom_index

def plotDomGraph(m, filename): # plot dominance matrices as directed graphs
	N_nodes = m.shape[0]
	node_strengths = np.sum(m,axis=1)/(m.shape[0]-1)
	node_strengths = (node_strengths+1)/2
	node_colors = [mpl.colors.rgb2hex([1-s,1-s,1]) for s in node_strengths]
	node_names = list(string.ascii_uppercase[0:N_nodes])

	foodwebgraph = Digraph()
	foodwebgraph.rankdir = 'BT'
	foodwebgraph.engine = GRAPHVIZENGINE
	foodwebgraph.format = "pdf"
	# add nodes
	for idx,node_name in enumerate(node_names):
		nodecolor = node_colors[idx]
		foodwebgraph.node(node_name, style="filled", color='#000000', fillcolor=nodecolor, fontcolor='#000000')
	# add edges
	for i, i_name in enumerate(node_names):
		for j, j_name in enumerate(node_names):
			edgecolor = '#000000'
			preflength = str(1.0)
			if m[i,j]==1:
				foodwebgraph.edge(i_name, j_name, color = edgecolor, len=preflength)	
	# save
	filepath = os.path.join(GRAPHSAVEDIR,filename)
	foodwebgraph.render(filepath, cleanup=True)

def get_significance(h):
	hierarchy_index = h
	random_matrices = [getDomMatrix(N,1) for i in range(N_RANDOMIZATIONS)]
	random_hierarchy_indices = np.array([getDomIndex(e) for e in random_matrices])
	p_value = np.mean((random_hierarchy_indices>hierarchy_index).astype(np.int))
	return p_value

m = getDomMatrix(N, 0) # a completely hierarchical dominance matrix
#m = getDomMatrix(N, 0.5) # a moderately hierarchical dominance matrix
#m = getDomMatrix(N, 1) # a completely random dominance matrix

H_index = getDomIndex(m)
p_value = get_significance(H_index)

print('H_index, p_value:')
print(H_index, p_value)

plotDomGraph(m,'m_'+str(H_index)+'_'+str(p_value))
