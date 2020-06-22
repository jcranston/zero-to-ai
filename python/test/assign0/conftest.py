"""
conftest.py needed for pytest to detect files.
This also contains helper methods for running tests or autograders.
Please do not modify this file.
"""
import os
from pathlib import Path

from enum import Enum, unique
from stanfordkarel.karel import Karel
from stanfordkarel.karel_application import StudentCode

PROBLEMS = [
    'hailstorm_karel',
    'lawn_mowing_karel',
    'restoration_karel',
    'steeplechase_karel',
    'double_beeper_karel',
    'duplication_karel'
]

Z2AI_CODE_DIR = os.path.join(Path(__file__).parents[2], 'zero2ai/assign0')
TEST_CODE_DIR = os.path.join(Path(__file__).parents[2], 'test/assign0')
TIMEOUT = 30
CHAR_WIDTH = 6
HORIZONTAL, VERTICAL = "─", "│"
SPACING = 10


@unique
class Color(Enum):
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def compare_karel(karel1: Karel, karel2: Karel):
    '''
    todo: Please remove this method and the method call once Tyler Yep
    fixes the autograder for stanfordkarel and publishes the fix to the pip
    channel.
    Please see https://trello.com/c/Zt4VNWa6 and https://trello.com/c/8emL7JDK
    for corresponding workstreams
    '''
    if karel1 == karel2:
        return True

    """ Compares Karel Output and gets the results. """

    def create_two_column_string(col1, col2):
        """ col1 and col2 are Lists. """
        return map(
            lambda x: "{}{}{}".format(x[0], " " * SPACING, x[1]),
            zip(col1, col2)
        )

    def symmetric_difference(a, b):
        extra_a, extra_b = {}, {}
        for k in a:
            if k not in b:
                extra_a[k] = a[k]
            elif a[k] - b[k] > 0:
                extra_a[k] = a[k] - b[k]
        for k in b:
            if k not in a:
                extra_b[k] = b[k]
            elif b[k] - a[k] > 0:
                extra_b[k] = b[k] - a[k]
        return extra_a, extra_b

    matching = True
    this, that = str(karel1).split("\n"), str(karel2).split("\n")

    if len(this) != len(that):
        matching = False
    else:
        for i in range(len(this)):
            if this[i] != that[i]:
                matching = False
                break

    world_width = len(this[0])

    header1, header2 = "Student Output:", "Expected Output:"
    text_spacing = " " * (world_width - len(header1) + SPACING + 1)
    two_columns = create_two_column_string(this, that)
    output = "\n".join(two_columns)
    fancy_arrows = "{}❯{}❯{}❯ ".format(
        Color.RED.value, Color.YELLOW.value, Color.GREEN.value
    )

    result = "\n\n{} {}{}{}" "\n{}{}{}\n{}\n".format(
        fancy_arrows,
        Color.YELLOW.value,
        karel1.world.world_name,
        Color.END.value,
        header1,
        text_spacing,
        header2,
        output,
    )

    if karel1.avenue != karel2.avenue or karel1.street != karel2.street:
        matching = False
        result += (
            "Karel did not end up in the same location in both worlds:\n"
            "Student: {}\n"
            "Expected: {}\n\n".format((karel1.avenue, karel1.street),
                                      (karel2.avenue, karel2.street))
        )

    # remove record of beepers that have a count of zero
    for d in [karel1.world.beepers, karel2.world.beepers]:
        for k in list(d):
            if d[k] == 0:
                del d[k]

    if karel1.world.beepers != karel2.world.beepers:
        matching = False
        extra_a, extra_b = symmetric_difference(karel1.world.beepers,
                                                karel2.world.beepers)
        result += (
            "Beepers do not match: "
            "(Only beepers that appear in one world but "
            "not the other are listed)\n"
            "Student: {}\n"
            "Expected: {}\n\n".format(extra_a, extra_b)
        )
    print(result)
    return matching


def get_code_file(problem_name):
    return os.path.join(Z2AI_CODE_DIR, problem_name + '.py')


def get_end_world_file(problem_name):
    return os.path.join(TEST_CODE_DIR, 'worlds', problem_name + '_end.w')


def get_beg_world_file(problem_name):
    return os.path.join(Z2AI_CODE_DIR, 'worlds', problem_name + '.w')


def execute_karel_code(problem_name):
    code_file = get_code_file(problem_name)
    beginning_world_file = get_beg_world_file(problem_name)
    end_world_file = get_end_world_file(problem_name)
    karel = Karel(world_file=beginning_world_file)
    student_code = StudentCode(code_file, karel)
    student_code.mod.main()
    matching = compare_karel(karel, Karel(end_world_file))
    if not matching:
        raise AssertionError('Resulting world did not match expected result.')
