#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1= Cat('A',2)
Cat2= Cat('B',3)
Cat3= Cat('C',4)

# 2 Create a function that finds the oldest cat
def FindOldest(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is { FindOldest(Cat1.age, Cat2.age, Cat3.age)} years old.")