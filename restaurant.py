import math

class Table:
    
    def __init__(self, amnt_diners):
        self.amnt_diners = amnt_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        
        for bill_details in self.bill:
            if bill_details["item"] == item and bill_details["price"] == price:
                bill_details["quantity"] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for order_info in self.bill:
            if order_info["item"] == item and order_info["price"] == price:
                if order_info["quantity"] >= quantity:
                    order_info["quantity"] -= quantity
                    if order_info["quantity"] == 0:
                        self.bill.remove(order_info)
                    return True
                else:
                    return False
        return False

    def get_subtotal(self):
        subtotal = 0
        for get_subtotal in self.bill:
            subtotal += get_subtotal["price"] * get_subtotal["quantity"]
        return subtotal

    def get_total(self):
        sum = 0
        for order_info in self.bill:
            sum += order_info["price"] * order_info["quantity"]
        return sum


