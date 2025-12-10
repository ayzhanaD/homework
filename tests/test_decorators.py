from datetime import datetime
from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log()
    def test_func_1() -> None:
        raise ValueError

    test_func_1()
    captured = capsys.readouterr()
    assert captured.out == "test_func_1 error: ValueError. Inputs: (), {}\n"

    @log()
    def test_func_2(a: int, b: int) -> int:
        return a + b

    test_func_2(4, 5)
    captured2 = capsys.readouterr()
    assert captured2.out == (f"test_func_2 result: 9, start time: {(datetime.now()).strftime("%H:%M:%S")}, "
                             f"arguments: (4, 5), {{}}\n")

    @log("log1.txt")
    def test_func_3(user_name: str) -> str:
        return user_name

    test_func_3("Olof")
    captured3 = capsys.readouterr()
    assert captured3.out == "test_func_3 ok\n"

    @log("log2.txt")
    def test_func_4(user_name: str) -> None:
        raise TypeError

    test_func_4("Olof")
    captured3 = capsys.readouterr()
    assert captured3.out == "test_func_4 error: TypeError. Inputs: ('Olof',), {}\n"
