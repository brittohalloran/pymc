import unittest
import monte_carlo as mc


class TestMonteCarlo(unittest.TestCase):
    def test_Norm(self):

        # Works normally
        a = mc.Norm(interval=(-1.645, 1.645))
        self.assertEqual(a.mean, 0)
        self.assertTrue(abs(a.sd - 1) < 0.005, a.sd)

        # Bad combination of inputs
        with self.assertRaises(Exception):
            a = mc.Norm(mean=0, interval=(0, 1))

        # Three number interval
        with self.assertRaises(Exception):
            a = mc.Norm(interval=(0, 1, 2))

        # One number interval
        with self.assertRaises(Exception):
            a = mc.Norm(interval=(0))

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()
