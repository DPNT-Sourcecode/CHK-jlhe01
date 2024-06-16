

from solutions.CHK import checkout_solution


class TestCheckout():
    def test_A(self):
        assert checkout_solution.checkout("") == 3
    def test_B(self):
        assert checkout_solution.checkout("") == 3
    def test_C(self):
        assert checkout_solution.checkout("") == 3
    def test_D(self):
        assert checkout_solution.checkout("") == 3
    def test_multi(self):
        assert checkout_solution.checkout("") == 3
    def test_invalid(self):
        assert checkout_solution.checkout("") == 3



# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


