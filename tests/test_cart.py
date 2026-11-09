import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            res = cart.add_digital_video_disc(DigitalVideoDisc(f"DVD {i}", cost=10.0))
            self.assertTrue(res)
        
        # Dia thu 21 phai bi tu choi (tra ve False)
        res_21 = cart.add_digital_video_disc(DigitalVideoDisc("DVD 21", cost=10.0))
        self.assertFalse(res_21)

if __name__ == '__main__':
    unittest.main()
