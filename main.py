
#                                  "list"
#                   $$$$$$$$$ --------------- $$$$$$$$$$$$

'''d=100
y="bike"
del d
print(y)
print(d)

m=int(500)
n=str(500)
o=float(500)
print(m,n,o)

a=5
b='SHOP'
c=32.5
print(type(a))
print(type(b))
print(type(c))

x=y=z='himalaya'
print(x,y,z)

x='tirupur'
y='avinasi'
z='poondi'
del(y)
print(x,z)

x='-god'
y='-is'
z='-great'
print(x+y+z)


x=5555
y=2222
z=9999
print(x+y+z)

v=5.2
b='jonson'
print(str(v),b)


a=6000
print(a)
def myfunction():
    global a
    print(a)
    a="changeingnow"
myfunction()
print(a)


a=1
b=255555
c=-2000
print(type(a))
print(type(b))
print(type(c))

x=1.10
y=1.0
z=-20.30
print(type(x))
print(type(y))
print(type(z))


p=3+5j
s=6j
y=7j
print(type(p))
print(type(s))
print(type(y))

mt1=20
print(mt1,"life is game",type(mt1))
ktm2=55.5
print(ktm2,"gamerslink",type(ktm2))
duke3=55.2j
print(duke3,"bitcain",type(duke3))

#this is change the type coretly


 a=65
b=22.2
c=55j

d=complex(a)
o=int(b)
n=float(a)
print(d,o,n)

#any numbers random print here this is random

import random
print(random.randrange(1,50))

import math           #this is math roots of python

print(math.pi)
print(math.cos(1.2))
print(math.exp(33))
print(math.log10(10000))
print(math.sinh(65))
print(math.factorial(2))

#  d=decymel.... o=octimal...  x=xeha decymel.....

print(0b1101010)
print(0o50)
print(0xAB+0b10)

ages=[19,22,18]
print(ages)

# any element for accept here for list concept

list1=[55,"dai",22.45,"dai"]
list2=["manoj",5,88.8,"hello"]
list3=[]
print(list1)
print(list2)
print(list3)

# this ex: for used to array concept this is -learn too [0,1,2,]....

bank=['htfc','iob','sbi']
print(bank[2])
print(bank[0])

# that - level that start in[-1,-2,-3]

bank=['htfc','iob','sbi']
print(bank[-2])
print(bank[-0])

# this is slicing of using before one letter or one number-------------------------------------

my_list=['h','u','m','a','n','b','e','i','n','g']
print(my_list[2:5])
print(my_list[5:])
print(my_list[:])


#  this is add element to a list in (append method)-----------------------------

numbers=[21,22,23,24,25,26]
print(numbers)
numbers.append(27)
numbers.insert(2,20)
print(numbers)

#this ex: for numbers or alternative but use(extend) next upend for this..-------------------

numbers=[1,2,3]

even_numbers=[4,5,6]
numbers.extend(even_numbers)
print(numbers)'''

# this is change for array concept[0,1,2]...--------------------------

'''languages=['python','c','c++']
languages[0]='mango'
print(languages)'''

# this is remove an item for list ......-----------------------------------

'''cars=['maruthi','swift','alto','benz','rools','800']
del cars[1]
print(cars)
del cars[-1]
print(cars)
del cars[0:2]
print(cars)'''

# this is true or false in list:    ........----------------------------

'''sports=["volleyball","foodball","hocky"]
print("tenish"in sports)
print('hocky'in sports)'''

# this is find the -lenth in list:  .....------------------------------

'''lesson=['tamil','english','maths']
print('list:',lesson)
print(len(lesson))

birthday=[n**2 for n in range(1,6)]
print(birthday)'''
#-----------------------------------------------------------------
'''numbers=[]
for n in range(1,5):
    numbers.append(n*4)


print(numbers)'''
#-----------------------------------------------------------------



#                                   ""TUPLE""
#                     &&&&&&&&&&&---------------&&&&&&&&&&&&&



# create tuple with one item .........--------------------

'''area=('karthi')
print(type(area))
area=("karthi")
print(type(area))

# tuple value change then after "list".....---------------

a=("karthi","mithun","sanjay")
b=list(a)
b[2]='vicky'
a=type(b)
print(a)

# that is tuple to tuple (+)....---------------

shop=('medical','bakery','saloon')
hospital=('reavathi')
shop+=hospital
print(shop)

# unpaking a tuple element...----------

data=('mother','father','sister')
(tintin,jooly,haripater)=data
print(tintin)
print(jooly)
print(haripater)

# asterisk :  for tuple concept....................................

home=("inset","design","record","review","help")
(book,note,*pen)=home
print(book)
print(note)
print(pen)

# same concept for asterisk:  ...........................................

home=('inset','design','record','review','help')
(book,*note,pen)=home
print( book , note , pen )

# join two tuple ,..............................................

point1=('A','B','C')
point2=(1,2,3,4)
point3=point1+point2
print(point3)
print(point1)

# there tuples ARE MULTIPLE here.................-----------

collage=('avs','mnp','psg','ghh')
student= collage    *3
print(student)

#  count method for tuple ............---------

theatre=(1,2,3,4,5,6,7,8,9,10)
x=theatre.count(5)
print(x)

# index method for tuple ...............

theatre=(1,2,3,4,5,6,6,6,)
x=theatre.index(6)
print(x)

# THIS CONCEPT FOR: (ALL) IN TUPLE.......-------------------

a=(5,4,0,2,3,1,False)
print(all(a))
a=()
print(all(a))

s=(2,4,6,8,10,11)
print(all(ele % 2 ==0 for ele in s))

# this concept for: (any) in tuple................-----------------

gw=(5,6,9,8,0,False)
print(any(gw))
sg=(0,False)
print(any(sg))

# this concept for: (sorted) in tuple ...............------------------

a=[2,6,5,7,9,8,9]
print("sorted list returned:",sorted(a))
print("Reverse sort:",sorted(a,reverse=True))

#this is (sum),(max),(min) that is maths concept...........-------------

g=(4,5,8,7,9,)
print(sum(g))
print(max(g))
print(min(g))'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  "SET"
#                 &&&&&&&&&&&------------------&&&&&&&&&&&&

#                    "EVERYONE  SHOULD LEARN HOW TO CODE,,
#                       IT TEACHES YOU HOW TO THINK"


'''mano=set(("cars","bikes","autos",))
mylist=["brother","sister"]
mano.update(mylist)# (list) and (tuple) add to set (datas)..........-----
tintin={"man","women","son"}
tintin.update(mano)
danger=mano.pop()#(pop) that is select the any (one) varient in data........
mano.remove("bikes")
mano.discard("autos")                    # discard  &  remove are delet (set datass)............------
mano.add("buses")                        # this is add to set datas...........-----------

print(mano)
print(danger)
print(mano)
print(tintin)
print(mano)

# this is  (clear) keyword used to clear (set (datas) )...............--------

horse=set({"is","was","that"})
horse.clear()
print(horse)           # that is clear to ( set) value .........--------

# this (output) (are) name "buuls" is  not difined .........----

bulls={"are","you","there"}
del bulls
print(bulls)

#  ...........     (update) and (union)  ......

mano={"hi","my","by"}
mano1={"77","66","55","55"}
print(mano1)
mano.update(mano1)
mano2=mano1.union(mano)
print(mano2)
print(mano)

#  two different veriable that's (same word) (print) here keep only tha duplicates .....................


z={"parrot","pecock","owal"}
x={"hight","wight","parrot"}
z.intersection_update(x)
print(z)

# keep all but not the (duplicates) (accept) here ..................---------------

o={"choto","beem","kaliya","55"}
p={"21","55","21"}
s=o.symmetric_difference(p)
print(s)

#  (copy)  method used here ............--------------

nuts={"milk","dates","grapes"}
kids=nuts.copy()
print(kids)

#   (difference)  method used here... (difference between same word remove here)...............-------------

a={"call","lal","55","hight","mall"}
b={'call',"belt","55","girls","lal"}
c=a.difference(b)
print(c)

#   (isdisjoint) method used here that's used to (true) or (false) .............---------

hey={"pop()","set","list","50","60",}
hey1={"jump","bunk","jolly",'40','70'}
hey2=hey1.isdisjoint(hey)
print(hey2)

#  (issubset) method used here this is used to issubset meens one data is small from another data (big data), small data is all are present in big data

dad={"a","b","c","d"}
dad1={"m","n","o","p","a","b","c","d"}
dad2=dad.issubset(dad1)
print(dad2)


  # (issuperset) method here (output) is false............-----

m={"girl","boy","son","dad"}
n={"5","6","2",}
g=m.issuperset(n)
print(g)'''


#                                         "DICTIONARY"
#              @@@@@@@@@@@@@@@@@@@@@@-----------------------@@@@@@@@@@@@@@@@@@@@@@@

# 1:  dictionary are used to store data values in key:value pairs......do not allowed duplicate
# 2:   changeable   ( duplicate values will overwrite  existing value:

'''hostel={"boys":"volleyball","girls":"handball","teachers":"warden","teachers":"warden"}
print(hostel["boys"])
print(hostel)'''

# dictionary  item --  data type :........-----

'''teem={"coach":"players","canteen":"master",
"school":["teachers","staff","principal"]}
random=({"55","66","77","88","99"})
random.remove("66")
print(teem)
a=teem["school"]           #.....(dict) by then used to [list]   and   {set}........
print(a[2])
print(random)'''

# (DICT() CONSTRUCTOR)............-----
#  (dict) used to then after any variable put here but out put is (dict).....
'''morwell=dict(a="manoj",b="50",c=["tiruppur","poondi"])
d=morwell["c"]
print(d[1])
print(morwell)'''

# ....gets (keys())........and......gets (value()).........----------------

'''bakery={"bun":"jam","tea":"bisket","sweet":"laddu"}
dai=bakery.keys()
print(dai)
hi=bakery.values()            # there bakery-keys & bakery-values are output here....
print(dai)
print(hi)    # here used (values) are for (keys)&(values)&(add) values & (add) keys.........---
g=bakery.keys()
m=bakery.values()
bakery["juice"]="lemon"
bakery=do=["mo"]
print(g)
print(m)'''

# here used for (item()) this used to total values & keys are show the result here .........----

'''viswas={"beer":"shotch","wine":"bottle","juice":"glass"}
hotel=viswas.items()
print(hotel)'''

# check the (keys)  in variable  here me yes meens print(f) no meens print (else)............

'''area={"boys":"freefire","mens":"pubg","uncle":"candy_crush"}
if"mens" in area:
    print(" yes , 'mens' is here ")
else:
    print(" 'mens', (keys) or not here ")'''


# change values use ( update) variable here ........-------

'''iact={"subhi":"5001","tect":"2500","develop":"boy"}
iact.update({"subhi":"6000"})
iact["tect"]= 3000
print(iact)'''

# adding items  and change tha new kyes & values adding here ........---------

'''m={"the":"55","she":"65","me":"77"}
m["he"]="88"
print(m)'''

# ubdate the new sentance in add keys & values. and use the ((pop)) variant used for select the variant remove here  ...............---------

'''hostel={"boys":"volleyball","girls":"handball","teachers":"warden","teachers":"warden"}
hostel.update({"ground":"balls"})
hostel.pop("girls")
print(hostel)'''

# (popitem) use for in last variant remove here ...........-----------

'''bakery={"bun":"jam","tea":"bisket","sweet":"laddu"}
bakery.popitem()
print(bakery)'''

# here used variant for (del)  &  (clear)...  (del) used to delete (1)  variant .....(clear) used to delete (total) variants ..........------

'''lol={"kee":"55","mee":"77","see":"33"}
del lol["kee"]
print(lol)
lol.clear()
print(lol)'''

# here doing (for) looping concept......... out put was 3 keys value show now ...........-------

'''bea={"friend":"45","mom":"85","dad":"33"}
for m in bea:
    print(m)'''

#  values()  .... method _________print all values ..................----------

'''a={"hey":"5","call":"6","bun":"3"}
for x in a.values():
    print(x)'''

# keys() ... method use for print all keys values ..............----------

'''nun={"a":"fight","b":"mano","c":"kolam"}
for x in nun.keys():

    print(x)
for y in nun.values():
        print(y)'''

# this looping concept used to both (keys()).....and ....values()),by using the (item()),method.........---------

'''a={"hi-":"55","my-":"88","fi-":"44"}
for x,y in a.items():
    print(x,y)

# copy method ..........

red={"yellow":"45","black":"78","orange":"12"}
del red ["yellow"]
hi=red.copy()
print(hi)

#......same concept copy method .....................................

red={"yellow":"45","black":"78","orange":"12"}
dai=dict(red)
print(red)

# (nested) (dict)       ..... can use for total variable show the print ...........-----

color={"white1":{"name":"manoj","year":"2001"},
        "white2":{"name":"karthi","year":"2003"},
        "white3":{"name":"mithun","year":"2004"}
      }
print(color)

#  ..........same concept........

lolipop1={"name":"manoj","year":"2001"}
mango2={"name":"karthi","year":"2003"}
apple3={"name":"mithun","year":"2004"}

wonderfull={
    "lolipop1":lolipop1,"mango2":mango2,"apple3":apple3}

print(wonderfull)

# *******************  same concept *******************

quite={ "white1":{"name":"manoj","year":"2001"},
             "white2":{"name":"karthi","year":"2003"},
             "white3":{"name":"mithun","year":"2004"}
           }

print(quite["white2"]["name"])

# setdefault().... this work for difined comend in tha variable print as that but no not variable here your own commend print here  ....................

hostel={"boys":"55","girls":"66","teachers":"80"}
dai=hostel.setdefault("boysd","horse")
print(dai)

# this usage for ( fromkeys )  this work are 2 variable (add) and show them print ........


x = ('sanjay', 'karthi', 'ashok')
y = "benily"

manoj= dict.fromkeys(x, y)
print(manoj)'''


#                                   "..operators.."
#   $$$$$$$$$$$$$$$$$$$$$$$$$$$$_____________________________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# .........ARITHMETIC OPERATORS.........

'''a=10
b=5
print(a+b)       # +	Addition
print(a-b)       # -	Subtraction
print(a*b)       # *	Multiplication
print(a/b)       # /	Division
print(a%b)       # %	Modulus
print(a**b)      # **	Exponentiation
print(a//b)      # //	Floor division
delet'''

# ... ASSIGNMENT OPERATORS..........

'''x=10
print(x)
x=x+3
print(x)
x=10
x=x-3
print(x)
x=10
x=x*3
print(x)
x=10
x=x**5
print(x)
x=138
x=x/7
print(x)
x=138
x=x%7
print(x)
x=138
x=x//7
print(x)
x=10
x=x&6
print(x)
x=10
x=x|6
print(x)
x=10
x=x>>2
print(x)
x=10
x=x<<6
print(x)'''


#.. LOGICAL OPERATORS ..........<<<<<<<<<<........

'''x = 10
print(x > 9 and x < 11)  		#True
print(x > 5 or x < 11)     		#True
print(not (x > 5 and x < 11) )	#True'''

#..........Python Identity Operators..........

'''mano1 =["Python","Java","MongoDB"]
mano2 = ["Python","Java","MongoDB"]
mano3=  mano1
print(mano1 is mano3)
print(mano1==mano2)'''

# ........... python identity operaters   ( is not ) typical .............

'''mano1 =["Python","Java","MongoDB"]
mano2 = ["Python","Java","MongoDB"]
mano3=mano1

print(mano1 is not  mano3)
print(mano1 is not mano2)
print(mano1 != mano2)'''

# .... python membership operaters.....

'''mano =["car","bike"]
kumar=["moto","handle"]
print("kumar" not  in  mano)

#  python bitwise operater

a=["horse","beach","500"]
b=["local","area","200"]
print()'''

#  ......Operator Precedence this work for step by step for 

'''kenda= ((7+5*6)-(6+3-1))
print(kenda)'''

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




#                             " PYTHON FOR LOOPING CONCEPT "
#         *****************....................................*********************



# pytho if...else... condition...

'''a=50
b=30
if b>a:
  print("b is greater then a ")
else:
    print("fail")'''

# .... concept for (( "elif" )).....

'''m=45
n=55
if m>n:
    print("n is greater then a")
elif m==n:
    print("a and b are  equal")
else:
    print("this condition pass")'''

# condition for ("else")........................--------------------------------------------

'''di=200
he=200
if he<di:
    print(" if conditon pass ")
    print("dai")
elif di==he:
    print("codition fail so print elif")
else:
    print("condition fail so print else")'''

# short cut of (print if condition).............------------------------

'''a=66
b=33
if a<b:print("a is  greater then b")
else:
    print("condition fail so print else")'''

# short cut of (if else condition)...........------------------------

'''a=500
b=300
print("if pass") if  a>b  else print("else pass")'''

# ........ condition for ( AND )...................----------------

'''a=700
b=600
c=500
if  a>b and  c>a:    #  .. (AND).. WORK IS BOTH CONDITION IN TRUE THAT HAS PRINT TRUE :...BUT ANY ONE CONDITION FAIL THAT HAS PRINT FALSE:.........--------
    print(" both are true")
elif a>b:
    print("2 condotion are fail so print elif ")'''

# ..... CONDITION FOR ( OR CONDOTION ) ....

'''a=500
b=400         #..... (OR) work has any one condition pass ..that print true :..any one codition fail then print true....:
c=300              # two condition fail then print fail:..........-----------
if a>b or c>a:
    print("if condition pass")'''

# ..... this is alternative print condition for (NOT)...that work has  [true then false],,[false then true]...............------

'''a=5
b=3
if not a<b:
    print("condition fail ")'''

# condition for (nested if) this use for 2 if condition first condition pass then print but fail go to the 2nd if............---------
#                 ============
'''a=55
if a<20:

      if a<10:
        print("second condition pass  ")
      else:
         print("2 condition fail")
else:
      print("first condition fail")'''


# THAT IS PASS STATEMENT :  ......................----------------------------------------

'''a = 55
b = 500
                 # just (pass) condition put there after run tha progaram ;;;
if b > a:
   pass'''
#                     <<<<  looping  >>>>

#  python lopp condition : while & for loops here :...........---------------

#  ::::: while loop condition ........------------------

'''i=5
while i<50:
    i += 1
    print(i)'''

# break statement condition for [ break ]...................----------

'''i = 1
while i<5:
    print(i)
    if i == 3:
     break
    i += 1
else:
    print("condition pass")'''

# continue statement for looping concept............-----------------------

#With the continue statement we can stop the current iteration, and continue with the next:

'''i = 1
while i < 7:
  i += 1
  if i == 4:
   continue    # Note that number 3 is missing in the result
  print(i)'''

#  that is (else) statement ..........-------------------


'''i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("while condition pass")'''

# FOR LOOP CONCEPT ..............-------------------

'''manoj=["police","army","it"]
for x in manoj:
    print(x)
for x in "army":
    print(x)'''

# break statement : for looping concept...........----------------

'''manoj=["police","army","it"]
for x in manoj:
    print(x)
    if x == "army":
     break'''

#............................................................................


#  new project : ............-------------------


'''list1=[1,2,3,4,5,6,7,8,9,10]
list2=[5,6,7,8,9,10]
resultlist=[]
for data in list1:
    if data not in list2:
        resultlist.append(data)
print(resultlist)'''


#                               {{"""  PYTHON FUNTION'S  """}}
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{!!!!!!!!!!!!!!!!!!!!!!!!!!!!}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


'''def sap(xz):
    list=[]
    for i in xz:
        list.append(i)

    final=sum(list)
    return final
dic={'a':100,'b':200,'c':300}
apple=(1,2)
horse=(50,60)
print(sap(apple))'''

# _____________________________________________________________________________

'''def duplicate(do1,do2):
       danger= ("IACT")
       for x in do1:
         for y in do2:
            if x==y:
               quite=("subi")
               return quite

       return danger

#a=[1,2,3,4,5]
#b=[1,2,3,4,5]
#print(duplicate(a,b))

a=[11,22,33,44]
b=[55,66,77,88,11]
print(duplicate(a,b))'''

#___________________________________________________________________________________

'''store="Tiruppur"
book=[]
for pen in store:
       if pen not in book:
           book.append(pen)

print(book)'''

#-----------------------------------------------------------------------------------------

''''def find_common(list1,list2,list3):
           common=set()
           for elem  in list1:
              if elem in list2 and elem in list3:
                 common.add(elem)
           return common

list1=[1,5,10,20,40,80]
list2=[6,7,20,80,100]
list3=[3,4,15,20,30,70,80,120]

common = find_common(list1,list2,list3)
print(common)'''

#--------------------------------------------------------------------------------------

'''good1=[10,15,20,30,35,40,]
good2=[25,35,40]

habit3=[]
for element in good1:
    if  element not in good2:
          habit3.append(element)

print(habit3)'''

#---------------------------------------------------------------------------------------


'''good1=[10,15,20,30,35,40,]
good2=[25,35,40]

cat=set(good2)
hello3=[x for x in good1 if x not  in cat]
print(hello3)
print(cat)'''


#------------------------------------------------------------------------------------

'''a=int(input("enter tha first number:"))
b=int(input("enter tha second number:"))
c=int(input("1.add 2.sub 3.multiple 4.divition : "))

if c==1:
     z=a+b
     print("output",z)
elif c==2:
     g=a-b
     print("output",g)
elif c==3:
     k=a*b
     print(k)
elif c==4:
       w=a%b
       print(w)

else:
      print("check your input")
a=10
b=15
print(type(b))



def holiday(a, b):
    if a == b:
        c = "sorry"
        return c
print(holiday (int(input()),int(input())))'''


#                                     :::", STRING INTRODUCTION ,":::
# ....,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,..,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.

'''a="hello world"
print(a)
print(a[0],a[2],a[8],a[10],a[-1])'''

#...........------------------------------------------------------------------.........-----....----...

'''a="manojkumar"
print("A")          ''' # one letter or many letter all of accept (char) type so print (A)..........-------------

#````````````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```````````````````````````````

'''x="""i am very happy and funnyly many more friends are
          and one of life travelling moment here and looking like ya wow"""

print(x) '''

#``````````````````````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`````````````````

'''supper="driving"
data1='hidden fire place'
print(['data1'])                     # STING USED TO "" CODS ARE SINGLE CODS    `````````````
print(["supper"])'''

#``````````````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~`````````````````````````````````

'''display="i'm a collage student"
print(display)'''              # there are not used to ''' cods ```````````````````~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''display= """manoj
            sanjay
            karthi"""
                        # that is many line data accept here...........-----------
print(display)'''

#```````````````````````  string length ```~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''a="manoj kumar!"
print(len(a))'''

#````````````````````````````````for looping````````````````````````````

'''a="banana"
for x in "banana":
    print(x)'''

#``````````````````````---:" check string  ":-------------------------------------------````````````

'''gate="dog in the house"
print("dog"in gate)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''gate="dog-in-the-house"

for screen in gate:

  if "windo"in gate:

    print("yes windo in")

  else:
    print("windo not in gate")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~""""...check if not in """"....~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''wolf="good charecters many her!"
print("bike"not in wolf)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''wolf="good charecters many her!"
if "happy" not in wolf:
  print("happy not in wolf")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~string slicing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''string1="trendzshop"
print(string1)
print("string1")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''a="manojkumar"
print(a[3:5])
print(a[2:-1])'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~:":"reversing a string":":~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''horse="ramuk jonam"
print(horse[::-1])'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~method.....2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''horse="ramuk jonam"
horse="".join(reversed(horse))
print(horse)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~updating  a  character of string~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''global8="mani things here"
print (global8)

list=list(global8)
list[3]='y'
water="".join(list)
print(water)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~method.....2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''global8="mani things here"
global9=global8[0:3]+'y'+global8[4:]
print(global9)'''
                     # tab(gaps) also counting here

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~entire string~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''mano="volleyball"
mano='total body'
mano="""ithula last tha print agum"""
print(mano)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~deleting a character~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# there is not use del key word by another way 2nd method..............~~~~~~~~~~~~~~~~

'''String1 = "Hello, I'm Arun"
print("Initial String: ")
print(String1)

print("Deleting character at 2nd Index:")
del String1[2]
print(String1)'''

# ~~~~~~~~~~~~~~~~~~~......... 2nd method............~~~~~~~~~~~~~~~~''''''''''''''''''''''''''

'''mano1="kaliforniya"
print('gapgapi')
print(mano1)
                  # not delet a character but change for this colam method ................
mano2=mano1[0:2]+mano1[3:-3]
print(mano2)'''

#~~~~~~~~~~~~~~~~~~~~~~~~""Escape Sequencing""~~~~~~~~~~~~~~~~~~~~~~~~~..............


'''dubai='see i\'s most beautiful'
print(dubai)
parrot="collage \"was\" waste"
print(parrot)
dubai="what is \\time now "
print(dubai)'''

# there used for single \  in single quotation
#   \\ used to in next word in key word that not over right here ......

#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~STRING FORMATTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''covai="{} {} {}".format('stone','papper','seser')
print(covai)

covai="{2} {0} {1}".format('stone','papper','seser')
print(covai)
             # those are binary formating~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

covai="{g} {f} {w}".format(w='stone',f='papper',g='seser')
print(covai)

covai="{0:b}\n{0:e}\n{0:2f}".format(20)
print(covai)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         python string methods

#                          ascii_letters


'''import string
result=string.ascii_letters
print(result)'''               # string.ascii_letters meaning small and capital (a to z) print here..........

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(.digits)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''import string
manoj=string.digits
print(manoj)    '''           # string.digits meaning (0 to 9) numbers print here........

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(.hexdigits)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''import string
kumar = string.hexdigits
print(kumar)     '''             # string.hexdigits meaning
                              # (0 to 9 and a to f caps and small letters print here/........
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(.endswith)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''text="o my god"
manoj=text.endswith(' god')
print(manoj)   # text.endswith meaning in last letter ending true or false (god) true so print (true)..

manoj=text.endswith("god",5,8)
print(manoj)'''
              #  that is (result for  (index value) method ).......

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(.startswith)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''text="copy paste send"

manoj=text.startswith('copy')
print(manoj)                 # .startswith meaning a startig word difine woring.........

manoj=text.startswith('copy', 0,5)
print(manoj)             #(index value).................................

manoj=text.startswith(('joly','lleu','copy'))
print(manoj)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#      any one letter in stats thats true ..........

'''manoj="kumar"
dai=manoj.startswith(('m','b','d','k'))
print(dai) '''                             # many letters here but stats letter in thats true ...........

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                    ((( string isdigit method )))

'''manoj='485687'
print(manoj.isdigit())  # true
                       # only getting ya numbers not in letters ...........
manoj='64hu564jsh89'
print(manoj.isdigit())  # false then letters inside so result false ........

manoj='omegle'
print(manoj.isalpha())
                          # .isalpha only ya letters accept here no numbers .......
manoj='horse'
print(manoj.swapcase())
                           # .swapcase work was small letters after caps letter chaning ..........

manoj='3578412'
print(manoj.isdecimal())
                         # .isdecimal only numbers allowed here.....

manoj='apple1'
print(manoj[5].isnumeric())
                            # .isnumeric only numbers accept here
                            # index method select tha one variable

manoj='uydghjf'
print(manoj.islower())
                      # .islower has only accept letters and only small letters......

manoj='GYYUGSSDF'
print(manoj.isupper())
                        # .isupper only caps letters allow here ........

add='manoj'
age='life'
story=("life is very sad {0} but now i have study {1} right right {0} now ."
       .format(add,age))
print(story)                      # STRING FORMAT() METHOD

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                              #  DIFICULT NO:1

txt = "I have {var:.3F} Rupees!"
print(txt.format(var = 4))'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     ()..............STRING FORMATEA.........()


'''print("hello,i am {} years old !".format(22))

manoj=("ones upon a time i go to {0} that place very {1} i need ya {2} and {3}")
print(manoj.format('ooty','mist','fire','lunch'))

print("college !life is very {} and many missing {} i love {}".format("beautiful","frd","vb" ))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
string = "Good Morning"
new_string = string.replace("Good","Great")
print(new_string)           # change tha value after print great morning......
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
manoj="smilr smilr smilr"
goast=manoj.replace("r","e")
print(goast)          #REPLACE THE VALUE (R) IRUKKA VALUES LA (E) YA MARIDUM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
string = "GUN GUN GUN GUN GUN GUN"
print(string.replace("GUN", "BUN", 4))'''
# REPLACE THA VALUE... OLD TO NEW CHANGE AND HOWMANY TIME CHANGE THATS A 6.........~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                              .isalnum()

# .isalnum() method that is number and letters are accept here not accept in special character ............
# and if else method ...............

'''manoj="XYZ123"
if manoj.isalnum():
       print("pass")
else:
       print("fail")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# run after abc123 is alphanumeric! True...........then no special character.....

'''manoj="abc123"  
print(manoj,"is alphanumeric!",manoj.isalnum())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                               .istitle()

# istitle method ares in any title first letter is ya capital letter it's ya true in small not true ....

'''m ='Welcome To IACT'
print(m.istitle())
           # this is ya false then first letter in caps but other letters in caps so false ....
m ='iACT tIRUPPUR'
print(m.istitle())
                 # first letter in smalla but other letter in caps so false
m ='WELCOME to IACT'
print(m.istitle())

m = '6041 Is My Number'
print(m.istitle())

m = 'IACT'       # this is false then total letters in capital letters so false.......
print(m.istitle())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                .partition() methods
# thats method has been selet tha word in center after words in side ..........

'''manoj="this is my class and all"
kumar="friends"
print(manoj.partition("my"))
print(kumar.partition("e"))'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# here in 2 characters but takes in first one ............thats all so partition methods .....

'''manoj="krishna waters serves krishna"
print(manoj.partition('krishna'))
                                    # same 2 characters vanthalum athu first la irukaratha tha edukum..
string = "b follows a, c follows b"
print(string.partition('follows'))'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         partition () method

'''string = "Welcome to IACT"
print(string.partition('is'))  '''     # is not here but take of the center ...............

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#................ Used Partition() Method to get a domain name from the String .......................

'''manoj="beem//kaliya/chutki"
boy = manoj.partition("//")
print(boy)
boy = boy[2].partition("/")
print(boy)
print(boy[0])'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Case sensitive Python ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# upper case or lower case check here.............

'''concept="bigboss overall tiruppur best shop and Overall pubilished"
manoj=concept.partition("overall")
print(manoj)                           # HERE CAPITAL WORD FIRST ACCEPT HERE.....
manoj=concept.partition("Overall")
print(manoj) ''' # THIS IS PARTITION METHOD .......................

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  String isidentifier() Method

'''manoj="localarea"   # starting not accept in numbers and spase ..starting accept in letters ....
print(manoj.isidentifier())'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 #                       ""..  just trail reference  ..""

'''string = "IACT COMPUTER"
print(string.isidentifier())

# A Perfect identifier
string = "IACTCOMPUTER"
print(string.isidentifier())

# Empty string
string = ""
print(string.isidentifier())

# Alphanumerical string
string = "IACT2COMPUTER"
print(string.isidentifier())

# Beginning with an integer
string = "55IACTCOMPUTER"
print(string.isidentifier())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    .'.'.'.'.'.''.'.'.'.'String rindex() Method.'.'.'.'.'.'.'.'.'.'

'''manoj="kerala croud big"
legal=manoj.rindex('o')       # this is index base work (o) is A 9th index so output is ("remaining'o':9")
print("remaining'o':",legal)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#      /''/'/'/'/'/'/''/Capitalize() in Python/''/'//''/'//''//'/
'''manoj="SAp thEartre"   # HOW MANY DATA YOUR PUT THA PROGRAM THEN AFTER FIRST LETTER ONLY A CHANGING CAPITAL .....
#print("original sting:",manoj)
print("after using capitalize:",manoj.capitalize())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#            /'/'/''    String Count()  /'/'/'
'''manoj="Himalaya hil"
boss=manoj.count('a')
print(boss)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''tom="[manojkumar]"
jerry="[m,a]"

monkey=[x for x in tom if x not in jerry]
print(monkey)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                           """/'/'   PRACTICAL 2   /'/'/'""###########################################

'''global8="mani things here"
global9=global8[0:3]+'y'+global8[4:]
print(global9)'''

'''a ="hello world"
print(a)
b=a.remove ['0:2']
print(b)'''

'''lol={"kee":"55","mee":"77","see":"33"}
del lol["kee"]
print(lol)
lol.clear()
print(lol)'''

'''a="hello world"
b=int(input())
for x in range(11):
  if x!=b:
      print(a[x],end="")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                                   ""/'/'/'PYTHON FUNTIONS"""/''/

'''def manoj(a):
    print("correct")
    c=a+50
    return c*2
print(manoj(10))'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def add(num,num2):
    num3=num*num2
    return num3

print (add(num2=10,num=20))'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''def nameAge(name, age):
       print("Hi, I am", name)
       print("My age is ", age)


nameAge("Kumar", 27)

nameAge(27,"Kumar")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def manoj(*dad):
    c=[]
    for x in dad:
        c.append(x)
    return c

print(manoj('google','50','65','yezdi'))'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def apple(**god):
    for x,m in god.items():
        print(" %s == %s" % (x,m))
apple(age='21',name='manoj',native='tiruppur')'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def ab ():
    print("manoj")
    def cd ():
        print('horse')
    cd()
ab()'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def add(a,b):
    if a==b:
        c=a+b
        return c*2
    else:
        c=a+b
        return c

print (add(10,120))'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def manoj (a):
    b=21
    if a==b:
        c=a-b
        return c
    elif b<a:
        c=a-b
        return c*2
    else:
        c=b-a
        return c


print(manoj(40))'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''a=int(input())
b=int(input())
c=a+b
if c<50:
    print("bellow 50")
else:
    print("above 50")'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def manoj (a):
    b=int(input())
    c=a+b
    if c>50:
        print("above 50")
    else:
        print("bellow 50")

manoj(10)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  must try 2nd program first for just try in learning affter try it conformly

'''class "Student":
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
object.class student'''
#!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''class volleyball:
    def__init__(self,coach,players):
        self.coach=coach
        self.players=players
    def teem(self.best,all the best):

obj=volleyball(best,all the best)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def condition(a,b):
    if a==True and b==True:
        print(True)
    elif a==False and b==False:
        print(False)
    elif a==True and b==False:
        print(True)
    elif  a==False and b==True:
         print(True)
condition(False,True)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       project input values are change list..........


'''p=[]
a=int(input())
for n in range(1,a+1):
    v=input()
    p.append(v)
print(p)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   manoj project success ::::  just for fun
'''def manoj (go):
    list = []
    for x in go:

        list.append(x)
    pop=sum(list)
    return pop
horse=[5,5]
print(manoj(horse))'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  manoj project success ::::: just for fun
'''a="tiruppur"
b=[]
for c in a:
    if c not in b:
        b.append (c)
print(b)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    project no 1

'''a=int(input())
if a%5:
    print("yes")
else:
    print("no")'''

#**********************************************************************************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python oops concept~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  🤩🤩🤩🤩🤩🤩

'''class manoj:

    play1="volleyball"
    play2="foodball"

    def game(self):
        print("i'am, not playing",self.play1)
        print("i'am, not playing",self.play2)

obj1=manoj()
#print(obj1.play1)
#print(manoj.play1)
obj1.game()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                             __init__ method

'''class person:

    def __init__(self,name):
        self.name=name

    def intro(self):
        print("hello i'am",self.name)

obj1=person('ashok')
obj1.intro()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''class bike:
    brand = 'pulser'
    def __init__(self,model,color,size):
        self.model=model
        self.color=color
        self.size=size
Arun = bike("ktm", "black",25)
shiva = bike("bajaj", "Brown",55)


print('\nArun bike details:')
print('Arun bike Barnd is ', Arun.brand)
print('model: ', Arun.model)
print('Color: ', Arun.color)
print('size:',Arun.size)


print('\nshiva bike details:')
print('shiva bike Barnd is ', shiva.brand)
print('model: ', shiva.model)
print('Color: ', shiva.color)
print('size:',shiva.size)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~oops concept first practical~~~~~~~~~~~~~~~~~~~~~~~

'''class food:
    hotel="NELLAI LALA"

    def __init__(self,idli,dosa,poori,pongal):

        self.idli=idli
        self.dosa=dosa
        self.poori=poori
        self.pongal=pongal
    def manoj(self):
        print("idli {},dosa {},poori {},pongal {}".format(self.idli,self.dosa,self.poori,self.pongal))

morning=food(2,5,1,2)
afternoon=food(3,2,4,1)

morning.manoj()
afternoon.manoj()
print(food.hotel)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  INHERITANCE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''class animal:
    name=""
    def eat(self):
        print("i can eat")

class tiger(animal):

    def display(self):
        print("my name is",self.name)

obj1=tiger()

obj1.name="manoj"
obj1.eat()
obj1.display()
#print(animal.name)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# here 2 funtion are same word.. but take second ................

'''class animal:
    name=("")
    def eat(self):
        print("yes i can eat dosa")

class tiger(animal):
    def eat(self):
        print("i don't have any food")

obj1=tiger()

obj1.eat()'''    # here 2nd data take the program......................

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  😋😋😋😋 The super() Method in Python Inheritance😋😋😋😋

'''class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Tiger(Animal):
    def eat(self):

        super().eat()

        print("I like to eat bones")

obj1 = Tiger()
obj1.name='manoj'
obj1.eat()
print(Animal.name)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   this method for two base() one derived() method ........................

'''class base1():

    def __init__(self):
        self.mom1='manoj'
        print("wow.1")
                                    # here 2 base ku oru derived open here ..and 3 init methods ku
class base2():                       # def funtion display nu open pandram

    def __init__(self):
        self.mom2='\nkumar'
        print("wow.2")

class derived(base1,base2):

    def __init__(self):

        base1.__init__(self)
        base2.__init__(self)
        print(self.mom1,self.mom2)

    def display(self):
        print(self.mom1,self.mom2)

obj1=derived()
obj1.display()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  THIS CONTINUE  TO SAME PROGRAM IN LAST PROGRAM...................

'''class base():
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
class child(base):
    def __init__(self,name,age):
        base.__init__(self,name)
        self.age=age

    def getage(self):
        return self.age
class grandchild(child):
    def __init__(self,name,age,address):
        child.__init__(self,name,age)
        self.address=address

    def getaddress(self):
        return self.address

g=grandchild("iact",40,"tiruppur")
print(g.getname(),g.getage(),g.getaddress())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''class grandfather:

    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

class father(grandfather):
    def __init__(self, fathername,grandfathername):
        self.fathername = fathername
        grandfather.__init__(self,grandfathername)

class Son(father):
    def __init__(self, sonname,fathername,grandfathername):
        self.sonname = sonname
        father.__init__(self,fathername,grandfathername)

    def print_name(self):
        print("grandfather name :",self.grandfathername)
        print("father name :",self.fathername)
        print("Son name :",self.sonname)

s1 = Son('manoj', 'Raja', 'Siva')
print(s1.grandfathername)
s1.print_name()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

#object1 = Child1()
object2 = Child2()
#object1.func1()
#object1.func2()
object2.func1()
object2.func3()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

'''class School:
    def func1(self):
        print("This function is in school.")
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")

class Student2(School):
    def func3(self):
        print("This function is in student 2.")

class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

#object2 = Student2()
#object2.func3()           #we can run this program by this type of syntax also...

#object = Student3()
#object.func1()
#object.func2()
#object.func4()'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~💕💕💕💕POLYMORPHISM IN PYTHON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive!")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly!")

car1=car("ford","mustang")
boat1=boat("doll","kargo")
plane1=plane("king","arrab")

for x in (car1,boat1,plane1):
    x.move()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~`~~~~~🎶🎶🎶🎶🎆Encapsulation in Python🎆🎶🎶🎶🎶~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~Those types of variables are known as private variables~~~~~~~~~~~~~~~~
#       ......................single underscore “_”......................

'''class base:
    def __init__(self):
        self._a = 2

class derived(base):
    def __init__(self):

        base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        self._a = 3
        print("Calling modified protected member outside class: ", self._a)

object1=derived()
object2=base() '''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   🌹🌹🌹🌹🌹🌹🌹✨ to define a private with double underscore “__”.✨🌹🌹🌹🌹🌹🌹🌹

'''class base:
    def __init__(self):
        self.a = "Tamilnadu"
        self.__c = "Tamilnadu"

class derived(base):
    def __init__(self):

        base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

object1=base()
object2=derived()
print(object2.c)
print(object1.a)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        ❤❤❤❤❤❤❤❤❤❤❤❤❤✨ABSTRACTION✨❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
#....\\\..... THAT IS  HIDE CODING PROGRAMS PYTHON......
#                        THIS IS ONLY USE FOR FUNTIONS PROGRAMS......../////

'''import test1
test1.myfunction()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''class car():
    def __init__(self,model):
        self.model=model
    def difference (self):
        print("this cars also available")
class company (car):
    def __init__(self,model,future):
        car.__init__(self,model)
        self.future=future

    def difference (self):
        print("audi:")

class customer (company):
    def __init__(self,model,future,colour):
        company.__init__(self,model,future)
        self.colour=colour

    def  difference (self):
        print("lanzer:")

class employer (customer):
    def __init__(self,model,future,colour,amount):
        customer.__init__(self,model,future,colour)
        self.amount=amount

    def difference (self):
        print("honda:")

car1=car("benz")
company1=company("benz","autometic")
customer1=customer("benz","autometic","purple")
employer1=employer("benz","autometic","purple","1,00,0000")

for x in (car,company,customer,employer):
    x.difference

#object1=customer
#object1.swiftcar
#g=employer("rollsroice","autometic","purple","1,00,000")
#print(g.benzcar(),g.hondacar(),g.swiftcar(),g.eight100())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     👀👀👀✨✨File Handling in Python✨✨👀👀👀


'''hi=open('manoj.txt','w')       #'w' is write tha program shot form
b="hello\n"                       #'r' is read tha program shot form
c=["bike:","\tcar:","\tbus:"]     #'a' is append tha program shot form
                                  #''
hi.write(b)
hi.writelines(c)

hi.close()

hi=open('manoj.txt','r')
print(hi.read())
hi.close()'''

#~~~~~~~~~~~~~~~~~~~~~~~~
'''my=open('manoj1.txt','w')
a=["kholli:\t","virat:\t","satchin:\t","fazil:\n"]
my.writelines(a)
my.close()

my=open('manoj1.txt','a')
my.write("holiday:")      # this is append method after holiday is append 'a' :
my.close()

my=open('manoj1.txt','r')
print(my.read())
my.close()

#✨✨here same data put tha program so over right here and delet tha first same data::::

fz=open('manoj1.txt','w')                     #'manoj1.txt','w' :::this is same data
a=["karthi:\t","ashok:\t","mithun:\t"]        # so over right and print  this "a"  ::
fz.writelines(a)
#fz.close()

fz=open('manoj1.txt','r')
print(fz.read())
#fz.close()'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       🎶    🎶       file handling  With statement  !!!!!!

'''manoj = ["python:", "java:", "html:"]

with open("player.txt", "w") as game:
    game.write(" Hello ")
   # game.writelines(manoj)
#with open("player.txt", "r") as game:p
    for x in manoj:
        game.write(x +'\n')

with open("player.txt", "r") as game2:
    print(game2.read())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

'''with open("sad.txt",'w')as ganthi:
    ganthi.write("kumar\n")
    l=["qqq\n","www\n","eee\n"]
    ganthi.writelines(l)

with open("sad.txt",'r') as ganthi:
     #print(ganthi.read(3))           #read use to full of output show here
     #print(ganthi.readline())        #readline use to output in first data show here
     print(ganthi.readlines())'''     #readlines use to  full of output and show conway to list[]:::

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           that is file remove method:::

#import os
#os.remove("New Text Document.txt")

#      if:    else:          method for file remove use ::

'''import os
if os.path.exists("jacksparow.txt"):
    os.remove("jacksparow.txt")
else:
    print("no ")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   for method in file handling:::

'''hy=["hhh\n","sss\n","ooo\n"]
d=["ggg","hhh","ppp"]
with open("hifi.txt",'w')as g:
    g.writelines(hy)
    g.write((input()) +'\n')
    for x in d:
        g.write(x+"\n")

with open("hifi.txt",'r')as g:
    print(g.readlines())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# while method for file handling:::

'''with open("hifi.txt",'r')as f:
    #print(f.readline())
    s=f.readline()
    a=0
    while a<5:
         print(s)
         s=f.readline()
         a+=1'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for method for file handling::

'''with open("dad.txt",'w')as u:
    #u.write("hello")
    b=[] 
    for x in range(1,5):
        a=input()
        b.append(a)
        u.writelines(b)
with open("dad.txt",'r')as u:
    print(u.read())
    print(u.readline())'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        😼😼😼ERROR HANDLING😼😼😼

# program make some error so suddenly close tha program so don't close way of
# then you use tha ...."try"...  and .. "except".. program


'''try:
  a=int(input())
  b=int(input())
  c=a+b
  print(c)
except:
    print("number only")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''def manoj():
    for x in range (5):
        print("who are u")
        a=input()
        if a=="AAA":
            print("1::go to next")
        elif a=="BBB":
            print("2::go to next")
        elif a=="CCC":
            print("3::go to next")
        elif a=="DDD":
            print("4::go to next")
        elif a=="EEE":
            print("5::go to next")
            print("finish")
        else:
            print("you are fail")

print(manoj())'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                            🦋🦋✨...PYTHON ... MYSQL...✨🦋🦋
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin")

mycursor = mydb.cursor()
mycursor.execute("create database emp")'''


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# summa :::::

'''a=3
b=int(input())
for x in range (b):
    #print(x)
    if x != a:
        print(x*2)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''d=[]
b=[]
for x in range (1,6):
    a = int(input())

    if a > 50:
        b.append(a)
    else:
        d.append(a)
print("above 50:::",b)
print("below 50:::",d)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''def manoj():

    for x in range (1,4):
        m = int(input())

        if m <= 20 :
            print(m,"i am A school student::")

        elif m <= 25 :
            print(m,"i am A college student")

        else:
            print(m,"i am business man")
print(manoj())'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''def manoj ():
    b=int(input())
    if b<=20:
        print("i am A school student:: ")

    elif b<=25:
        print("i am A college student:: ")

    elif b<=50:
        print("i am a business man:: ")

print(manoj())'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     practice for file handling:::::::::::✨✨✨


'''a=open("gost.txt",'w')
a.write("sorry\n")
z=["beem\n","dash\n","jaggu\n"]
a.writelines(z)
a.close()

a=open("gost.txt",'r')
print(a.read())
a.close()'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''a=open("gost.txt",'a')
a.write("lolipop\n")
c=["ggg\n","uuu\n","ooo\n"]
a.writelines(c)
a.close()

a=open("gost.txt","r")
print(a.read())
a.close()'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''a=open("gost.txt",'w')
d=[]
for x in range (1,5):
    f=(input())
    d.append(f)

for s in d:
    a.writelines(s+"\n")
    print(s)'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''with open("three.txt",'w')as jd:
     for x in range(1,6):
        c=input()
        jd.write(c+'\n')'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%     🎇🎇🎃🎃🎇🎇project for not come slace\\\ es ....     %%%%%%%%%%%%%%%%%%


'''manoj="D:\MANOJ\pyc\main.py"
q=manoj.split("\\")
#print(q)

for x in q :
    print(x)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%  ✨✨✨✨project  print in random questions  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''class manoj():
    import random
    a=["1.what is pytho","2.what is number","3.bike going road or water","4.what is 123","5.what is diffence","6.cobra is snake or fish","7.human is nature","8.java in query language","9.tailer in it jobs","10.big temple in chennai"]
    print(a[random.randrange(1,10)])

manoj()'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%  ✨✨🎐🎐 project reverse correct word 🎐🎐✨✨ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''a=input()
b="".join(reversed(a))
#print(a)
if a==b:
    print("right")
else:
    a!=b
    print("wrong")'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
###%%%%%%%%%%%%%%%%%%%%%  project not comming same letters ::::  %%%%%%%%%%%%%%%%%%%%%%

'''a="python code"
b=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        print("yes")
        
print(b)'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%% vowels project same letter in print +1:::: %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''a = input()
y=0
f=0
b=["a","e","i","o","u"]
for x in a:
    if x in b:
        y=y+1
    else:
        f=f+1
print(y)
print(f)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''a=int(input)
if a<100:
    print("no charge")
    elif:
    a<200:(
        print("charge :10:"))'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%practical%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''b=int(input())
if b<=100:
    print(" no charge ")
elif b<=200:
      b=b*10
      print(b)
else:
    b<=300
    h=b*20
    print(h)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%⚽ datetime program 🏐🏀%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''from datetime import datetime
from datetime import time
a = datetime.now()
print(a)
b = time()
n=time(11,45,54)
print(b)
print(n)'''

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%









