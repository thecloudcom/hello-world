def manager(offer):
    return lambda total_mrp:total_mrp*(1-offer/100)

manager_id="Manager"
manager_pwd="M"
attempt_count=3

# Initialize variables BEFORE the loop
discount_percent = 0  # Default 0% discount
billing_formula = None  # Initialize as None

while attempt_count>0:
    m_id = input("Please enter your manager ID: ")
    m_pwd = input("Please enter your password:  ")

    if m_id == manager_id and m_pwd == manager_pwd:
        discount_percent=int(input("Please enter your discount percent: "))
        billing_formula=manager(discount_percent)
        print("Discount percentage: ",discount_percent,"%")
        break
    else:
        attempt_count -= 1
        print(f"Wrong ID or password. Attempts left: {attempt_count}")

product_dict={ "Apple": 50,"Banana": 10,"Milk": 30,"Bread": 25,"Eggs": 60,"Rice": 80}
print(product_dict)
orders=[]
while True:
    product_name=input("Please enter your product name: ")
    if product_name not in product_dict:
        print("Product not available")
        continue
    product_quantity = int(input("Please enter your product quantity: "))
    product_price = product_dict[product_name]
    orders.append((product_name,product_quantity,product_price))
    print(f"Added {product_name} and {product_quantity}to your orders")
    order_continue=input("Press 'c' to continue or 's' to stop \n")
    if order_continue.lower()=="s":
        break
print("Final Bill")
total_bill=0
for product_name,product_quantity,product_price in orders:
    total=product_quantity*product_price
    total_bill+=total
    print(f"{product_name} = {product_price} x {product_quantity} = ${total}")
print(f"Total Bill: ${total_bill}")

if billing_formula is not None:  # Check if manager logged in and created the function
    final_amount = billing_formula(total_bill)  # Call the lambda function
    print(f"After {discount_percent}% discount: ${final_amount}")
else:
    print("No manager discount applied.")
    print(f"Final amount to pay: ${total_bill}")












