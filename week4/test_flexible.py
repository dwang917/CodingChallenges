import unittest
import flexible_space

class flexibleSpaceTest(unittest.TestCase):
  def run_cases(self, cases):
        for case in cases:
            actual = flexible_space.solve_spaces(case[0], case[1])
            self.assertEqual(
                actual, case[2], f"Expected checkboard={case[0]}, {case[1]} to produce {case[2]} but got {actual}")

  def test_flexible(self):
    #test cases for the examples and the smallest edge case, also not sure if there's a better way to feed the input
    cases = [
      (10, [1,4,8], [1, 2, 3, 4, 6, 7, 8, 9, 10]),
      (6, [2, 5], [1, 2, 3, 4, 5, 6]),
      (2, [1], [1, 2])
    ]
    self.run_cases(cases)

if __name__ == '__main__':
  unittest.main()
