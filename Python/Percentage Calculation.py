print('Enter Marks obtained in 4 subjects:')
math = int(input("Maths:"))
science = int(input("Science: "))
english = int(input("English: "))
hindi  = int(input("Hindi: "))
sum = math + science + english + hindi
print("Sum of all the subjects",sum)
per = (sum/400)*100
print(end="Percentage Marks =")
print(per)