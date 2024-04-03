import pytest
import src.lab3_3 as lab
import util

def myfunc(n):
    return "testing123"

def test1(capsys):
    lab.say_math(myfunc, 4)
    out, err = capsys.readouterr()
    expected = "The result of <function myfunc "
    assert  expected == out[:31], util.format_message("Function does not produce correct output", expected, out)
    expected = "> applied to 4 is testing123\n"
    assert  expected == out[-29:], util.format_message("Function does not produce correct output", expected, out)