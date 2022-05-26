import random as rnd
a=[i for i in range(1,14,1)]
b=[j for j in range(1,14,1)]
c=[k for k in range(1,14,1)]
d=[l for l in range(1,14,1)]
f=a+b+c+d
playerA=[]
playerB=[]
Round=[]
count=0
for j in range(0,1000,1):
      x=1
      
      for i in range(0,52,1):
            x=rnd.randrange(51)
            f.append(f.pop(x))

      for i in range(0,52,2):
            playerA.append(f[i])
      
      for i in range(1,52,2):
            playerB.append(f[i])

      
      DeskofA=[]
      DeskofB=[]
      
      while playerA and playerB:
            initialcardofplayerA=playerA.pop()
            initialcardofplayerB=playerB.pop()
            if initialcardofplayerA==initialcardofplayerB:
                  DeskofA.extend([initialcardofplayerA]+playerA[-3: ])
                  playerA=playerA[ :-3]
                  playerA.append(DeskofA.pop())

                  DeskofB.extend([initialcardofplayerB]+playerB[-3: ])
                  playerB=playerB[ :-3]
                  playerB.append(DeskofB.pop())
            elif initialcardofplayerA>initialcardofplayerB:
                  
                  playerA=[initialcardofplayerA,initialcardofplayerB]+DeskofA+DeskofB+playerA
                  DeskofA=[]
                  DeskofB=[]
            elif initialcardofplayerB > initialcardofplayerA:
                  playerB=[initialcardofplayerB,initialcardofplayerA]+DeskofB+DeskofA+playerB
                  DeskofA=[]
                  DeskofB=[]
            x=x+1
     
      Round.append(x)
      
      if (len(playerA)==0):
            
            count=count+1
            
      

      x=0
     
      playerA=[]
      playerB=[]

print("Player B will win the match",count,"times")
"""                  
x=1
DeskofA=[]
DeskofB=[]
while playerA and playerB:
      initialcardofplayerA=playerA.pop()
      initialcardofplayerB=playerB.pop()
      if initialcardofplayerA==initialcardofplayerB:
            DeskofA.extend([initialcardofplayerA]+playerA[-3: ])
            playerA=playerA[ :-3]
            playerA.append(DeskofA.pop())

            DeskofB.extend([initialcardofplayerB]+playerB[-3: ])
            playerB=playerB[ :-3]
            playerB.append(DeskofB.pop())
      elif initialcardofplayerA>initialcardofplayerB:
            playerA=[initialcardofplayerA,initialcardofplayerB]+DeskofA+DeskofB+playerA
            DeskofA=[]
            DeskofB=[]
      elif initialcardofplayerB > initialcardofplayerA:
            playerB=[initialcardofplayerB,initialcardofplayerA]+DeskofB+DeskofA+playerB
            DeskofA=[]
            DeskofB=[]
      print(x,len(playerA),len(playerB))
      x=x+1
            
      
     
d=playerA.pop(len(playerA)-1)
print(playerA)
print(playerA.pop())
"""
