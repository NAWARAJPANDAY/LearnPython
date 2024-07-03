from symtable import Symbol


resultset ={
    '00123456A':'4',
    '00123457B':'2.5',
    '00123459J':'3.9',
}
Symbol_no = input("Enter your symbol number ")

result =""

for i in resultset.keys():
    if Symbol_no == i:
        result =resultset[i]
        break
    else:
      result =''

if result != "":
   print(f"Your result is {result}")
else:
    print("Your symbol is  number not found.")