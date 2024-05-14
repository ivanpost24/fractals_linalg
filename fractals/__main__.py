import matplotlib.pyplot as plt
import numpy as np


ITERATIONS = 100000

SIDES = 3


def main() -> None:
    rng = np.random.default_rng()

    t = np.linspace(0, 2 * np.pi, SIDES + 1)[:-1]
    v = np.array([np.cos(t), np.sin(t)]).T

    T = np.array([[0.5, 0.0],
                  [0.0, 0.5]])
    x = np.zeros(shape=(ITERATIONS + 1, 2))
    x[0] = rng.uniform(-0.5, 0.5, size=2)
    for i in range(ITERATIONS):
        k = rng.integers(SIDES)
        x[i + 1] = T @ (x[i] - v[k]) + v[k]

    fig, ax = plt.subplots()
    ax.plot(x[:, 0], x[:, 1], '.', markersize=0.1)
    ax.set_aspect('equal')

    plt.show()


if __name__ == '__main__':
    main()
