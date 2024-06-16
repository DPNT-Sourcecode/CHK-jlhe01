from collections import Counter
import typing as t
from dataclasses import dataclass

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


# def discounted_price_calculator(
#     quantity: int,
#     original_price: int,
#     num_required_for_discount: int,
#     discount_bundle_price: int,
# ) -> int:
#     num_bundles = quantity // num_required_for_discount
#     num_leftover = quantity % num_required_for_discount
#     return (num_leftover * original_price) + (num_bundles * discount_bundle_price)


# def checkout(sku: str) -> int:
#     counts = Counter(sku) # returns a sorted dictionary of counts
#     total_cost = 0

#     for item, quantity in counts.items():
#         if item == "A":
#             # 5 multi discount (and possibly the 3 multi discount as well), its always better to use the 5 deal if you can
#             suggested_cost = (quantity // 5) * 200
#             suggested_cost += discounted_price_calculator(quantity=quantity % 5, original_price=50, num_required_for_discount=3, discount_bundle_price=130)
#             total_cost += suggested_cost
#         elif item == "B":
#             # always better to get a B free then possibly use the 2 multi discount
#             total_cost += discounted_price_calculator(quantity=quantity - counts.get('E', 0) // 2, original_price=30, num_required_for_discount=2, discount_bundle_price=45)
#         elif item == "C":
#             total_cost += 20 * quantity
#         elif item == "D":
#             total_cost += 15 * quantity
#         elif item == "E": # price E separately to the E logic in the B conditional as we always need to pay for anyway
#             total_cost += 40 * quantity
#         else:
#             return -1

#     return total_cost


# -----------------------
# ---- REQUIREMENT 3 ----
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
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+


# def checkout(sku: str) -> int:
#     counts = Counter(sku)  # returns a sorted dictionary of counts
#     total_cost = 0

#     for item, quantity in counts.items():
#         if item == "A":
#             # 5 multi discount (and possibly the 3 multi discount as well), its always better to use the 5 deal if you can
#             suggested_cost = (quantity // 5) * 200
#             suggested_cost += discounted_price_calculator(
#                 quantity=quantity % 5,
#                 original_price=50,
#                 num_required_for_discount=3,
#                 discount_bundle_price=130,
#             )
#             total_cost += suggested_cost
#         elif item == "B":
#             # always better to get a B free then possibly use the 2 multi discount
#             total_cost += discounted_price_calculator(
#                 quantity=quantity - counts.get("E", 0) // 2,
#                 original_price=30,
#                 num_required_for_discount=2,
#                 discount_bundle_price=45,
#             )
#         elif item == "C":
#             total_cost += 20 * quantity
#         elif item == "D":
#             total_cost += 15 * quantity
#         elif (
#             item == "E"
#         ):  # price E separately to the E logic in the B conditional as we always need to pay for anyway
#             total_cost += 40 * quantity
#         elif item == "F":
#             total_cost += discounted_price_calculator(
#                 quantity=quantity,
#                 original_price=10,
#                 num_required_for_discount=3,
#                 discount_bundle_price=20,
#             )
#         else:
#             return -1

#     return total_cost


# -----------------------
# ---- REQUIREMENT 4 ----
# -----------------------

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+


@dataclass
class FreeItemDeal:
    item_to_buy: str
    required_quantity: int


@dataclass(order=True)
class BundleDeal:
    size: int
    bundle_price: int


class ItemPricing:
    def __init__(
        self,
        item: str,
        original_price: int,
        bundle_deals: t.Optional[t.List[BundleDeal]] = None,
        free_item_deal: t.Optional[FreeItemDeal] = None,
    ):
        self.item = item
        self.item_original_price = original_price
        self.bundle_deals = bundle_deals
        self.free_item_deal = free_item_deal

    def calculate_cost(self, quantities: t.Dict[str, int]) -> int:
        quantity = quantities[self.item]
        if self.free_item_deal:
            quantity -= (
                quantities.get(self.free_item_deal.item_to_buy, 0)
                // self.free_item_deal.required_quantity
            )

        cost = 0
        if self.bundle_deals:
            for deal in sorted(self.bundle_deals, reverse=True):
                num_bundles = quantity // deal.size
                cost += num_bundles * deal.bundle_price
                quantity = quantity % deal.size

        return cost + (quantity * self.item_original_price)


pricing_mapping = {
    "A": ItemPricing("A", 50, [BundleDeal(3, 130), BundleDeal(5, 200)]),
    "B": ItemPricing("B", 30, [BundleDeal(2, 45)], FreeItemDeal("E", 2)),
    "C": ItemPricing("C", 20),
    "D": ItemPricing("D", 15),
    "E": ItemPricing("E", 40),
    "F": ItemPricing("F", 10, [BundleDeal(3, 20)]),
    "G": ItemPricing("G", 20),
    "H": ItemPricing("H", 10, [BundleDeal(5, 45), BundleDeal(10, 80)]),
    "I": ItemPricing("I", 35),
    "J": ItemPricing("J", 60),
    "K": ItemPricing("K", 80, [BundleDeal(2, 150)]),
    "L": ItemPricing("L", 90),
    "M": ItemPricing("M", 15, None, FreeItemDeal("N", 3)),
    "N": ItemPricing("N", 40),
    "O": ItemPricing("O", 10),
    "P": ItemPricing("P", 50, [BundleDeal(5, 200)]),
    "Q": ItemPricing("Q", 30, [BundleDeal(3, 80)], FreeItemDeal("R", 3)),
    "R": ItemPricing("R", 50),
    "S": ItemPricing("S", 30),
    "T": ItemPricing("T", 20),
    "U": ItemPricing("U", 40, [BundleDeal(4, 120)]),
    "V": ItemPricing("V", 50, [BundleDeal(2, 90), BundleDeal(3, 130)]),
    "W": ItemPricing("W", 20),
    "X": ItemPricing("X", 90),
    "Y": ItemPricing("Y", 10),
    "Z": ItemPricing("Z", 50),
}


def checkout(sku: str) -> int:
    counts = Counter(sku)
    total_cost = 0
    for item in counts.keys():
        if item.isupper():
            total_cost += pricing_mapping[item].calculate_cost(counts)
        else:
            return -1
    return total_cost

