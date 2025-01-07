Amount =int(input("Please Enter amount for withdraw:"))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100 rupee",note_1)
print("Notes 0f 50rupee",note_2)
print("Notes 0f 10 rupee",note_3)