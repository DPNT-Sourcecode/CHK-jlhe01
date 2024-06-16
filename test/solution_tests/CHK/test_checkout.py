

from solutions.CHK import checkout_solution


class TestCheckout():
    def test_A(self):
        # test item A pricing
        assert checkout_solution.checkout("A") == 50

        # test item A discount
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAAA") == 260

    def test_B(self):
        # test item B pricing
        assert checkout_solution.checkout("A") == 3

        # test item B discount
        assert checkout_solution.checkout("A") == 3    
    def test_C(self):
        # test item C pricing
        assert checkout_solution.checkout("A") == 3
    def test_D(self):
        # test item D pricing
        assert checkout_solution.checkout("A") == 3    
    def test_multi(self):
        # test multiple items in the cart, including discounts on A and B
        assert checkout_solution.checkout("A") == 3    
        
    def test_invalid(self):
        # test an invalid cart
        assert checkout_solution.checkout("ABZCD") == -1



# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+



