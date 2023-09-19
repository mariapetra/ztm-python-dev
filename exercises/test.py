import unittest
import guessing_game

class TestGame(unittest.TestCase)
    def setUp(self):
        print('about to test the guessing game')

    def check_correct_number(self):
        answer = 5
        guess = 5
        result = guessing_game.run_guess(answer, guess)
        self.assertTrue(result, answer)

    def test_wrong_guess(self):
        answer = 5
        guess = 0
        result = guessing_game.run_guess(answer, guess)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = guessing_game.run_guess(5, 11)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
