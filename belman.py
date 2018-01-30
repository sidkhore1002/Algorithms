import math

t =float("inf")


c=0
a=[0,t,t,t,t]
aa=[]
b=[]

def bel():
	for i in range(len(g)):
		for j in range(len(g)):
			if(g[i][j]!=0):
				if((a[i]+g[i][j])<a[j]):	
					a[j]=(a[i]+g[i][j])		
	
	print a

	
 
#g=[[0,1,2,0],[0,0,1,0],[0,0,0,3],[0,-6,0,0]]
g=[[0,-1,4,0,0],[0,0,3,2,2],[0,0,0,0,0],[0,1,5,0,0],[0,0,0,-3,0]]
 
print str(g)+"\n" 

for k in range(0,len(g)-1):	
	bel()


