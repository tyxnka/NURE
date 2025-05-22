inventory = {
    "яблука": 10,
    "банани": 3,
    "морква": 7,
    "помідори": 2
}

def update_inventory(product, quantity):
    if product in inventory:
        inventory[product] += quantity
        if inventory[product] < 0:
            inventory[product] = 0
    else:
        inventory[product] = max(0, quantity)

update_inventory("банани", 5)
update_inventory("помідори", -1) #
update_inventory("огірки", 4)

low_stock = [product for product, qty in inventory.items() if qty < 5]

print("Інвентар:", inventory)
print("Продукти з кількістю менше 5:", low_stock)
