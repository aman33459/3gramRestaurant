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
def totalvocab(text):
    text=open('transcript.txt','r')
    words=text.read()
    k= len(set(words.split()))
    #print(k)
    return k

def count1(s , text):
    text=open('transcript.txt','r')
    words = text.read()
    cn=0
    #print(words)
    #print(len(words.split()))
    for word in words:
       # print(word)
        if(s.lower() == word.lower()):
            cn+=1
   # print('***')
    #print(cn / len(words.split()))
    return (cn+1)/(len(words.split())+totalvocab(text))

def count2(s1,s2):
    text=open('transcript.txt','r')
    words=text.read()
    cn = 0
    for word in words:
        if(word.lower() == s1.lower()):
            cn+=1
    text=open('transcript.txt','r')
    words=text.read()
    cn1=0
    for word in range(0,len(words)-1,2):
        if(words[word].lower() ==s1.lower() and  s2.lower()==words[word+1].lower()):
            cn1+=1
    return (cn1+1)/(cn+totalvocab(s1))

print('Prediction of occurence of word in a given trigram')
val = input('Enter the sentence\n')
words = val.split(' ')
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
v= totalvocab(text)
st.append(word_space[0].lower())
st.append(word_space[1].lower())
res = res * count1(word_space[0] , text)
res = res * count2(word_space[0], word_space[1])
for i in range(2,len(word_space)):
	text=open('transcript.txt','r')
	tmp=text
	k = count(st,tmp)
	st.append(word_space[i].lower())
	text=open('transcript.txt','r')
	tmp=text
	k1=count(st,tmp)
	#print(k1,k)
	ans=(k1+1)/(k+v)
	res=res*ans
	st.pop(0)
#print(words)
print('The probability of occurence of the given string is - ')
print(res)
