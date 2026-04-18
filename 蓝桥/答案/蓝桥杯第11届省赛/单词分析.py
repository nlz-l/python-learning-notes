#ddccbba
word=list(input())
ans=sorted(sorted(word),key=lambda x:word.count(x),reverse=True)[0]
print(ans)
print(word.count(ans))