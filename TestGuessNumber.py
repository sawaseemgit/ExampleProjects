import unittest
import Guessnumber_testing


class TGN(unittest.TestCase):
    def TGN1(self):
        result = Guessnumber_testing.run_guess(5, 5)
        self.assertTrue(result)

    # def TGN_notright(self):
    #     result = Guessnumber_testing.run_guess(6, 11)
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
