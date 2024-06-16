
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
# def checkout(sku: str) -> int:
#     counts = Counter(sku)
#     total_cost = 0
#     for item, quantity in counts.items():
#         if item == "A":
#             num_bundles = quantity // 3
#             num_leftover =  quantity % 3
#             total_cost += (num_leftover * 50) + (num_bundles * 130) 
#         elif item == "B":
#             num_bundles = quantity // 2
#             num_leftover =  quantity % 2
#             total_cost += (num_leftover * 30) + (num_bundles * 45)         
#         elif item == "C":
#             total_cost += 20 * quantity
#         elif item == "D":
#             total_cost += 15 * quantity
#         else:
#             return -1 
    
#     return total_cost


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
            # 5 multi discount (and possibly the 3 multi discount as well), its always better to use the 5 deal if you can
            suggested_cost = (quantity // 5) * 200
            suggested_cost += discounted_price_calculator(quantity=quantity % 5, original_price=50, num_required_for_discount=3, discount_bundle_price=130)
            total_cost += suggested_cost
        elif item == "B":
            # always better to get a B free then possibly use the 2 multi discount
            total_cost += discounted_price_calculator(quantity=quantity - counts.get('E', 0) // 2, original_price=30, num_required_for_discount=2, discount_bundle_price=45)
        elif item == "C":
            total_cost += 20 * quantity
        elif item == "D":
            total_cost += 15 * quantity
        elif item == "E": # price E separately to the E logic in the B conditional as we always need to pay for anyway
            total_cost += 40 * quantity
        else:
            return -1 
    
    return total_cost

