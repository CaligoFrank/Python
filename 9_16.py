class ItemToPurchase:

    def __init__(self):
        """item_name = 'none'
            item_description = 'none'
            item_price = 0
            item_quantity = 0
        """
        self.item_name = 'none'
        self.item_description = 'none'
        self.item_price = 0
        self.item_quantity = 0


    def set_item_name(self, item_name):
        """Sets the Items name

        Args:
            item_name (string): assigns to the name to the object
        """
        self.item_name = item_name

    def set_item_price(self, price):
        
        self.item_price = price
    
    def set_item_quantity(self,quantity):
        self.item_quantity = quantity

    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
        


class ShoppingCart:
    def __init__(self, customer_name, current_date) -> None:
        self.customer_name = 'none'
        self.current_date = 'Janurary 1, 2016'
        self.cart_items = []
    
    def add_item(self, item : ItemToPurchase):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        item: ItemToPurchase
        
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
            else:
                print(f"Item not found in cart. Nothing removed.")
    
    def modify_item(self, quantity, itemToPurchase : ItemToPurchase):
         
        item : ItemToPurchase
        for item in self.cart_items:
            if item.item_name == itemToPurchase.item_name:
                item.set_item_quantity(quantity)
            else:
                print("Item not found in cart. Nothing modified.")
     
    def get_num_items_in_cart(self):
        item : ItemToPurchase
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total
    
    def get_cost_of_cart(self):
        item : ItemToPurchase
        total_cost = 0
        
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        
        item : ItemToPurchase
        
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
            
        print(f"Total: ${self.get_cost_of_cart()}")
        
    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        
        print(f"Item Descriptions")
        item : ItemToPurchase
        
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
        
         
        

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    shoppingCart = ShoppingCart(customer_name,current_date)
    
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    
    
    def print_menu():
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
    def execute_menu(user_choice, shoppingCart: ShoppingCart):
        if user_choice == 'a':
            pass
        elif user_choice == 'r':
            pass
        elif user_choice == 'c':
            pass
        elif user_choice == 'i':
            pass
        elif user_choice == 'o':
            print("OUTPUT SHOPPING CART")
            
            
    
    #Main
    print_menu()
    user_choice = input("Choose an option: ")
    
    
    if user_choice != 'q':
        execute_menu(user_choice, shoppingCart)
    
    