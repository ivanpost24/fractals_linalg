import matplotlib.pyplot as plt  # Plotting functions
import numpy as np  # Array and matrix representation
import numpy.typing as npt


type Vector2 = npt.NDArray[np.float64]
type Line2 = tuple[Vector2, Vector2]


def rotation(angle_degrees: float) -> npt.NDArray[np.float64]:
    return np.array([[np.cos(np.radians(angle_degrees)), -np.sin(np.radians(angle_degrees))],
                     [np.sin(np.radians(angle_degrees)),  np.cos(np.radians(angle_degrees))]])


def _levyc_helper(start_point: Vector2, end_point: Vector2, depth: int) -> list[Line2]:
    if depth == 0:
        return [(start_point, end_point)]
    R = rotation(45)
    R2 = rotation(-45)
   # A = -(R - 2 * np.identity(2)) / 3
  #  B = (R + np.identity(2)) / 3
    #print((1/np.sqrt(2))*R2)
    points = [start_point,
              ((1/np.sqrt(2))*(R2@(end_point-start_point))+start_point),
             # (R2@end_point),
              end_point]
    lines = [line for line in zip(points, points[1:])]
    out_lines = lines.copy()
    for index, line in enumerate(lines):
        out_lines[index] = _levyc_helper(line[0], line[1], depth - 1)
    return [line for lines in out_lines for line in lines]


def levyc(start_point: Vector2, end_point: Vector2, depth: int) -> list[Vector2]:
    lines = _levyc_helper(start_point, end_point, depth)
    return [line[0] for line in lines] + [lines[-1][1]]

def main() -> None:
    rng = np.random.default_rng()  # Create a random number generator

    x = np.array([-1, 0])
    y = np.array([1, 0])
    points = np.array(levyc(x, y,10))

    fig, ax = plt.subplots(figsize=(20, 20))
    ax.plot(points[:, 0], points[:, 1])
    ax.set_aspect('equal')
    plt.show()


if __name__ == '__main__':  # Don't worry about what this does
    main()
