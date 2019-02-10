
a=open('check.json','r') #given file


t=open('pro11.txt','a') # tweet file
s=open('pro21.txt','a') # in lower case


e=open('stop.txt','r') # stopper file
fi=open('pro31.txt','a') # except stopper

str3=''
str5=''
str6=''
str9=''
for i in a:

    str1=i
    l=len(str1)-1
    l1=str1.find('text')
    l2=str1.find('source')
    l1=l1+4
    #str2=str1[l1]
    #str3=str1[l2]
    #for j in range(0,25):
     #   for str2 in str3:
     
    str3=''     
    for j in str1[l1:l2]:
        if (ord(j) > 64 and ord(j) < 91) or (ord(j) > 96 and ord(j) < 123):
            str3+=j
            
            
        elif j== ' ':
            str3+=j
    t.writelines(str3)
    t.writelines('\n')
        
            
    #print l1
    #print l2
  #  print str3
    #br
    
t=open('pro11.txt','r')

for gg in t:
    str1=gg.lower()
    s.writelines(str1)


str11=''    
for k in e:
    str11+=k
#print str2
st3=str11.split()
#print str3
len1=len(st3)-1
#print len1






s=open('pro21.txt','r')
e=open('stop.txt','r')

for l in s:
    #print 'world'
    st4=l.split()

    for m in st4:
        co=0
        for n in range (0,len1):
            
            #print 'era'
            #print str3[len1]
            if(st3[n]!=m):
             #   print 'n'
              #  print n
              #  print 'str3[n]'
              #  print str3[n]
              #  print 'm'
              #  print m
                co=co+1
              #  print 'co'
              #  print co
                
                
                if(co==(len1)):
         #          print 'not in other'
                    fi.writelines(m)
                    fi.writelines(' ')
                    
    fi.writelines('\n')

    print st4
fi=open('pro31.txt','r')
f=open('fout1.txt','a') # final output file
for k in fi:
    str5=''
    str5+=k
    str10=str5.split()
    len1=len(str10)
    for n in str10:
        if(len(n)<11):
            f.writelines(n)
            f.writelines(' ')
    f.writelines('\n')


            
  
a.close()
t.close()
s.close()
f.close()
e.close()
fi.close()

