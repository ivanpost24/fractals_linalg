import matplotlib.pyplot as plt  # Plotting functions
import numpy as np  # Array and matrix representation
import numpy.typing as npt


def de_rham_curve_ifs(alpha: float,
                      beta: float,
                      delta: float,
                      epsilon: float,
                      zeta: float,
                      eta: float,
                      samples: int = 10000,
                      random_state: np.random.Generator | None = None) -> np.ndarray:
    rng = np.random.default_rng(random_state)
    d0 = np.array([[1,     0,       0],
                   [0, alpha,   delta],
                   [0,  beta, epsilon]])
    d1 = np.array([[    1,         0,    0],
                   [alpha, 1 - alpha, zeta],
                   [ beta,     -beta,  eta]])

    def step(point: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        if rng.random() < 0.5:
            return d0 @ point
        else:
            return d1 @ point
    x = np.zeros(shape=(samples, 3))
    x[:, 0] = 1
    for i in range(1, samples):
        x[i] = step(x[i - 1])
    return x[:, 1:]


def cesaro_curve_ifs(a: complex,
                     samples: int = 10000,
                     random_state: np.random.Generator | None = None) -> npt.NDArray[np.float64]:
    alpha, beta = a.real, a.imag
    return de_rham_curve_ifs(alpha, beta, -beta, alpha, beta, 1 - alpha,
                             samples=samples, random_state=random_state)


def takagi_curve_ifs(w: float,
                     samples: int = 10000,
                     random_state: np.random.Generator | None = None) -> npt.NDArray[np.float64]:
    return de_rham_curve_ifs(0.5, 1, 0, w, 0, w,
                             samples=samples, random_state=random_state)


def koch_peano_curve_ifs(a: complex,
                         samples: int = 10000,
                         random_state: np.random.Generator | None = None) -> npt.NDArray[np.float64]:
    alpha, beta = a.real, a.imag
    return de_rham_curve_ifs(alpha, beta, beta, -alpha, -beta, alpha - 1,
                             samples=samples, random_state=random_state)


def main() -> None:
    rng = np.random.default_rng()

    x = koch_peano_curve_ifs(0.5 + np.sqrt(3) / 6 * 1j, random_state=rng)

    fig, ax = plt.subplots(figsize=(20, 20))
    ax.plot(x[:, 0], x[:, 1], '.', markersize=1)
    ax.set_aspect('equal')
    ax.set_title('Koch Snowflake')
    plt.show()


if __name__ == '__main__':  # Don't worry about what this does
    main()
