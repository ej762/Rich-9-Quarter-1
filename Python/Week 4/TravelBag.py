bedroom = ["Hat","Shoes","Clothes","PS5."]


travelbag =[]

print("PACK YOUR BAGS")
print("Enter the index of an item you'd like to mobe from your room to bag.")
print("Type 'done' when you are done packing.\n")
print("Your Bedroom Items")
for item in bedroom:
    print(item)

item = int(input("Item index"))


while item !=100:
    travelbag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("/nYour bedroom;")
    print(bedroom)
    print("\nYour travelbag;")
    print(travelbag)
    item = int(input("Item Index:"))
