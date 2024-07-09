import os

import pytest

from src.decorators import log


def test_log_to_file_success() -> None:
    # Удаляем лог-файл перед тестом, если он существует
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    # Вызываем функцию
    @log(filename="test_log.txt")
    def test_function_success(x: int, y: int) -> int:
        return x + y

    result = test_function_success(2, 3)
    assert result == 5

    # Проверяем содержимое лог-файла
    with open("test_log.txt", "r") as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert lines[0].strip() == "test_function_success ok"


def test_log_to_file_error() -> None:
    # Удаляем лог-файл перед тестом, если он существует
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    # Вызываем функцию и проверяем результат
    @log(filename="test_log.txt")
    def test_function_error(x: int, y: int) -> float:
        return x / y

    result = test_function_error(1, 0)
    assert result == "Error"

    # Проверяем содержимое лог-файла
    with open("test_log.txt", "r") as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert "test_function_error error: division by zero. Inputs: (1, 0), {}" in lines[0].strip()


def test_log_to_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    # Вызываем функцию
    @log()
    def test_function_console_success(x: int, y: int) -> int:
        return x + y

    result = test_function_console_success(2, 3)
    assert result == 5

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "test_function_console_success ok" in captured.out


def test_log_to_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    # Вызываем функцию и проверяем результат
    @log()
    def test_function_console_error(x: int, y: int) -> float:
        return x / y

    result = test_function_console_error(1, 0)
    assert result == "Error"

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "test_function_console_error error: division by zero. Inputs: (1, 0), {}" in captured.out
