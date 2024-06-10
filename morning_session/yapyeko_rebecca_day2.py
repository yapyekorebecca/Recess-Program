# Example 1
age=70
if age>18:
    print('You are an adult')
    
elif age>65:
    print('You are a senior citizen')

else:
    print('You are a youth')
  
  
#   Example 2  
grade=90

if grade>=90:
    print('Excellent')
elif grade>=80:
    print('Very Good')
elif grade>=70:
    print('Good')
else:
    print('Not good')

# Example 3
age= int(input('Enter Age:')) 
price=2000
if age<13:
    print(price-1000)
elif age>=13 and age<=18:
    print(price-500)
elif age>=18 and age<=65:
    print(price)
else:
    print('pay 5000')
   
# LOOPS 
# for,while
cars =['Tesla','Audi','Jeep','RangeRover']
for car in cars:
    print(car)
  
#   While loop  
count=0
while count<=10:
   print("Count 1 to 10:",count)
   count +=1

# Examples  (reversing)
favorite_colors= ['Black', 'Red', 'Green','Blue','Purple']

reversed_color=favorite_colors[::-1]
for color in reversed_color:
    print(color)
    
index=len(favorite_colors)
while index>=0:
    print(favorite_colors[index])
    index-=1
    
num=[1,2,3,4,5]
index=len(num)
while index>=0:
    print(num[index])
    index-=1
    
