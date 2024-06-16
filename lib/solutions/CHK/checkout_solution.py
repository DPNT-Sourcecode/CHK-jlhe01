
from collections import Counter

# -----------------------
# ---- REQUIREMENT 1 ----
# -----------------------

# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

# noinspection PyUnusedLocal
# skus = unicode string
def checkout_R1(sku: str) -> int:
    counts = Counter(sku)
    total_cost = 0
    for item, quantity in counts.items():
        if item == "A":
            num_bundles = quantity // 3
            num_leftover =  quantity % 3
            total_cost += (num_leftover * 50) + (num_bundles * 130) 
        elif item == "B":
            num_bundles = quantity // 2
            num_leftover =  quantity % 2
            total_cost += (num_leftover * 30) + (num_bundles * 45)         
        elif item == "C":
            total_cost += 20 * quantity
        elif item == "D":
            total_cost += 15 * quantity
        else:
            return -1 
    
    return total_cost


# -----------------------
# ---- REQUIREMENT 2 ----
# -----------------------

# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

# noinspection PyUnusedLocal
# skus = unicode string

def discounted_price_calculator(quantity: int, original_price: int, num_required_for_discount: int, discount_bundle_price: int) -> int:
    num_bundles = quantity // num_required_for_discount
    num_leftover =  quantity % num_required_for_discount
    return (num_leftover * original_price) + (num_bundles * discount_bundle_price)

def checkout(sku: str) -> int:
    counts = Counter(sku) # returns a sorted dictionary of counts
    total_cost = 0
    for item, quantity in counts.items():
        if item == "A":
            # 3 multi discount
            suggested_cost_3_bundle = discounted_price_calculator(quantity=quantity, original_price=50, num_required_for_discount=3, discount_bundle_price=130)

            # 5 multi discount (and possibly the 3 multi discount as well)
            suggested_cost_5_bundle = (quantity // 5) * 200
            suggested_cost_5_bundle += discounted_price_calculator(quantity=quantity % 5, original_price=50, num_required_for_discount=3, discount_bundle_price=130)

            suggested_cost = min(suggested_cost_3_bundle, suggested_cost_5_bundle)

            # add whichever gives the best deal i.e. favours the customers
            total_cost += suggested_cost

        elif item == "B":
            num_free = counts.get('E', 0) // 2 # always better to get a B free then possibly use the discount
            new_quantity = quantity - num_free
            num_bundles = new_quantity // 2
            num_leftover =  new_quantity % 2
            total_cost += (num_leftover * 30) + (num_bundles * 45)         
        elif item == "C":
            total_cost += 20 * quantity
        elif item == "D":
            total_cost += 15 * quantity
        elif item == "E": # price E separately to the E logic in the B conditional as we always need to pay for anyway
            total_cost += 40 * quantity
        else:
            return -1 
    
    return total_cost

