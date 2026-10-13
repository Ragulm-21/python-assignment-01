# Q3: Online Shopping Discount Eligibility

# 1. Accept order amount and membership status
order_amount = float(input("Enter the order amount (Rs): "))
membership = input("Are you a member? (yes/no): ")

# 2. Handle membership input without case sensitivity (also ignore stray spaces)
is_member = membership.strip().lower() == "yes"

# 3. Validate the order amount: must be between 0 and 1,00,000 (inclusive)
is_valid_amount = order_amount >= 0 and order_amount <= 100000

# 4. Decide the discount percentage
if not is_valid_amount:
    print("Invalid order amount. It must be between Rs 0 and Rs 1,00,000.")
else:
    if order_amount >= 5000:
        discount_percent = 15
        status = "Eligible: 15% discount for orders of Rs 5,000 or more"
    elif is_member and order_amount >= 2000:      # here amount is < 5000
        discount_percent = 10
        status = "Eligible: 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for a discount"

    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    # 5. Display the results
    print("Original amount :", order_amount)
    print("Discount        :", discount_percent, "%")
    print("Discount amount :", discount_amount)
    print("Final payable   :", final_amount)
    print("Status          :", status)
