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


# class TestCheckout():
#     def test_discounted_price_calculator(self):
#         assert checkout_solution.discounted_price_calculator(quantity=2, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 45
#         assert checkout_solution.discounted_price_calculator(quantity=4, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 90
#         assert checkout_solution.discounted_price_calculator(quantity=5, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 120

#     def test_A(self):
#         # test item A pricing
#         assert checkout_solution.checkout("A") == 50

#         # test item A multi discount
#         assert checkout_solution.checkout("AAA") == 130
#         assert checkout_solution.checkout("AAAAA") == 200
#         assert checkout_solution.checkout("AAAAAA") == 250
#         assert checkout_solution.checkout("AAAAAAAA") == 330 # 200 + 130

#     def test_B(self):
#         # test item B pricing
#         assert checkout_solution.checkout("B") == 30

#         # test item B multi (discount)
#         assert checkout_solution.checkout("BB") == 45
#         assert checkout_solution.checkout("BBBB") == 90
#         assert checkout_solution.checkout("BBBBB") == 120

#         # test item B with E's (no discount)
#         assert checkout_solution.checkout("BE") == 70 # 30 + 40
#         assert checkout_solution.checkout("BBE") == 85 # 45 + 40

#         # test item B with multiple E's (discounts!)
#         assert checkout_solution.checkout("BEE") ==  80 # 0 + 80
#         assert checkout_solution.checkout("BBEE") ==  110 # 30 + 2*40
#         assert checkout_solution.checkout("BBBEE") ==  125 # 45 + 2*40
#         assert checkout_solution.checkout("BBEEE") ==  150 # 30 + 3*40
#         assert checkout_solution.checkout("BBEEEE") ==  160 # 0 + 4*40


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

#     def test_E(self):
#         # test item E pricing
#         assert checkout_solution.checkout("E") == 40

#         # test item E multi (no discount)
#         assert checkout_solution.checkout("EE") == 80

#     def test_multi(self):
#         # test multiple items in the cart, including discounts on A and B
#         # expected result: # 130 + 45 + 40 + 30 + 80
#         assert checkout_solution.checkout("ABCDEABCDEAB") == 325

#     def test_invalid(self):
#         # test an invalid cart
#         assert checkout_solution.checkout("ABZCDE") == -1


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

# class TestCheckout():
#     def test_discounted_price_calculator(self):
#         assert checkout_solution.discounted_price_calculator(quantity=2, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 45
#         assert checkout_solution.discounted_price_calculator(quantity=4, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 90
#         assert checkout_solution.discounted_price_calculator(quantity=5, original_price=30, num_required_for_discount=2, discount_bundle_price=45) == 120

#     def test_A(self):
#         # test item A pricing
#         assert checkout_solution.checkout("A") == 50

#         # test item A multi discount
#         assert checkout_solution.checkout("AAA") == 130
#         assert checkout_solution.checkout("AAAAA") == 200
#         assert checkout_solution.checkout("AAAAAA") == 250
#         assert checkout_solution.checkout("AAAAAAAA") == 330 # 200 + 130

#     def test_B(self):
#         # test item B pricing
#         assert checkout_solution.checkout("B") == 30

#         # test item B multi (discount)
#         assert checkout_solution.checkout("BB") == 45
#         assert checkout_solution.checkout("BBBB") == 90
#         assert checkout_solution.checkout("BBBBB") == 120

#         # test item B with E's (no discount)
#         assert checkout_solution.checkout("BE") == 70 # 30 + 40
#         assert checkout_solution.checkout("BBE") == 85 # 45 + 40

#         # test item B with multiple E's (discounts!)
#         assert checkout_solution.checkout("BEE") ==  80 # 0 + 80
#         assert checkout_solution.checkout("BBEE") ==  110 # 30 + 2*40
#         assert checkout_solution.checkout("BBBEE") ==  125 # 45 + 2*40
#         assert checkout_solution.checkout("BBEEE") ==  150 # 30 + 3*40
#         assert checkout_solution.checkout("BBEEEE") ==  160 # 0 + 4*40


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

#     def test_E(self):
#         # test item E pricing
#         assert checkout_solution.checkout("E") == 40

#         # test item E multi (no discount)
#         assert checkout_solution.checkout("EE") == 80

#     def test_F(self):
#         # test item F pricing
#         assert checkout_solution.checkout("F") == 10

#         # test item F multi discount
#         assert checkout_solution.checkout("FFF") == 20
#         assert checkout_solution.checkout("FFFFF") == 40
#         assert checkout_solution.checkout("FFFFFF") == 40
#         assert checkout_solution.checkout("FFFFFFF") == 50

#     def test_multi(self):
#         # test multiple items in the cart, including discounts on A and B
#         # expected result: # 130 + 45 + 40 + 30 + 80
#         assert checkout_solution.checkout("ABCDEFABCDEFABF") == 345


#     def test_invalid(self):
#         # test an invalid cart
#         assert checkout_solution.checkout("ABZCDEF") == -1


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


class TestCheckout:

    def test_A(self):
        # test item A pricing
        assert checkout_solution.checkout("A") == 50

        # test item A multi discount
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAAA") == 330  # 200 + 130

    def test_B(self):
        # test item B pricing
        assert checkout_solution.checkout("B") == 30

        # test item B multi (discount)
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120

        # test item B with E's (no discount)
        assert checkout_solution.checkout("BE") == 70  # 30 + 40
        assert checkout_solution.checkout("BBE") == 85  # 45 + 40

        # test item B with multiple E's (discounts!)
        assert checkout_solution.checkout("BEE") == 80  # 0 + 80
        assert checkout_solution.checkout("BBEE") == 110  # 30 + 2*40
        assert checkout_solution.checkout("BBBEE") == 125  # 45 + 2*40
        assert checkout_solution.checkout("BBEEE") == 150  # 30 + 3*40
        assert checkout_solution.checkout("BBEEEE") == 160  # 0 + 4*40

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

    def test_F(self):
        # test item F pricing
        assert checkout_solution.checkout("F") == 10

        # test item F multi discount
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_multi(self):
        # test multiple items in the cart, including discounts on A and B
        # expected result: # 130 + 45 + 40 + 30 + 80
        assert checkout_solution.checkout("ABCDEFABCDEFABF") == 345

    def test_invalid(self):
        # test an invalid cart
        assert checkout_solution.checkout("ABC1DEF") == -1


