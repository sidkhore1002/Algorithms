
g=[[0,3,1,0,0],[3,0,4,5,0],[1,4,0,6,7],[0,5,6,0,2],[0,0,7,2,0]]

print g
l=[]
ll=[]
final=[]
final1=[]
f2=[]
ff=[]

for i in range(len(g)):
	l.append([i])
ll.append(l)

#print ll
list1=ll[0]
print list1

for i in range(len(g)):
	for j in range(len(g)):
		if(g[i][j]>0):
			final.append(str(i)+str(j)+str(g[i][j]))
#print final

for i in range(len(final)):
	final1.append(int(final[i][::-1]))
#print final1
final1.sort()
#print final1

for i in range(len(final1)):
	s=str(final1[i])
	final1[i]=s[1]+s[2]
#print final1
cnt=0
while(cnt<len(final1)):
	f2.append(final1[cnt])
	cnt=cnt+2
print f2	


for k in range(len(f2)):
	m=f2[k]
	for i in range(len(list1)):	
		if(int(m[0]) in list1[i]):				
			ind1=i
#			print ind1
	for j in range(len(list1)):	
		if(int(m[1]) in list1[j]):							
			ind2=j
#			print ind2
	
	if(ind1!=ind2):	
		ff.append(m)

#		print list1[ind1]+list1[ind2]
		list1[ind1]=list1[ind1]+list1[ind2]
	
		list1.remove(list1[ind2])
	
		print list1

print ff
