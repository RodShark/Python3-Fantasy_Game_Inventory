# Write a data structure to model a player's inventory in a fantasy video game.
# String values describing the item, integer value detailing how many of that item is in the player's inventory.

game_inventory = {
    "rope": 3,
    "tent": 5,
    "food": 8,
    "dagger": 2,
    "gold coin": 47,
    "bow": 1,
    "arrow": 30
}

# Write a function called display_inventory that would take any possible inventory item and display it like so:
#   Inventory:
#   12 arrows
#   42 gold coins
#   1 torch
#   Total number of items: 55


def display_inventory(inventory):
    print("Here are the items inside your inventory:")
    total = 0
    for item_name, item_amount in inventory.items():
        print("{} {}".format(str(item_amount), item_name))
        total += item_amount
    print("Your total items in your inventory comes out to: {} items.".format(str(total)))


display_inventory(game_inventory)

# Your character just killed a boss! Create a list that will represent the boss's loot table.
# Try an include an item more than once in the list.

boss_loot = ["gold coin", "sword", "gold coin", "ruby", "gold coin"]

print("\nYou just killed a boss, nice going! Here's the loot you get from that:\n")

for spoils in boss_loot:
    print("A {}".format(spoils))

print("\nNow here's what your inventory looks like.\n")

# Next, create a function named add_to_inventory(inventory, added_items) to add the boss's loot to your inventory.
# The function should return a dictionary that represents the updated inventory.


def add_to_inventory(loot_table, inventory):
    for item in loot_table:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = inventory.get(item, 1)  # Not working currently.

add_to_inventory(boss_loot, game_inventory)
display_inventory(game_inventory)
