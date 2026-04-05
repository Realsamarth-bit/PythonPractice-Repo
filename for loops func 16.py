list1=["smarth","rahul","ronaldo","messi",]
print(list1)
for item in list1:
    print(item)

tuple=("smarth","rahul","ronaldo","messi",)
for item in tuple:
    print(item)

loop=[["smarth", 55],["rahul", 45],["ronaldo", 67],["messi", 677,]]
for item, num in loop:
    if item == "smarth" :
        print(item, "this is list and money number",num)
else:
    print("not found")

samlist=["samarth","57","riya","nikhil","56","6","5","4",]
for item in samlist:
    if item.isdigit():
        if int(item)>6:
            print(item)