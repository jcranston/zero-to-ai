import pytest
from test.assign0.conftest import PROBLEMS, TIMEOUT, execute_karel_code


@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize('problem_name', PROBLEMS)
def test_karel_functionality(problem_name):
    execute_karel_code(problem_name)
