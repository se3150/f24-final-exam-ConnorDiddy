import time
import pytest
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def cracker():
    return Brute("secret")


def describe_Brute():

    def describe_bruteOnce():
        def test_it_initializes_correctly(cracker):
            assert cracker.target == cracker.hash("secret")
            
        def test_correct_answer_works(cracker):
            assert cracker.bruteOnce("secret") == True
            
        def test_wrong_answer_doesnt_work(cracker):
            assert cracker.bruteOnce("wrong") == False
            
    def describe_bruteMany():
        def test_does_not_take_more_time_than_given(cracker):
            t1 = time.time()
            cracker.bruteMany(50000)
            assert time.time() - t1 <= 50000
            
        def test_random_guess_returns_valid_string(cracker):
            random_string = cracker.randomGuess()
            assert 0 < len(random_string) < 9
