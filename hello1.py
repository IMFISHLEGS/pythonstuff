
print ("hello world!")

full_name = "goodness man"

print (full_name)
full_name = "black widdow"
print (full_name)
full_name = " the kkatanjin brothers"
print (full_name)
surname = "quadrishh"
print (surname)

# i cant breath by goodness 
cake = "buzy guy"
print (cake)
money = "even if i cant see shit"
print (money)
dupe = "somto has thin butts"
print (dupe)
greetings = 'my boss yelled "go fuck yourself"'
print (greetings)
name = "raymond"
greetings = "my name is not " + name
print(greetings.split(" "))
num = "66"
print((int(num)) * 3)
favorite_cars = {
"anderson": "mazda", 
"funmi": "rolls royce",
"plum": "GMT",
}
print(favorite_cars["plum"]) 
print(favorite_cars)
num = 12
print(num * 3)
print(10 == 10)
print(12 <= 11)
name = ["max", "bob", "shayla"]
for banana in name:
	print(banana)
fav_pizza = {
	"john": "pepperoni",
	"blake": "mushroom",
	"bob": "cheese",
}
for key,value in fav_pizza.items():
	print(key + " dosent like " + value + "pizza")

num = 0
while (num <= 100):
	if (num % 3 == 0) and (num % 5 == 0):
		print (str(num) + ". fizzbuzz!")
	elif (num % 3 == 0):
		print (str(num) + ". fizz!")
	elif (num % 5 == 0):
		print (str(num) + ". buzz!")
	else:
		print(str(num) + '.')	
	num +=1


num = 0
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0


while (num <= 100):
	if (num % 3 == 0) and (num % 5 == 0):
		print (str(num) + ". fizzbuzz!")
		fizzbuzzcount += 1

	elif (num % 3 == 0):
		print (str(num) + ". fizz!")
		fizzcount += 1

	elif (num % 5 == 0):
		print (str(num) + ". buzz!")
		buzzcount += 1

	else:
		print(str(num) + '.')	
	num +=1

print("________________________")
print("fizz\tbuzz\tfizzbuzz")
print(str(fizzcount) + "\t" + str(buzzcount) + "\t" + str(fizzbuzzcount))

def nameit(pizza):

	print("i love " + pizza)

nameit("pepperoni")	

from naging import naging
naging("i love pizza")






