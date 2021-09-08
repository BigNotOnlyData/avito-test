import aiohttp
from typing import List


def change_direction(directions: List[str], direction: str) -> str:
    index_direction = directions.index(direction)
    return directions[(index_direction + 1) % len(directions)]


def spiral(matrix: List[List[int]]) -> List[int]:
    numbers = []
    n = len(matrix)
    row = 0
    col = 0
    directions = ['down', 'right', 'up', 'left']
    direction = directions[0]
    for _ in range(n * n):
        numbers += [matrix[row][col]]
        matrix[row][col] = None

        if direction == 'down':
            row += 1
            if row > n - 1 or matrix[row][col] is None:
                row -= 1
                col += 1
                direction = change_direction(directions, direction)
        elif direction == 'right':
            col += 1
            if col > n - 1 or matrix[row][col] is None:
                col -= 1
                row -= 1
                direction = change_direction(directions, direction)
        elif direction == 'up':
            row -= 1
            if row < 0 or matrix[row][col] is None:
                row += 1
                col -= 1
                direction = change_direction(directions, direction)
        elif direction == 'left':
            col -= 1
            if col < 0 or matrix[row][col] is None:
                col += 1
                row += 1
                direction = change_direction(directions, direction)
    return numbers


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                text = await response.text()
            except aiohttp.ClientError as e:
                print(e)
            else:
                matrix = [list(map(int, line.split()[1::2])) for line in text.strip().split('\n')[1::2]]
                return spiral(matrix)
