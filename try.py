import random
a=input("Are you ready for a game of Hangman?[Yes/No]: ")
def find(a,b):#for is just for comparision sake , to check is our list r is equal to k
    if a == b:
        print("YOU HAVE DEFEATED ME , WELL DONE MY FRIEND")
        return 1
    else:
        return 0
def check(a,b):#two values will be receieved here a and b , from line 30 basically list k and ' '
    indices=[]
    for k ,c in enumerate(a): #enumerate basically is a tuple with indices and value  , so is our list was [0,1,0] , enumerate would make it like ((0,0),(1,1),(2,1))
        if c == b:#k value from above will be our index and our c value will be the letter , this just compares with our argument b which we passed through
            indices.append(k)
    return indices
if a.lower()=="yes":
    i=input("Select a topic:[Movies, Games, Places, Celebrities, Books]: ")
    m=['Spider-Man','Iron Man','Titanic','Avatar','The Matrix','John Wick','The Avengers','The Batman','The Super Mario Bros.','Puss in Boots: The Last Wish','Minions','Wreck-It Ralph']
    g=['Fortnite','PUBG','Valorant','Batman Arkham Knight','Red Dead Redemption 2','The Last of Us','Dying Light',"Assassin's Creed",'DOOM','Grand Theft Auto','Tomb Raider','Halo']
    p=['Dubai','Paris','Tokyo','Berllin','London','Mumbai','New Delhi','Hong Kong','Thailand']
    c=['Ronaldo','Messi','Leonardo DiCaprio','Johnny Depp','Kylie Jenner','Roger Federer','Kanye West','Neymar','Lebron James','Dywane Johnsson','Howard Stern']
    b=['The Diary of a Wimpy Kid','The Great Gatsby','The Catcher in the Rye','To Kill a Mockingbird','The Lord of the Rings','Invisible Man','Great Expectations',"Harry Potter and the Philosopher's Stone","Gulliver's travels"]
    v1=random.choice(m)
    v=v1.lower()
    w1=random.choice(g)
    w=w1.lower()
    x1=random.choice(p)
    x=x1.lower()
    y1=random.choice(c)
    y=y1.lower()
    z1=random.choice(b)
    z=z1.lower()
    k=list(v)#we covert to list for comparision later on
    r=[]
    if i.lower()=="movies":
        print("Your word is so length in a programmers way ,starting from 0 :) is :",len(k)-1)
        s1=len(k)#finding the length of our list to multiply with *
        k1='*'*s1 #multiples * with the number of letters in the word , * acts as unknow value
        r=list(k1) #coverts it to a list
        m1=check(k,' ') # check for specific value in our list and returns list of all indices with that specific value
        m2=check(k,'-')#calls the check function which is defined on top (line 3)
        m3=check(k,':')
        m4=check(k,'.')
        if m1!=[]: #iniciates only if value is found and list is returned
            for i in m1: # for the number presents in list , we pop the * with the index then insert the value in that specific place
                r.pop(i)
                r.insert(i,'_')
        if m2!=[]:
            for i in m2:
                r.pop(i)
                r.insert(i,'-')
        if m3!=[]:
            for i in m3:
                r.pop(i)
                r.insert(i,':')
        if m4!=[]:
            for i in m4:
                r.pop(i)
                r.insert(i,'.')
        x1=check(k,'a') # this checks for vowels and does the same thing
        x2=check(k,'e')
        x3=check(k,'i')
        x4=check(k,'o')
        x5=check(k,'u')
        if " " in k: # this just checks for value and replaces space with '_'
            a=k.index(" ")
            k[a]="_"
        if x1 !=[]:
            for i in x1:
                r.pop(i)
                r.insert(i,'a')
        if x2 !=[]:
            for i in x2:
                r.pop(i)
                r.insert(i,'e')
        if x3 !=[]:
            for i in x3:
                r.pop(i)
                r.insert(i,'i')
        if x4 !=[]:
            for i in x4:
                r.pop(i)
                r.insert(i,'o')
        if x5 !=[]:
            for i in x5:
                r.pop(i)
                r.insert(i,'u')
        print(" Your initial guess word is: ('_' indictaes spaces)")
        for i in r:#for each element in list r , it prints that elements with each element close by
            print(i,end=" ")
        print("LETS BEGIN")
        sq=0
        n2=0
        sq1=0
        while sq < 6:
            g= find(r,k)
            if g == 1:
                sq = 3
                print("YOU HAVE COMPLETED THE GAME WITH:",6-v,"lifes")
                break
            if n2 >=3:
                sq+=1
                sq1+=1
            if n2>0:
                print("Your seriously wanna waste those chances ,smh ",'\n')
            if sq == 0:
                print("6 LIVES",'\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f'," ",'\u2764\ufe0f')   
            if sq == 1:
                print("GOTCHA SUCKER,5 MORE TO GO",'\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f',u"\U0001F90D")
            if sq == 2:
                print("ANOTHER ONE BITES THE DUST, 4 MORE ",'\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f'," ",u"\U0001F90D",u"\U0001F90D")  
            if sq ==3:
                print("THIRD TIMES THE CHARM , 3 MORE",'\u2764\ufe0f','\u2764\ufe0f','\u2764\ufe0f'," ",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D")
            if sq==4:
                print("STRIKE THREE , 2 MORE :)",'\u2764\ufe0f','\u2764\ufe0f'," ",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D")
            if sq == 5:
                print("OHOH HERE WE GO , LAST LIFE , TO CLUTCH OR NOT TO CLUTCH",'\u2764\ufe0f'," ",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D")
            n1=str(input("Enter your letter:"))
            if len(n1)>=2 and n1.isalnum():
                sq+=0
                sq1+=0
                n2+=1
                print("What does a letter refer to my friend",'\n')
            if n1.isalnum() == False:
                sq+=0
                sq1+=0
                n2+=1
                print("Do you not understand the meaning of letter?",'\n')
            if n1.isalnum() == True and len(n1)==1:
                if n1 in k:
                    check1=check(k,n1)
                    n2+=0
                    for i in check1:
                        r.pop(i)
                        r.insert(i,n1)
                        sq+=0
                        sq1+=0
                    print("Your word is as stands")
                    for i in r:
                        print(i,end=" ")
                    print('\n')
                if n1 not in k:
                    sq+=1  
                    sq1+=1
                    n2+=0    
        if sq == 6:
            print("TO NOT CLUTCH IT IS , IMAGINE NOT GETTING IT",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D",u"\U0001F90D")
            print("IF YOU MUST KNOW , YOUR MOVIE WAS:", sq1)
    
    elif i.lower()=="games":
        print (w)
    elif i.lower()=="places":
        print (x)
    elif i.lower()=="celebrities":
        print (y)
    elif i.lower()=="books":
        print (z)
