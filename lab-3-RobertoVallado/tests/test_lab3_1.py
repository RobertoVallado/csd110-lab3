import pytest
import src.lab3_1 as lab
import util

def test1(capsys):
    lab.print_division_info(4, 3)
    out, err = capsys.readouterr()
    expected = "4 divided by 3 is 1 remainder 1\n"
    assert out == expected, util.format_message("Function does not produce correct output for 4/3", expected, out)

def test2(capsys):
    lab.print_division_info(1, 1)
    out, err = capsys.readouterr()
    expected = "1 divided by 1 is 1 remainder 0\n"
    assert out == expected, util.format_message("Function does not produce correct output for 1/1", expected, out)

def test3(capsys):
    lab.print_division_info(10, 10)
    out, err = capsys.readouterr()
    expected = "10 divided by 10 is 1 remainder 0\n"
    assert out == expected, util.format_message("Function does not produce correct output for 10/1", expected, out)

def test4(capsys):
    lab.print_division_info(12, 1)
    out, err = capsys.readouterr()
    expected = "12 divided by 1 is 12 remainder 0\n"
    assert out == expected, util.format_message("Function does not produce correct output for 12/1", expected, out)

def test5(capsys):
    lab.print_division_info(123, 100)
    out, err = capsys.readouterr()
    expected = "123 divided by 100 is 1 remainder 23\n"
    assert out == expected, util.format_message("Function does not produce correct output for 123/100", expected, out)

def test6(capsys):
    lab.print_division_info(100, 123)
    out, err = capsys.readouterr()
    expected = "100 divided by 123 is 0 remainder 100\n"
    assert out == expected, util.format_message("Function does not produce correct output for 100/123", expected, out)