print("Enter the numbe of Days: ")
num = int(input())
year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)
print("Total Number of Years: ")
print(year)
print("Total number of weeks: ")
print(week)
print("Total number of days ")
print(days)