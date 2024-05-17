import matplotlib.pyplot as plt  # Plotting functions
import numpy as np  # Array and matrix representation
import numpy.typing as npt


type Vector2 = npt.NDArray[np.float64]
type Line2 = tuple[Vector2, Vector2]


def rotation(angle_degrees: float) -> npt.NDArray[np.float64]:
    return np.array([[np.cos(np.radians(angle_degrees)), -np.sin(np.radians(angle_degrees))],
                     [np.sin(np.radians(angle_degrees)),  np.cos(np.radians(angle_degrees))]])


def _koch_helper(start_point: Vector2, end_point: Vector2, depth: int) -> list[Line2]:
    if depth == 0:
        return [(start_point, end_point)]
    R = rotation(60)
    A = -(R - 2 * np.identity(2)) / 3
    B = (R + np.identity(2)) / 3
    points = [start_point,
              (end_point - start_point) / 3 + start_point,
              A@start_point + B@end_point,
              2 * (end_point - start_point) / 3 + start_point,
              end_point]
    lines = [line for line in zip(points, points[1:])]
    out_lines = lines.copy()
    for index, line in enumerate(lines):
        out_lines[index] = _koch_helper(line[0], line[1], depth - 1)
    return [line for lines in out_lines for line in lines]


def koch(start_point: Vector2, end_point: Vector2, depth: int) -> list[Vector2]:
    lines = _koch_helper(start_point, end_point, depth)
    return [line[0] for line in lines] + [lines[-1][1]]


def main() -> None:
    rng = np.random.default_rng()  # Create a random number generator

    x = np.array([-1, 0])
    y = np.array([1, 0])
    points = np.array(koch(x, y, 6))

    fig, ax = plt.subplots(figsize=(20, 20))
    ax.plot(points[:, 0], points[:, 1])
    ax.set_aspect('equal')
    plt.show()


if __name__ == '__main__':  # Don't worry about what this does
    main()
