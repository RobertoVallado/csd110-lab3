import pytest
import src.lab3_2 as lab
import util

def test1(capsys):
    lab.solve_quadratic(1, 1, 0)
    out, err = capsys.readouterr()
    expected = "The roots of y = 1x^2 + 1x + 0 are 0.0 and -1.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=1, b=1, c=0", expected, out)

def test2(capsys):
    lab.solve_quadratic(2, 3, 1)
    out, err = capsys.readouterr()
    expected =  "The roots of y = 2x^2 + 3x + 1 are -0.5 and -1.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=2, b=3, c=1", expected, out)

def test3(capsys):
    lab.solve_quadratic(1, 0, -1)
    out, err = capsys.readouterr()
    expected = "The roots of y = 1x^2 + 0x + -1 are 1.0 and -1.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=1, b=0, c=-1", expected, out)

def test4(capsys):
    lab.solve_quadratic(1, 0, 0)
    out, err = capsys.readouterr()
    expected = "The roots of y = 1x^2 + 0x + 0 are 0.0 and 0.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=1, b=0, c=0", expected, out)

def test5(capsys):
    lab.solve_quadratic(-1, -2, -1)
    out, err = capsys.readouterr()
    expected = "The roots of y = -1x^2 + -2x + -1 are -1.0 and -1.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=-1, b=-2, c=-1", expected, out)

def test6(capsys):
    lab.solve_quadratic(12, 34, -56)
    out, err = capsys.readouterr()
    expected = "The roots of y = 12x^2 + 34x + -56 are 1.1666666666666667 and -4.0\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=12, b=34, c=-56", expected, out)

def test7(capsys):
    lab.solve_quadratic(0.25, 1.3, -2.66)
    out, err = capsys.readouterr()
    expected = "The roots of y = 0.25x^2 + 1.3x + -2.66 are 1.5713307229228426 and -6.771330722922842\n"
    assert out == expected, util.format_message("Function does not produce correct output for a=0.25, b=1.3, c=-2.66", expected, out)