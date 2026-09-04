# create a class zomato with attributes
# class attributes: discount,coupon_code and list of all rest_names
# instance attributes: rest_name,dictionary of items,rest_id
# now, calculate rest_id based on another class variable restaurent number.
# create a function variable rest_number. create a function order which
# takes an item number as input and checks wheather the user entered a
# valid id and prints the final bill if they entered coupan code correctly
# with discount
class Zomato:
    discount = 10
    coupon_code = "ZOMATO10"
    rest_names = []
    rest_number = 0

    def __init__(self, rest_name, items):
        self.rest_name = rest_name
        self.items = items
        Zomato.rest_number += 1
        self.rest_id = Zomato.rest_number
        Zomato.rest_names.append(rest_name)

    def order(self, item_number, coupon=None):
        if item_number not in self.items:
            print("Invalid item number!")
            return

        bill = self.items[item_number]
        print(f"Base price: {bill}")

        if coupon == Zomato.coupon_code:
            discount_amount = (Zomato.discount / 100) * bill
            bill -= discount_amount
            print(f"Coupon applied! Discount: {discount_amount}")
        else:
            if coupon:
                print("Invalid coupon code!")

        print(f"Final bill: {bill}")


items1 = {1: 200, 2: 150, 3: 300}
rest1 = Zomato("Spicy House", items1)

items2 = {1: 100, 2: 250}
rest2 = Zomato("Sweet Corner", items2)

print("Restaurant IDs:", rest1.rest_id, rest2.rest_id)
print("All restaurants:", Zomato.rest_names)

rest1.order(1, "ZOMATO10")
rest2.order(2, "WRONGCODE")
rest2.order(5)
