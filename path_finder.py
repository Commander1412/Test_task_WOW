import random
from collections import deque


class PathFinder:
    def __init__(self, m, n, land_share):
        self.m = m
        self.n = n
        self.land_share = land_share
        self.field = self.generate_map()

    def generate_map(self):
        total_cells = self.m * self.n
        land_cells = int(total_cells * self.land_share)
        field = [['~' for _ in range(self.n)] for _ in range(self.m)]
        start_x, start_y = random.randint(0, self.m - 1), random.randint(0, self.n - 1)
        field[start_x][start_y] = '#'
        land_cells -= 1
        growth_points = [(start_x, start_y)]
        while land_cells > 0:
            x, y = growth_points.pop(random.randint(0, len(growth_points) - 1))
            for dx, dy in random.sample([(-1, 0), (1, 0), (0, -1), (0, 1)], 4):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n and field[nx][ny] == '~':
                    field[nx][ny] = '#'
                    growth_points.append((nx, ny))
                    land_cells -= 1
        return field

    def print_map(self):
        print("\nСгенерированная карта:")
        for row in self.field:
            print(' '.join(row))

    def bfs_shortest_path(self, start, end):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(start[0], start[1], [start])])
        visited = [[False] * self.n for _ in range(self.m)]
        visited[start[0]][start[1]] = True
        while queue:
            x, y, path = queue.popleft()
            if (x, y) == end:
                return path
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n and self.field[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, path + [(nx, ny)]))
        return None

    def print_map_with_path(self, path):
        if not path:
            print("\nПуть из точки A в точку B не найден.")
            return
        directions = {(0, 1): '→', (0, -1): '←', (1, 0): '↓', (-1, 0): '↑'}
        field_with_path = [row[:] for row in self.field]
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            dx, dy = x2 - x1, y2 - y1
            field_with_path[x1][y1] = directions[(dx, dy)]
        start_x, start_y = path[0]
        end_x, end_y = path[-1]
        field_with_path[start_x][start_y] = 'A'
        field_with_path[end_x][end_y] = 'B'
        print("\nКарта с кратчайшим путем:")
        for row in field_with_path:
            print(' '.join(row))

    @staticmethod
    def check_input_pos_int_data(value):
        while True:
            try:
                data = int(input(value))
                if data > 0:
                    return data
                else:
                    print("Ошибка: введите целое положительное число.")
            except ValueError:
                print("Ошибка: введите целое положительное число.")

    @staticmethod
    def check_input_coordinates(value, m, n):
        while True:
            try:
                start_x, start_y = map(int, input(value).split())
                if 0 <= start_x < m and 0 <= start_y < n:
                    return start_x, start_y
                else:
                    print("Ошибка: координаты должны быть от 0 до M-1 и от 0 до N-1")
            except ValueError:
                print("Ошибка: Введите два целых числа, разделенных пробелом.")


if __name__ == "__main__":
    m = PathFinder.check_input_pos_int_data("Введите параметр M: ")
    n = PathFinder.check_input_pos_int_data("Введите параметр N: ")
    land_share = PathFinder.check_input_pos_int_data("Введите долю суши в % (например, 40 для 40%): ") * 0.01
    navigator = PathFinder(m, n, land_share)
    navigator.print_map()
    start_x, start_y = navigator.check_input_coordinates("Введите координаты точки А в формате 'x y' (от 0 до M-1 и от 0 до N-1): ", m, n)
    end_x, end_y = navigator.check_input_coordinates("Введите координаты точки В в формате 'x y' (от 0 до M-1 и от 0 до N-1): ", m, n)
    path = navigator.bfs_shortest_path((start_x, start_y), (end_x, end_y))
    navigator.print_map_with_path(path)
