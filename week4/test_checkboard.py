import checkboard
import unittest

#unit test for check board
class checkboardTest(unittest.TestCase):
    def run_cases(self, cases):
        for case in cases:
            actual = checkboard.check_checkboard(case[0])
            self.assertEqual(
                actual, case[1], f"Expected checkboard={case[0]} to produce {case[1]} but got {actual}")

    def test_board(self):
        cases = [
            # example cases and an edge case (not sure if there's a better way to feed the input, and not sure how to do the largest edge case in this way, because that would be a long string)
            (['WBBW', 'WBWB', 'BWWB', 'BWBW'], 1),
            (["WB", "WB"], 0),
            (["BWWB", "BWBB", "WBBW", "WBWW"], 0),
            (["BWBWWB", "WBWBWB", "WBBWBW", "BBWBWW", "BWWBBW", "WWBWBB"], 0),
            (["WWBBWB", "BBWWBW", "WBWBWB", "BWBWBW", "BWBBWW", "WBWWBB"], 1)
        ]
        self.run_cases(cases)

if __name__ == '__main__':
  unittest.main()

