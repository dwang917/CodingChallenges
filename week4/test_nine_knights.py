import unittest
import nine_knights

class testNineKnights(unittest.TestCase):
  def run_case(self, cases):
    for case in cases:
            actual = nine_knights.check(case[0])
            self.assertEqual(
                actual, case[1], f"Expected checkboard={case[0]} to produce {case[1]} but got {actual}")
  
  def test_board(self):
    #example test cases, still not sure if there's a better case design
    cases = [
      (["...k.", "...k.", "k.k..", ".k.k.", "k.k.k"], "invalid"),
      ([".....", "...k.", "k.k.k", ".k.k.", "k.k.k"], "valid"),
      ([".....", "...k.", "k.k.k", ".k.k.", "k...k"], "invalid")
    ]
    self.run_case(cases)

if __name__ == '__main__':
  unittest.main()