# tests/test_ranking_calculator.py

import unittest
from author_ranking.ranking_calculator import calculate_composite_score

class TestRankingCalculator(unittest.TestCase):
    def test_composite_score(self):
        author = {
            "citations": {"article1": 10, "article2": 5},
            "publications": {"journal1": 2},
            "self_citations": {"article1": 3, "article2": 2},
            "collaborators": {"most_frequent": 3},
        }
        score = calculate_composite_score(author)
        self.assertAlmostEqual(score, expected_value)  # Replace expected_value with the actual expected result

if __name__ == '__main__':
    unittest.main()
