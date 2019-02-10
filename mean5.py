a=open('fout1.txt','r') 
b=open('AFINN-111.txt','r') #afinn file
c=open('fout23.txt','a') # number file
d=open('FinalResult.txt','a') # actual meaning

for i in a:
    str1=0
    str1=i.split()
    
    for j in str1:
        b=open('AFINN-111.txt','r')
        
        for k in b:
            str2=0
            str2=k.split()
            # print str2
            if(str2[0]==j):
                #print str2[0]
                #print str2[1]
                if j=='messing':
                    str7=str2[2] 
                else: 
                    str7=str2[1] 
                c.writelines(str7)
                c.writelines(' ')
    c.writelines('\n')
c=open('fout23.txt','r')
for n in c:
    m=n.split()
    sum1=0
    sum1=int(sum1)
    for l in m:
        
        l=int(l)
        sum1=int(sum1)
        sum1=sum1+l
        #sum1=int(sum1)
    if(sum1==0):
        d.writelines('neutral')
        d.writelines('\n')
    elif(sum1>0):
        d.writelines('+ve')
        d.writelines('\n')
    else:
        d.writelines('-ve')
        d.writelines('\n')
        
a.close()
b.close()
c.close()
d.close()
