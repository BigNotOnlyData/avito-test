from main import get_matrix
import asyncio


SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    loop = asyncio.get_event_loop()
    assert loop.run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL, 'Неверный ответ'


if __name__ == '__main__':
    test_get_matrix()
