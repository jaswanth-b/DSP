from matplotlib import pyplot as py
x=[1,2,3,4,5]
y=[]
sum=0
for i in x:
    sum=sum+i
    y.append(sum)
py.plot(x,y)
py.show()