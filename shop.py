# INT240106710 / Ayberk Yahşi


print("Welcome to the my shop!")

# ürün 1
urun1 = input("Enter the name of the first item: ")
print("Name of the first item: ", urun1)

price1 = float(input("Enter the price of the first item: $"))
print("Price of the first item: ", price1)

quantity1 = int(input("Enter the quantity of the first item: "))
print("Quantity of the first item: ", quantity1)


# ürün 2
urun2 = input("Enter the name of the second item: ")
print("Name of the second item: ", urun2)

price2 = float(input("Enter the price of the second item: $"))
print("Price of the second item: ", price2)

quantity2 = int(input("Enter the quantity of the second item:"))
print("Quantity of the second item: ", quantity2)

# hesaplama
subtotal1 = price1 * quantity1
subtotal2 = price2 * quantity2
total_subtotal = subtotal1 + subtotal2

# vergi kısmı
tax = total_subtotal * 0.10
final_total = total_subtotal + tax

# fiş
print("---")
print("YOUR RECEIPT")
print(f"{urun1}: ${price1} x {quantity1} = ${subtotal1}")
print(f"{urun2}: ${price2} x {quantity2} = ${subtotal2}")
print("---")

print(f"Subtotal: ${total_subtotal:.2f}:")
print(f"Tax (10%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for shopping.")


