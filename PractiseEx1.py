# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)
x=int(input())
y=int(input())
x=x//y
y=y//x
print(y)
# conn = smtplib.SMTP('smtp.gmail.com',587)
# conn.ehlo('')
# print(conn.starttls())



#import webbrowser
# from selenium import webdriver
# browser = webdriver.Firefox()

#res= requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code)
# print(len(res.text))
# print(res.text[0:1000])
address='22814 lodge ct novi mi'
# if len(sys.argv)>1:
#   address=" ".join(sys.argv[1:])
# else:
#   address=pyperclip.paste()

#webbrowser.open('https://google.com')
# import os
# os.chdir('C:\\Desktop')
# print(os.getcwd())
# print(os.path.isfile('C:\\Desktop\\hii.txt'))
# hFile=open('C:\\Desktop\\hii.txt')
#os.makedirs('C:\\Desktop\\PyFolder')
#print(os.listdir('C:\\Desktop'))
lst=['H','e','l','l','l','o','o']
#lst=[1,1,2,3,3,3,3,4,4]
#print('-'.join(lst))
# print(lst.count(3))

# import re
# vowelRe= re.compile(r'^ro*')
# spam="robocop eats all of the baby food available in the fridge"
# print((vowelRe.findall(spam)))


# str1='hiblahhowblahblahareblahublah'
# str2= str1.lstrip('blah').rstrip('blah')
# #if len(str2) != 10:
# print(str2)


# sup=['bins','chart','books','pens']
# sup.sort(reverse=True)
# print(sup)
# for i in range(len(sup)):
#   print(f"Index {i} in supplies contains {sup[i]}")

# a=5
# def su():
#   global a
#   a="Hii"
#   #print(a)
#   return a
#   #return a
# print(su())
# print(a)

lst=[1,2,3,4]
lst2=lst[-1:]
#print(lst2)

# v=-1
# if v==1:
#   print("case1")
# if v<=1:
#   print("case2")
# if v!=0:
#   print("case3")
# else : print("case4")


# print([i for i in range(-1,-2)])

# lst=[[x for x in range(3)] for y in range(3)]
# for r in range(3):
#   for c in range(3):
#    if lst[r][c]%2!=0:
#        print("#")



# num=[1,2,3]
# val = num
# del val[:]
# print(val)
# print(num9)



# dct={}
# dct['1']=(1,2)
# dct['2']=(2,1)
# for x in dct.keys():
#   print(dct[x][1],end="")
# tup=1,2,4,8
# tup=tup[-2:-1]
# tup=tup[-1]
# print("a","b","c",sep="sep")

# v=1
# if v==1:
#   print("A")
# elif v<=1:
#   print("B")


# for i in range(2):
#   print("$")
# else:
#   print("$")

'''def chckOdd(lst):
  return lst%2==1
lst=[1,2,3,4,5,6,7,8,9]
print(list(filter(chckOdd,lst)))

def mulby2(lst):
  return lst.upper()
lst=['a','d','g','h']
print(list(map(mulby2,lst)  ))

class User():
  def signin(self):
    print("Yes logged in")

class Wizard(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print (f'Attack with power of {self.power}')

class Archer(User):
  def __init__(self,arrows):
    self.arrows=arrows
  
  def narrows(self):
   print(f"The number of arrows are: {self.arrows}")

class HybridClass(Wizard, Archer):
 def __init__(self, name, power, arrows):
   Archer.__init__(self,arrows)
   Wizard.__init__(self,name,power)

hc1=HybridClass('Ann',56,5)
print(hc1.attack())
print(hc1.narrows())
print(hc1.signin())

class SuperClass(list):
 def __len__(self):
   return 1000

super_list1= SuperClass()

print(len(super_list1))
super_list1.append(3)
print(super_list1[0])
print(issubclass(SuperClass,list))

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('simon',10),Sally('sally',5)]
 
#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets= Pets(my_cats)
#4 Output all of the cats walking using the my_pets instance
my_pets.walk()
 
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
  
    if name in schoolClass:
        schoolClass[name] += (score)
    else:
        schoolClass[name] = (score)
        
for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)

 l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l1
del l2

print(l3)


class User():
  def sign(self):
    print('Signed-in')

class Wizard(User):
  def __init__(self, name, power):
   self.name = name
   self.power = power
  
  def attac(self):
    print(f'Attacking {self.name} power of {self.power}')
  
class Archer(User):
  def __init__(self, name, nArrows):
    self.name = name
    self.nArrows = nArrows
  
  def attack(self):
    print(f'has arrows {self.nArrows}')

wiz1= Wizard('AA',5)
print(wiz1.attac())
 '''
# '''
# class PlayerNames():
#   def __init__(self, name='anon', age=5):
#    self.name=name
#    self.age=age

#   def shout(self):
#    print(f'Name is {self.name} and age is {self.age}')

# Player1= PlayerNames()
# Player1.name="aloo"
# print(Player1.name)
# print(Player1.shout())

# def high_even(mlist):
#   elist=[]
#   for l in mlist:
#     if l % 2 == 0:
#       elist.append(l),
#   print(max(elist) )
#   return

# li=[4,10,2,3,4,8,11]
# high_even(li)

# def s2Num():
#     n1 = input("Enter first number: ")
#     n2 = input('Enter second number: ')
#     return int(n1) + int(n2)

# print(s2Num( ))

# def say_hello():
#   print('Hellloooo.!!')

# say_hello()

# print(say_hello)

# mList= ['a','b','c','b','d','m','n','n','n']
# dup=[]
# for l in mList:
#   if mList.count(l)>1:
#     if l not in dup:
#      dup.append(l)
# print(dup)
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for row in picture:
#   for p in row:
#    if p== 0:
#     print(" ", end='')
#    else :
#     print("*", end='')
#   print('')

# mlist=[1,1,2,2,2,3,4,4,4,4]

# for i,char in enumerate(list(range(100))):
#   if i<50:
#     print(i,char)
#     break

# for i in range(1, 10, 2):
#     print(i)
#  mList=[1,2,3,4,5,6,7,8,9,10]
# nSum=0;
# for m in mList:
#    nSum += m;
# print("The sum of 10 integers is:",nSum)

# DIct = {
#   'a': 1,
#   'b' : 'hellooo',
#   'c': 'dd',
#   'd': 5
# }

# for key,value in DIct.items():
#         print('The values are', key, ',', value)

# old = 1
# lic= 0
# if old and lic :
#   print('Expert')
# elif old and not lic :
#     print("U r a learner")

# msg = "You are old.!!" if old else "You are Young.!"
# print(msg)

# if old:
#   print("Is eleigible")
# else:
#   print('Not eligible')

# mset= {1,2,3,3,3,3,4,5}
# mset.add(2)
# print(mset)

# DIct = {
#   'a': [1,2,3],
#   'b' : 'hellooo',
#   'c': ['x','y','z'],
#   'd': 5
# }
# DIct.update({'e':9})
# print(DIct)

# lists = ['a','b','c','d']
# lists.append('g')
# lists.extend(['e','h'])
# #lists.pop(1)
# lists.sort()
# print(lists)
# sen = '  '.join(['hi','there'])
# print(sen)

# print(lists.index('g', 0,6))
# nlist= lists
# nlist.insert(2,'p')
# nlist.clear()
# print(nlist)
# print('a' in nlist)


# print(bin(1))
# print(int('0b1011', 2))
# Iq=10
# Iq =+ 5
# print(Iq)
# print("hello" + " 5")
# name= "Jon"
# print(name[::-1])

# exp = "hey it\'s a \"very\" \n \t windy day "
# print(exp)

# greet= "Hello, how r u?"
# print(f'Hi {name}. {greet}')
# #print(reversed('greet'))

# print(exp.capitalize())
# exp = exp.replace('it','mit')
# print(exp)

# uN = input("Enter a username: ")
# pwd= input("Enter your password: ")
# pwdlen= len(pwd)

# print(f"Heyy {uN}, your password is {'*' *pwdlen} and it is {pwdlen} chartacters long.")
# '''