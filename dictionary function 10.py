dict={}
dict1={"samarth":"roti","rahul":
    "pizza","ayaan":"biryani","riyan":{"b":"roti","l":"biryani","r":"saboon",}}
print(dict1)
print(dict1["riyan"]["b"])
dict1["rajesh"]="coca cola"
print(dict1)
d1=dict1.copy()
print(dict1["riyan"]["l"])
print(dict1.keys())
print(dict1.items())
print(type(dict1))