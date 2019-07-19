number=[str(i) for i in range(1,11)]
letter=["a","b","c","d","e","f","g","h","i","j"]
mix1=[[i+j for i in number] for j in letter]
mix2=[[j+i for i in number] for j in letter]
new1=[]
new2=[]
for i in range(0,3):
    for k in range (0,3):
     new1.append(mix1[i][k])
     new2.append(mix2[i][k])
print("1.",sorted(new1),"\n","2.",sorted(new2),sep="")

