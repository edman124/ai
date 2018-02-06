import sys, collections, queue, time
from Tkinter import *


def createNode(nodes,names):
	nodelist={}
	for i in range(len(nodes)):
		info=nodes[i].split(' ')
		nodelist[info[0]]=(info[1], info[2], names[i])
	return nodelist
def createEdge(edges):
	edgelist={}
	for e in edges:
		ed=e.split(' ')
		edgelist[ed[0]]+=[ed[1]]
		edgelist[ed[1]]+=[ed[0]]
	return edgelist
def draw(nodelist, edgelist):
	done=set()
	master = Tk()
	w = Canvas(master, width=50, height=50)
	w.pack()
	for key,val in edgelist:
		coord=nodelist[key]
		for n in val if n not in done:
			coord2=nodelist[val]
			w.create_line(coord[0],coord[1],coord2[0],coord2[1])
	mainloop()

nodeFile=open("romNodes.txt","r")
nodes=nodeFile.readlines()
edgeFile=open("romEdges.txt","r")
edges=edgeFile.readlines()
nameFile=open("romFullNames.txt","r")
names=nodeFile.readlines()
nodelist=createNode(nodes,names)
edgelist=createEdge(edges)
draw(nodelist,edgelist)
