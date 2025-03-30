import pytest
from freezegun import freeze_time

from src.decorators import my_function, log

@pytest.mark.parametrize("x, y, expected_output", [
    (1, 2, "\n[2025-03-28 12:24:25] my_function started with inputs: (1, 2), {}\n"
            "[2025-03-28 12:24:25] my_function finished successfully with result: 3")
])
@freeze_time("2025-03-28 12:24:25")  # Замораживаем время на нужной дате и времени

def test_log(capsys, x, y, expected_output):
    @log()
    def my_function(x, y):
        return x + y

    my_function(x, y)  # вызываем функцию, чтобы сработал декоратор
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()


def test_my_function_logs_error(capfd):
    with pytest.raises(TypeError, match="Введены не правильные данные в функции my_function"):
        my_function(1, "2")
    out, err = capfd.readouterr()
    assert "my_function started with inputs:(1, '2'), {}" in out
    assert "my_function error: TypeError. Inputs: (1, '2'), {}" in out