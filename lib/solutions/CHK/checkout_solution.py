
from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(sku: str) -> int:
    counts = Counter(sku)
    total_cost = 0
    for item, quantity in counts.items():
        if item == "A":
            num_bundles = quantity // 3
            num_leftover =  quantity % 3
            total_cost += (num_leftover * 50) + (num_bundles * 130) 
        elif item == "B":
            pass
        elif item == "C":
            total_cost += 20 * quantity
        elif item == "D":
            total_cost += 15 * quantity
        else:
            return -1 
    
    return total_cost



# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+





