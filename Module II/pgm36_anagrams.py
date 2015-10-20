def anagram(a):
	dic=dict()
	h=[]
	result=[]
	for i in a:
		j=list(i)
		j.sort()
		d=''.join(j)
		dic[i]=d
       	

	for k in range(len(a)-1):
		
		temp=[]
		if a[k] not in h:
			for j in range(k+1,len(a)):
				if dic[a[k]]==dic[a[j]]:
					temp.append(a[j])
					h.append(a[j])

			
			temp.append(a[k])
			
			result.append(temp)

	return result

print anagram(['eat', 'ate', 'done', 'tea', 'soup', 'node'])

