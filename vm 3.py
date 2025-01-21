class VendingMachine:
    def __init__(self):
        #Initialize products are their prices
        self.items = {
            "Hot Drinks": {"C1": ("Coffee", 2.0, 5), "C2": ("Tea", 1.5, 5)},
            "Snacks": {"S1": ("Chips", 1.2, 3), "S2": ("Chocolate Bar", 1.0, 4)},
            "Cold Drinks": {"D1": ("Water", 0.8, 6), "D2": ("Soda", 1.5, 5)},
            }
        self.total_money = 0.0
    #The display to indicate when an item is out of stock.
    def display_menu(self):
        print("\nWelcome to the Vending Machine!")
        print("Here are the available items:")
        for category,  products in self.items.items():
            print(f"\n{category}:")
            for code, (name, price, stock) in products.items():
                stock_status = f" (Out of stock)" if stock == 0 else ""
                print(f"  {code}: {name} - ${price:.2f}{stock_status}")
                
    # Check if the selected item is valid             
    def get_user_selection(self):
        while True:
            code = input("\nEnter the codes of the item you want to purchase: ").strip()
            for products in self.items.values():
                if code in products:
                    return code, products[code]
                print("Invalid code, please try again.")
    #prompt user to insert money             
    def accept_payment(self, price):
        while True:
            try:
                money = float(input(f"Insert money (price: ${price:.2f}): "))
                if money >= price:
                    return money
                else:
                    print("Insufficient money, please try again.")
            except ValueError:
                print("Invalid input, please enter a valid amount.")
    def dispense_items(self, code):
        for products in self.items.values():
            if code in products:
                products[code] = (products[code][0], products[code][1], products[code][2] - 1)
    #Suggest purchase item with category             
    def suggest_purchase(self, category):
        suggestion = {
            "Hot Drinks": "How about a biscuit with your hot drink?",
            "Snacks": "A drink might go well with your snack!",
            "Cold Drinks": "Consider a snack to pair with your drink!",
        }
        return suggestion.get(category, "")
    
    def start(self):
        while True:
            self.display_menu()
            code, (name, price, stock) = self.get_user_selection()
            if stock == 0:
                print(f"Sorry, {name} is out of stock.")
                continue
            money = self.accept_payment(price)
            change = money - price
            self.total_money += price
            self.dispense_items(code)
            print(f"\nDispensing {name}. Enjoy!")
            print(f"Your change: ${change:.2f}")
            
            #Suggest complementary item
            for category, products in self.items.items():
                if code in products:
                    suggestion = self.suggest_purchase(category)
                    if suggestion:
                        print(suggestion)
                        
            #Allow additional purchase
            cont = input("\nWould you like to buy another items? (yes/no): ").strip().lower()
            if cont != "yes":
                print("\nThank you for using the Vending Machine. Have a great day!")
                break
            
#Run the vending machine
vending_machine = VendingMachine()
vending_machine.start()
            