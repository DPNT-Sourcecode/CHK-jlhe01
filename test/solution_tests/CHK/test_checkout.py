from solutions.CHK import checkout_solution
import string

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


# class TestCheckout:
#     def test_A(self):
#         # test item A pricing
#         assert checkout_solution.checkout("A") == 50

#         # test item A multi discount
#         assert checkout_solution.checkout("AAA") == 130
#         assert checkout_solution.checkout("AAAAA") == 200
#         assert checkout_solution.checkout("AAAAAA") == 250
#         assert checkout_solution.checkout("AAAAAAAA") == 330  # 200 + 130

#     def test_B(self):
#         # test item B pricing
#         assert checkout_solution.checkout("B") == 30

#         # test item B multi (discount)
#         assert checkout_solution.checkout("BB") == 45
#         assert checkout_solution.checkout("BBBB") == 90
#         assert checkout_solution.checkout("BBBBB") == 120

#         # test item B with E's (no discount)
#         assert checkout_solution.checkout("BE") == 70  # 30 + 40
#         assert checkout_solution.checkout("BBE") == 85  # 45 + 40

#         # test item B with multiple E's (discounts!)
#         assert checkout_solution.checkout("BEE") == 80  # 0 + 80
#         assert checkout_solution.checkout("BBEE") == 110  # 30 + 2*40
#         assert checkout_solution.checkout("BBBEE") == 125  # 45 + 2*40
#         assert checkout_solution.checkout("BBEEE") == 150  # 30 + 3*40
#         assert checkout_solution.checkout("BBEEEE") == 160  # 0 + 4*40

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

#     def test_G(self):
#         # test item G pricing
#         assert checkout_solution.checkout("G") == 20

#         # test item G multi (no discount)
#         assert checkout_solution.checkout("GG") == 40

#     def test_H(self):
#         # test item H pricing
#         assert checkout_solution.checkout("H") == 10

#         # test item H multi discount
#         assert checkout_solution.checkout("HHHHH") == 45
#         assert checkout_solution.checkout("HHHHHHHHHH") == 80
#         assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125  # 80 + 45

#     def test_I(self):
#         # test item I pricing
#         assert checkout_solution.checkout("I") == 35

#         # test item I multi (no discount)
#         assert checkout_solution.checkout("II") == 70

#     def test_J(self):
#         # test item J pricing
#         assert checkout_solution.checkout("J") == 60

#         # test item J multi (no discount)
#         assert checkout_solution.checkout("JJ") == 120

#     def test_K(self):
#         # test item K pricing
#         assert checkout_solution.checkout("K") == 80

#         # test item K multi (discount)
#         assert checkout_solution.checkout("KK") == 150
#         assert checkout_solution.checkout("KKK") == 230
#         assert checkout_solution.checkout("KKKK") == 300

#     def test_L(self):
#         # test item L pricing
#         assert checkout_solution.checkout("L") == 90

#         # test item L multi (no discount)
#         assert checkout_solution.checkout("LL") == 180

#     def test_M(self):
#         # test item M pricing
#         assert checkout_solution.checkout("M") == 15

#         # test item M multi (no discount)
#         assert checkout_solution.checkout("MM") == 30

#         # test item M with N's (no discount)
#         assert checkout_solution.checkout("MNN") == 95  # 15 + 2*40

#         # test item M with multiple N's (discounts!)
#         assert checkout_solution.checkout("MNNN") == 120  # 0 + 3*40
#         assert checkout_solution.checkout("MMNNN") == 135  # 15 + 3*40
#         assert checkout_solution.checkout("MMNNNN") == 175  # 15 + 4*40
#         assert checkout_solution.checkout("MMNNNNNN") == 240  # 0 + 6*40

#     def test_N(self):
#         # test item N pricing
#         assert checkout_solution.checkout("N") == 40
#         # test item N multi (no discount)
#         assert checkout_solution.checkout("NN") == 80

#     def test_O(self):
#         # test item O pricing
#         assert checkout_solution.checkout("O") == 10
#         # test item O multi (no discount)
#         assert checkout_solution.checkout("OO") == 20

#     def test_P(self):
#         # test item P pricing
#         assert checkout_solution.checkout("P") == 50

#         # test item P multi discount
#         assert checkout_solution.checkout("PPPPP") == 200
#         assert checkout_solution.checkout("PPPPPP") == 250
#         assert checkout_solution.checkout("PPPPPPPPPP") == 400

#     def test_Q(self):
#         # test item Q pricing
#         assert checkout_solution.checkout("Q") == 30

#         # test item Q multi discount
#         assert checkout_solution.checkout("QQQ") == 80
#         assert checkout_solution.checkout("QQQQ") == 110
#         assert checkout_solution.checkout("QQQQQQ") == 160

#         # test item Q with R's (no discount)
#         assert checkout_solution.checkout("QR") == 80  # 30 + 50
#         assert checkout_solution.checkout("QQQR") == 130  # 80 + 50

#         # test item Q with multiple R's (discounts!)
#         assert checkout_solution.checkout("QRRR") == 150  # 0 + 3*50
#         assert checkout_solution.checkout("QQQRRR") == 210  # 2*30 + 0 + 3*50
#         assert checkout_solution.checkout("QQQQRRR") == 230  # 80 + 0 + 3*50
#         assert checkout_solution.checkout("QQQRRRR") == 260  # 2*30 + 0 + 4*50
#         assert checkout_solution.checkout("QQQRRRRRRRRR") == 450  # 0 + 9*50

#     def test_R(self):
#         # test item R pricing
#         assert checkout_solution.checkout("R") == 50
#         # test item R multi (no discount)
#         assert checkout_solution.checkout("RR") == 100

#     def test_S(self):
#         # test item S pricing
#         assert checkout_solution.checkout("S") == 30
#         # test item S multi (no discount)
#         assert checkout_solution.checkout("SS") == 60

#     def test_T(self):
#         # test item T pricing
#         assert checkout_solution.checkout("T") == 20
#         # test item T multi (no discount)
#         assert checkout_solution.checkout("TT") == 40

#     def test_U(self):
#         # test item U pricing
#         assert checkout_solution.checkout("U") == 40
#         # test item U multi discount
#         assert checkout_solution.checkout("UUUU") == 120
#         assert checkout_solution.checkout("UUUUUUUU") == 240
#         assert checkout_solution.checkout("UUUUUU") == 200  # 120 + 2*40

#     def test_V(self):
#         # test item V pricing
#         assert checkout_solution.checkout("V") == 50
#         # test item V multi discount
#         assert checkout_solution.checkout("VV") == 90
#         assert checkout_solution.checkout("VVV") == 130
#         assert checkout_solution.checkout("VVVVV") == 220  # 90 + 130
#         assert checkout_solution.checkout("VVVVVV") == 260

#     def test_W(self):
#         # test item W pricing
#         assert checkout_solution.checkout("W") == 20
#         # test item W multi (no discount)
#         assert checkout_solution.checkout("WW") == 40

#     def test_X(self):
#         # test item X pricing
#         assert checkout_solution.checkout("X") == 90
#         # test item X multi (no discount)
#         assert checkout_solution.checkout("XX") == 180

#     def test_Y(self):
#         # test item Y pricing
#         assert checkout_solution.checkout("Y") == 10
#         # test item Y multi (no discount)
#         assert checkout_solution.checkout("YY") == 20

#     def test_Z(self):
#         # test item Z pricing
#         assert checkout_solution.checkout("Z") == 50
#         # test item Z multi (no discount)
#         assert checkout_solution.checkout("ZZ") == 100

#     def test_multi(self):
#         # test multiple items in the cart, including discounted items
#         # expected result:  sum of all prices
#         assert checkout_solution.checkout(string.ascii_uppercase) == 965

#     def test_invalid(self):
#         # test an invalid cart
#         assert checkout_solution.checkout("ABC1DEF") == -1  # with a digit
#         assert checkout_solution.checkout("ABCaDEF") == -1  # with a letter case letter


# -----------------------
# ---- REQUIREMENT 5 ----
# -----------------------

# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+


class TestCheckout:

    def test_group(self):
        # test one of each
        assert checkout_solution.checkout("STXYZ") == 82  # 45 + 20 + 17

        # test multiples
        assert checkout_solution.checkout("STXYZZST") == 127  # 2*45 + 20 + 17

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

    def test_G(self):
        # test item G pricing
        assert checkout_solution.checkout("G") == 20

        # test item G multi (no discount)
        assert checkout_solution.checkout("GG") == 40

    def test_H(self):
        # test item H pricing
        assert checkout_solution.checkout("H") == 10

        # test item H multi discount
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125  # 80 + 45

    def test_I(self):
        # test item I pricing
        assert checkout_solution.checkout("I") == 35

        # test item I multi (no discount)
        assert checkout_solution.checkout("II") == 70

    def test_J(self):
        # test item J pricing
        assert checkout_solution.checkout("J") == 60

        # test item J multi (no discount)
        assert checkout_solution.checkout("JJ") == 120

    def test_K(self):
        # test item K pricing
        assert checkout_solution.checkout("K") == 70

        # test item K multi (discount)
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKK") == 190
        assert checkout_solution.checkout("KKKK") == 240

    def test_L(self):
        # test item L pricing
        assert checkout_solution.checkout("L") == 90

        # test item L multi (no discount)
        assert checkout_solution.checkout("LL") == 180

    def test_M(self):
        # test item M pricing
        assert checkout_solution.checkout("M") == 15

        # test item M multi (no discount)
        assert checkout_solution.checkout("MM") == 30

        # test item M with N's (no discount)
        assert checkout_solution.checkout("MNN") == 95  # 15 + 2*40

        # test item M with multiple N's (discounts!)
        assert checkout_solution.checkout("MNNN") == 120  # 0 + 3*40
        assert checkout_solution.checkout("MMNNN") == 135  # 15 + 3*40
        assert checkout_solution.checkout("MMNNNN") == 175  # 15 + 4*40
        assert checkout_solution.checkout("MMNNNNNN") == 240  # 0 + 6*40

    def test_N(self):
        # test item N pricing
        assert checkout_solution.checkout("N") == 40
        # test item N multi (no discount)
        assert checkout_solution.checkout("NN") == 80

    def test_O(self):
        # test item O pricing
        assert checkout_solution.checkout("O") == 10
        # test item O multi (no discount)
        assert checkout_solution.checkout("OO") == 20

    def test_P(self):
        # test item P pricing
        assert checkout_solution.checkout("P") == 50

        # test item P multi discount
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("PPPPPP") == 250
        assert checkout_solution.checkout("PPPPPPPPPP") == 400

    def test_Q(self):
        # test item Q pricing
        assert checkout_solution.checkout("Q") == 30

        # test item Q multi discount
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("QQQQ") == 110
        assert checkout_solution.checkout("QQQQQQ") == 160

        # test item Q with R's (no discount)
        assert checkout_solution.checkout("QR") == 80  # 30 + 50
        assert checkout_solution.checkout("QQQR") == 130  # 80 + 50

        # test item Q with multiple R's (discounts!)
        assert checkout_solution.checkout("QRRR") == 150  # 0 + 3*50
        assert checkout_solution.checkout("QQQRRR") == 210  # 2*30 + 0 + 3*50
        assert checkout_solution.checkout("QQQQRRR") == 230  # 80 + 0 + 3*50
        assert checkout_solution.checkout("QQQRRRR") == 260  # 2*30 + 0 + 4*50
        assert checkout_solution.checkout("QQQRRRRRRRRR") == 450  # 0 + 9*50

    def test_R(self):
        # test item R pricing
        assert checkout_solution.checkout("R") == 50
        # test item R multi (no discount)
        assert checkout_solution.checkout("RR") == 100

    def test_S(self):
        # test item S pricing
        assert checkout_solution.checkout("S") == 20
        # test item S multi (no discount)
        assert checkout_solution.checkout("SS") == 40

    def test_T(self):
        # test item T pricing
        assert checkout_solution.checkout("T") == 20
        # test item T multi (no discount)
        assert checkout_solution.checkout("TT") == 40

    def test_U(self):
        # test item U pricing
        assert checkout_solution.checkout("U") == 40
        # test item U multi discount
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUUUUU") == 240
        assert checkout_solution.checkout("UUUUUU") == 200  # 120 + 2*40

    def test_V(self):
        # test item V pricing
        assert checkout_solution.checkout("V") == 50
        # test item V multi discount
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VVVVV") == 220  # 90 + 130
        assert checkout_solution.checkout("VVVVVV") == 260

    def test_W(self):
        # test item W pricing
        assert checkout_solution.checkout("W") == 20
        # test item W multi (no discount)
        assert checkout_solution.checkout("WW") == 40

    def test_X(self):
        # test item X pricing
        assert checkout_solution.checkout("X") == 90
        # test item X multi (no discount)
        assert checkout_solution.checkout("XX") == 180

    def test_Y(self):
        # test item Y pricing
        assert checkout_solution.checkout("Y") == 10
        # test item Y multi (no discount)
        assert checkout_solution.checkout("YY") == 20

    def test_Z(self):
        # test item Z pricing
        assert checkout_solution.checkout("Z") == 50
        # test item Z multi (no discount)
        assert checkout_solution.checkout("ZZ") == 100

    def test_multi(self):
        # test multiple items in the cart, including discounted items
        # expected result:  853 (sum of all prices) - 21 (price of Z) - 20 (price of S) - 20 (price of T) + 45 (price of one group)
        assert checkout_solution.checkout(string.ascii_uppercase) == 837

    def test_invalid(self):
        # test an invalid cart
        assert checkout_solution.checkout("ABC1DEF") == -1  # with a digit
        assert checkout_solution.checkout("ABCaDEF") == -1  # with a letter case letter




