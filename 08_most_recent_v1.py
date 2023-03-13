# get data from user and store it in list, then display the most recent three nicely

# set up empty list
all_calculations = []
MAX_CALCS = 5

# get items from data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

all_calculations.reverse()

# show that everything made it to the list
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 5 ***")
for item in range(0, 5):
    print(all_calculations[len(all_calculations) - item - 1])

else:
    print()
    print("*** Items from Newest to Oldest ***")
    for item in all_calculations:
        print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])

