import matplotlib.pyplot as plt

def hist():
    activities=[]
    positive=0
    negative=0
    neutral=0
    neutral=int(neutral)
    positive=int(positive)
    negative=int(negative)
   
    f=open('FinalResult.txt','r')
    li=[]
    for i in f:
        li.append(i)

    print li[2]
    print li[3]

    for i in li:
        if i=='neutral\n':
            neutral=neutral+1

        if i=='+ve\n':
            positive=positive+1

        if i=='-ve\n':
            negative=negative+1

    print positive,negative,neutral

    slices=[neutral,negative,positive]
    
    activities=['Neutral','Negative','Positive']
    cols=['c','m','r','k']

    plt.pie(slices, labels=activities, colors=cols ,shadow=True , autopct='%1.1f%%')
    plt.title('Pie chart')
    # plt.legend()
    plt.show()



hist()


