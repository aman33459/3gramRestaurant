import sys
import string
def count(st,text):
	cn=0
	for line in text:
		line = line.strip()
		line = line.lower()
		line = line.translate(line.maketrans("", "", string.punctuation))
		words = line.split(' ')
		words=words[1:]
		#print(words)
		fg=0
		for i  in range(0,len(words) - len(st) + 1):
			m = i
			fg=0
			for k in range(0,len(st)):
				if(words[m] != st[k]):
					fg=1
					break
				m=m+1
			if(fg == 0):
				cn=cn+1
	return cn
print('Prediction of occurence of word in a given trigram')
val = input('Enter the sentence\n')
words = val.split(' ')
if(len(words) <=2):
	print('Trigram model would not predict for sentences having length less than three')
	sys.exit(0)
cal = dict()
word_space=[]
k=-1
for word in words:
	k=k+1
	if(word.strip() == ''):
		continue
	else:
		word_space.append(word)
print(word_space)
text=open('transcript.txt','r')
st=[]
res=1.000
st.append(word_space[0].lower())
st.append(word_space[1].lower())
for i in range(2,len(word_space)):
	text=open('transcript.txt','r')
	tmp=text
	k = count(st,tmp)
	st.append(word_space[i].lower())
	text=open('transcript.txt','r')
	tmp=text
	k1=count(st,tmp)
	if(k1==0 or k == 0):
		res=0
		break
	print(k1,k)
	ans=k1/k
	res=res*ans
	st.pop(0)
#print(words)
print('The probability of occurence of the given string is - ')
print(res)
