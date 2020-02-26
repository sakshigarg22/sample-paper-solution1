a = input()
b = input()
c = 0
for i in range(0,len(a)-len(b)+1):
	if b == a[i:i+len(b)]:
		c = c+1
print(c)
