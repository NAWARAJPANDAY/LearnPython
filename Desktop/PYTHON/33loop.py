#for i in range(1,11)
#print(i)

#Creat Multiplication table of 9


start = int(input("Enter start number :"))
end = int(input("Enter end number:"))
for i in range(1,11):
   
    print(f"9*{i}={9*i}")
for i in range (1,11):
    for j in range(1,11):
             print(f"{i}*{j}={i*j}")
             print("\n-----\n")
