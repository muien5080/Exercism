"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    for recipe, updates in recipe_updates:
        ideas[recipe] = updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetical order."""
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information."""
    fulfillment = {}
    
    # reverse alphabetical order
    for item in sorted(cart.keys(), reverse=True):
        quantity = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        fulfillment[item] = [quantity, aisle, refrigerated]
    
    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, (qty, aisle, refrigerated) in fulfillment_cart.items():
        if item in store_inventory:
            store_qty = store_inventory[item][0]
            new_qty = store_qty - qty
            
            if new_qty <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_qty
    
    return store_inventory
    