import sys, collections, queue, time
from tkinter import *
from math import pi , acos , sin , cos

def convert(namelist):
	cityname=sys.argv[1]
	destname=sys.argv[2]
	if len(sys.argv)==5:
		cityname=sys.argv[1]+' '+sys.argv[2]
		destname=sys.argv[3]+' '+sys.argv[4]
	elif len(sys.argv)>3:
		if sys.argv[1] not in namelist.keys():
			cityname=sys.argv[1]+' '+sys.argv[2]
			destname=sys.argv[3]
		else:
			destname=sys.argv[2]+' '+sys.argv[3]
	print(cityname, destname)
	return namelist[cityname], namelist[destname]
def calcd(y1,x1, y2,x2):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles = 6371 km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   #

def createNode(nodes,names):
	nodelist={}
	namelist={}
	minx=float(999999)
	maxx=float(0)
	miny=float(999999)
	maxy=float(0)
	for i in range(len(nodes)):
		info=nodes[i].replace('\n','').split(' ')
		nodelist[info[0]]=(float(info[1]), float(info[2]), info[0])  #(y, x, name)
		if minx>float(info[2]):
			minx=float(info[2])
		if maxx<float(info[2]):
			maxx=float(info[2])
		if miny>float(info[1]):
			miny=float(info[1])
		if maxy<float(info[1]):
			maxy=float(info[1])
	for i in range(len(names)):
		info=names[i].replace('\n','').split(' ')
		nam=info[1]
		for i in range(2,len(info)):
			nam+=' '+info[i]
		namelist[nam]=info[0]
		nodelist[info[0]]=(nodelist[info[0]][0], nodelist[info[0]][1], nam)


	return nodelist, namelist, minx, maxx, miny, maxy
def createEdge(edges,nodelist):
	edgelist={}
	totald=0
	for e in edges:
		ed=e.replace('\n','').split(' ')
		d=calcd(nodelist[ed[0]][0],nodelist[ed[0]][1],nodelist[ed[1]][0],nodelist[ed[1]][1])
		totald+=d
		edgelist[ed[0]]=edgelist.get(ed[0], [])+[(ed[1],d)]  #node symbol,dist
		edgelist[ed[1]]=edgelist.get(ed[1], [])+[(ed[0],d)]
	return edgelist,totald
def draw(nodelist, edgelist, minx, maxx, miny, maxy):
	scale=10
	done=set()
	master = Tk()
	w = Canvas(master, width=700, height=500)
	w.pack()
	for key,val in edgelist.items():
		coord=nodelist[key]
		for n in val:
			if n[0] not in done:
				coord2=nodelist[n[0]]
				w.create_line(scale*float(coord[1]-minx+1),scale*float(maxy-coord[0]+1),scale*float(coord2[1]-minx+1),scale*float(maxy-coord2[0]+1))
	return w

def heur(city, dest, nodelist): #city and dest take in codename
	return calcd(nodelist[city][0], nodelist[city][1], nodelist[dest][0], nodelist[dest][1])

def constructDict(city, dest, edgelist, nodelist, w): #city and dest take in codename
	path = {city:None}
	parseMe = queue.PriorityQueue()  #openset
	checked = set()	#closedset
	parseMe.put((0,0, city))
	scale=10
	count=0
	ch=0
	while True:
		count+=1
		tmp=parseMe.get()
		countFrom = tmp[1]
		curr=tmp[2]  #city
		if curr == dest:  
			break
		if curr in checked:
			continue
		checked.add(curr)	#blue
		ch+=1
		w.create_oval(scale*float(nodelist[curr][1]-minx+.75),scale*float(maxy-nodelist[curr][0]+.75),scale*float(nodelist[curr][1]-minx+1.25),scale*float(maxy-nodelist[curr][0]+1.25), outline="blue", fill="blue", width=.5)
		for child in edgelist[curr]:
			if(child[0] not in checked):
				h=countFrom+child[1]+heur(child[0], dest, nodelist)
				path[child[0]] = curr
				parseMe.put((h,countFrom+child[1],child[0]))	#green
				w.create_oval(scale*float(nodelist[child[0]][1]-minx+.75),scale*float(maxy-nodelist[child[0]][0]+.75),scale*float(nodelist[child[0]][1]-minx+1.25),scale*float(maxy-nodelist[child[0]][0]+1.25), outline="green", fill="green", width=.5)
		if count%500==0:
			w.update()
	print(ch)
	return path
def astar(city, dest, edgelist, nodelist, w):  #city and dest take in codename
	dic = constructDict(city, dest, edgelist, nodelist, w)
	ret = [nodelist[dest][2]]#[nodelist[city][2]] #city name
	scale=10
	travel=0
	if dic:
		tmp = dest
		while not dic[tmp] == None:
			# print(tmp)
			dist=0
			for i in range(len(edgelist[tmp])):
				if edgelist[tmp][i][0]==dic[tmp]:
					dist=edgelist[tmp][i][1]
					break
			travel+=dist
			print("print node: "+str(nodelist[dic[tmp]]))
			ret = [(nodelist[dic[tmp]][2], dist)] + ret
			w.create_oval(scale*float(nodelist[tmp][1]-minx+.75),scale*float(maxy-nodelist[tmp][0]+.75),scale*float(nodelist[tmp][1]-minx+1.25),scale*float(maxy-nodelist[tmp][0]+1.25), outline="red", fill="red", width=.5)
			tmp = dic[tmp] #red
	else:
		ret = "impossible"
	return ret, travel

t=time.time()
nodeFile=open("railroads\\rrNodes.txt","r")
nodes=nodeFile.readlines()
edgeFile=open("railroads\\rrEdges.txt","r")
edges=edgeFile.readlines()
nameFile=open("railroads\\rrNodeCity.txt","r")
names=nameFile.readlines()
nodelist, namelist, minx, maxx, miny, maxy=createNode(nodes,names)

# print(nodelist)
# print()
# print(namelist)

city, dest = convert(namelist)
edgelist, totald=createEdge(edges, nodelist)
print("city, dest:"+str(city)+"   "+str(dest))
# print(edgelist)

print(str(totald)+" miles")
w=draw(nodelist,edgelist, minx, maxx, miny, maxy)
ast,travel=astar(city, dest, edgelist, nodelist, w)
print(ast)
print("distance: "+str(travel)+"miles")
print("time: "+str(time.time()-t)+"sec")

mainloop()