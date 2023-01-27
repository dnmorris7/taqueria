import json
#read the menu from the menu.json file
data = json.load(open('menu.json'))

 #convert each key in data to lowercase
dataLower = {k.lower(): v for k, v in data.items()}

'''for item in menu:
    menu[item] = {"name": item, "price": menu[item]}
'''
#print(menu)
#convert the menu to a list of dictionaries
menu = [{"name": item, "price": data[item]} for item in data]

def display_menu():
    print("Welcome to the Taqueria!")
    print("MENU")
    print("----")
    for item in menu:
        print(item["name"], item["price"])

 
#tally order total
def tally_order(order):
    total = 0
    for item in order:
        total += dataLower[item]
    return total       




# Ask for user input. If the user enters control+d, exit the program. If the user enters something not on the menu, ignore it. If the user enters something on the menu, add it to the order.
def get_order():
    order = []
    tally = "$0.00"
  
    while True:
        try:
            item = input("What would you like to order? ").lower()
           
            if item in dataLower:
                order.append(item)
                #print ongoing order items
                print(f"You added {item} to your order.")
                print(f"Your orders so far: {', '.join(str(i).title() for i in order)}.")

                #formate tally_order as currency
                tally = "${:,.2f}".format(tally_order(order))
                print(f"Current Total: {tally}")

            if item == "done" or item == "no" or item == "exit":
                print("Thank you for your order!")
                print(f"Current Total: {tally}")
                break

            if item == "cancel":
                print("Your order has been cancelled.")
                break
        
        #add exception to exit program
        except EOFError:
            print("System Error. Ordered Canceled.")
            break
    


#test display_order_options
display_menu()

#test get_order
get_order()

'''

def get_order():
    order = []
    tally = "$0.00"
    try:
        item = input("What would you like to order? ").lower()
        while True:     
            if item in dataLower:
                order.append(item)
                #print ongoing order items
                print(f"You added {item} to your order.")
                print(f"Your orders so far: {', '.join(str(i).title() for i in order)}.")

                #formate tally_order as currency
                tally = "${:,.2f}".format(tally_order(order))
                print(f"Current Total: {tally}")

            if item == "done" or item == "no":
                print("Thank you for your order!")
                print(f"Current Total: {tally}")
                break
        
        return "Order Complete."
    except EOFError:
        print("Goodbye!")
        return "Order Complete."
        

'''