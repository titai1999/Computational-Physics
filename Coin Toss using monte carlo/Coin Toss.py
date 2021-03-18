
import random as rnd #(taking the library which will generate the random no)
n=100 #(taking the no of points)
j=0
s=0.0
i=0.0
xx=[0.0]*n #(creating an array of 100 elements)
while j<n:
      n1=0
      np=50
      i=0.0
      while i<np:
            x=rnd.random() #(we will get random no in a range 0 to 1)
            i=i+1
            if x<=.5:
                  n1=n1+1
      xx[j]=n1#(in this array we are going to store the no of favourable output after 50 coin toss)
      s=s+xx[j]
      j=j+1
av=s/(n*50)#(here we are taking the probability that total no to favourable output/total no of events)
print ("the probability is",av)
