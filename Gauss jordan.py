import ast
a=ast.literal_eval(input('enter the augmented matrix:'))
n=len(a)
for i in range(n):
	k=None
	for j in range(n):
		if a[i][j]!=0.0:
			h=a[i][j]
			k=j
			break
	if k==None:
		print ('No solution')
	else:
		for j in range(n+1):
			a[i][j]/=h
		for l in range(n):
			if l!=i:
				b=a[l][k]
				for j in range(n+1):
					a[l][j]-=a[i][j]*b
for i in range(n):
	for j in range(n):
		if a[i][j]==1.0 and i!=j:
			a[i],a[j]=a[j],a[i]

print([a[i][n] for i in range(n)])