

from solutions.CHK import checkout_solution


# -----------------------
# ---- REQUIREMENT 1 ----
# -----------------------

# class TestCheckoutR1():
#     def test_A(self):
#         # test item A pricing
#         assert checkout_solution.checkout("A") == 50

#         # test item A multi (discount)
#         assert checkout_solution.checkout("AAA") == 130
#         assert checkout_solution.checkout("AAAAAA") == 260
#         assert checkout_solution.checkout("AAAAAAAA") == 360

#     def test_B(self):
#         # test item B pricing
#         assert checkout_solution.checkout("B") == 30

#         # test item B multi (discount)
#         assert checkout_solution.checkout("BB") == 45
#         assert checkout_solution.checkout("BBBB") == 90
#         assert checkout_solution.checkout("BBBBB") == 120
#     def test_C(self):
#         # test item C pricing
#         assert checkout_solution.checkout("C") == 20

#         # test item C multi (no discount)
#         assert checkout_solution.checkout("CC") == 40

#     def test_D(self):
#         # test item D pricing
#         assert checkout_solution.checkout("D") == 15

#         # test item D multi (no discount)
#         assert checkout_solution.checkout("DD") == 30
    
#     def test_multi(self):
#         # test multiple items in the cart, including discounts on A and B
#         # expected result: 130 + 45 + 40 + 30 
#         assert checkout_solution.checkout("ABCDABCDA") == 245   
        
#     def test_invalid(self):
#         # test an invalid cart
#         assert checkout_solution.checkout("ABZCD") == -1


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


class TestCheckout():
    def test_discounted_price_calculator():
        assert checkout_solution.discounted_price_calculator(quantity=2, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 45
        assert checkout_solution.discounted_price_calculator(quantity=4, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 90
        assert checkout_solution.discounted_price_calculator(quantity=5, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 120

    def test_A(self): # TODO
        # test item A pricing
        assert checkout_solution.checkout("A") == 50

        # test item A where 3 multi discount is always cheaper (even though sometimes 5 multi might be available)
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAAA") == 260
        assert checkout_solution.checkout("AAAAAAAA") == 360

        # test item A 5 multi (discount)



    def test_B(self): # TODO
        # test item B pricing
        assert checkout_solution.checkout("B") == 30

        # test item B multi (discount)
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120
    
    def test_C(self):
        # test item C pricing
        assert checkout_solution.checkout("C") == 20

        # test item C multi (no discount)
        assert checkout_solution.checkout("CC") == 40

    def test_D(self):
        # test item D pricing
        assert checkout_solution.checkout("D") == 15

        # test item D multi (no discount)
        assert checkout_solution.checkout("DD") == 30

    def test_E(self):
        # test item E pricing
        assert checkout_solution.checkout("E") == 40

        # test item E multi (no discount)
        assert checkout_solution.checkout("EE") == 80   
    
    def test_multi(self): # TODO
        # test multiple items in the cart, including discounts on A and B
        # expected result: ?
        assert checkout_solution.checkout("ABCDABCDA") == 245   
        
    def test_invalid(self):
        # test an invalid cart
        assert checkout_solution.checkout("ABZCDE") == -1



