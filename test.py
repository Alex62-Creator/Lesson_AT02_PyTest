import pytest
from main import count_vowels

# Используем декоратор для параметризованных тестов
@pytest.mark.parametrize("text, expected", [
   ("Привет! Как тебя зовут?", 7),
   ("ау я юо", 5),
   ("Трр крк стр", 0),
   ("Здесь будет ошибка", 3),
   ("У меня есть сын Юра.", 7)
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected