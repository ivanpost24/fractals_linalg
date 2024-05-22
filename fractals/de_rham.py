"""Definitions of de Rham curve iterated function systems."""


from collections.abc import Generator, Callable
import numpy as np
import numpy.typing as npt
from PIL import Image
from typing import Literal


__all__ = ['DeRhamIFS', 'cesaro_curve_ifs', 'takagi_curve_ifs', 'koch_peano_curve_ifs']


def _scale(array: np.ndarray, bottom: float, top: float, bounds: tuple[float, float] | None = None) -> np.ndarray:
    if bounds is None:
        bounds = array.min(), array.max()
    return np.interp(array, bounds, (bottom, top))


class DeRhamIFS:
    """
    An iterated function system (IFS) based on the chaos game for drawing de Rham curves.

    A de Rham curve is constructed with a complete metric space on which two contracting maps d0 and d1 with fixed
    points p0 and p1. The curve is defined by the uncountably infinite set of countably infinite binary strings where 0
    indicates an application of d0 and 1 indicates an application of d1.

    The chaos game IFS for de Rham curves starts at the fixed point p0 and then randomly with uniform probability
    selects one of the contracting maps to apply. For the chaos game to work, d0 and d1 must additionally satisfy the
    continuity condition d0(p1) = d1(p0).

    Using the above conditions simplifies the parameters for the contracting maps to a half-way point and four
    parameters. d0 is always a linear transformation, and d1 is an affine transformation.

    For maximal efficiency, points generated are saved in an array which can be accessed later.
    """
    def __init__(self, halfway_point: complex, delta: float, epsilon: float, zeta: float, eta: float, random_state=None) -> None:
        """
        Initializes a new DeRhamIFS.
        :param halfway_point: The half-way point of the curve, expressed as a complex number. The real
        :param delta: A parameter for the first contracting map. Must be between -1 and 1.
        :param epsilon: A parameter for the first contracting map. Must be between -1 and 1.
        :param zeta: A parameter for the second contracting map. Must be between -1 and 1.
        :param eta: A parameter for the second contracting map. Must be between -1 and 1.
        :param random_state: A seed for initializing the random state of the iterated function system.
        """
        alpha, beta = halfway_point.real, halfway_point.imag
        self.d0 = np.array([[1,     0,       0],
                            [0, alpha,   delta],
                            [0,  beta, epsilon]])
        self.d1 = np.array([[    1,         0,    0],
                            [alpha, 1 - alpha, zeta],
                            [ beta,     -beta,  eta]])
        self._rng = np.random.default_rng(random_state)

        self._points: npt.NDArray[np.float64] | None = None

    @classmethod
    def from_complex_functions(cls, d0: Callable[[complex], complex], d1: Callable[[complex], complex]) -> 'DeRhamIFS':
        pass

    @property
    def points(self) -> npt.NDArray[np.float64]:
        """The already-calculated points by this IFS."""
        if self._points is None:
            raise RuntimeError('No points have been generated yet')

        return self._points[:, 1:]

    def set_random_state(self, state) -> None:
        """Sets the random state of the IFS."""
        self._rng = np.random.default_rng(state)

    def make_image(self,
                   length: int,
                   width: int,
                   batch_size: int = 1000,
                   completeness_cutoff: float = 0.99,
                   color_theme: Literal['dark'] | Literal['light'] = 'dark',
                   print_progress: bool = False) -> Image.Image:
        """
        Creates an image of the de Rham curve this IFS generates. Points are generated in batches until a sufficient
        proportion of the new points generated are already filled (until the curve is sufficiently complete).

        :param length: Length of the image, in pixels.
        :param width: Width of the image, in pixels.
        :param batch_size: The number of points processed at a time before checking for completeness.
        :param completeness_cutoff: The proportion of points that need to already be filled by a previous batch before
                                    point generation stops. (default: 0.99).
        :param color_theme: Whether to use a dark or light background for the fractal image (default: 'dark').
        :param print_progress: If True, print progress to the standard output (default: False).
        :return: A PIL.Image.Image object that contains the image.
        """
        off = 0 if color_theme == 'dark' else 255
        on = 255 if color_theme == 'dark' else 0
        image = np.full(shape=(width, length), fill_value=off, dtype=np.uint8)

        self.calculate_points(10000)
        x_bounds = np.min(self._points[:, 1]) - 0.05, np.max(self._points[:, 1]) + 0.05
        y_bounds = np.min(self._points[:, 2]) - 0.05, np.max(self._points[:, 2]) + 0.05

        if print_progress:
            last_threshold = 10
            print('...', end='', flush=True)
        else:
            last_threshold = 100

        for points in self.generate_points(batch_size):
            x_coords = np.floor(_scale(points[:, 0], 0, length - 1, x_bounds)).astype(int)
            y_coords = np.floor(_scale(points[:, 1], 0, width - 1, y_bounds)).astype(int)
            completeness = np.count_nonzero(image[y_coords, x_coords]) / batch_size
            if completeness >= completeness_cutoff:
                if print_progress:
                    print('done', flush=True)
                break
            if print_progress and completeness >= last_threshold / 100:
                print(f'{last_threshold}%...', end='', flush=True)
                if last_threshold >= int(100 * completeness_cutoff) - 10:
                    last_threshold += 1
                else:
                    last_threshold += 10
            image[y_coords, x_coords] = on
        return Image.fromarray(np.flipud(image))

    def calculate_points(self, nsteps: int) -> None:
        """
        Calculates the given number of points on the de-Rham curve. These new points are added to the points property
        to be accessed later.

        :param nsteps: The number of points to generate.
        """
        if self._points is None:
            self._points = np.zeros(shape=(nsteps, 3), dtype=np.float64)
            self._points[:, 0] = 1
            start_index = 1
            nsteps -= 1
        else:
            start_index = self._points.shape[0]
            self._points = np.vstack((self._points, np.zeros(shape=(nsteps, 3), dtype=np.float64)))

        for i in range(start_index, nsteps + start_index):
            self._points[i] = self._step(self._points[i - 1])

    def generate_points(self, batch_size: int) -> Generator[npt.NDArray[np.float64], None, None]:
        """
        Generates points in batches. Points that have already been generated will be yielded first, but still in the
        necessary batches.
        :param batch_size: The number of points in each batch.
        :return: A generator of points in the batch size given.
        """
        if self._points is None:
            self._points = np.zeros(shape=(batch_size, 3), dtype=np.float64)
            self._points[:, 0] = 1
            for i in range(1, batch_size):
                self._points[i] = self._step(self._points[i - 1])

        upper = 0
        for lower, upper in zip(range(0, len(self._points), batch_size), range(batch_size, len(self._points), batch_size)):
            yield self._points[lower:upper, 1:]
        if len(self._points[upper:]) < batch_size:
            start_index = len(self._points)
            self._points = np.vstack((self._points, np.zeros(shape=(batch_size - len(self._points[upper:]), 3), dtype=np.float64)))
            self._points[start_index:, 0] = 1
            for i in range(start_index, len(self._points)):
                self._points[i] = self._step(self._points[i - 1])
        yield self._points[upper:, 1:]

        while True:
            start_index = self._points.shape[0]
            self._points = np.vstack((self._points, np.zeros(shape=(batch_size, 3), dtype=np.float64)))
            for i in range(start_index, batch_size + start_index):
                self._points[i] = self._step(self._points[i - 1])

            yield self._points[start_index:batch_size + start_index, 1:]

    def clear(self) -> None:
        """
        Clears all generated points in this IFS. Generators created before this function is called should be ignored.
        """
        self._points = None

    def _step(self, point: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        if self._rng.random() < 0.5:
            return self.d0 @ point
        else:
            return self.d1 @ point


def simple_de_rham_ifs(delta: float, epsilon: float, zeta: float, eta: float, random_state=None) -> DeRhamIFS:
    """
    Returns the IFS generating a de Rham curve whose half-way point is at (0.5, 1).
    :param delta: A parameter for the first contracting map.
    :param epsilon: A parameter for the first contracting map.
    :param zeta: A parameter for the second contracting map.
    :param eta: A parameter for the second contracting map.
    :param random_state: A seed for initializing the random state of the iterated function system.
    :return: A DeRhamIFS object for the iterated function system of this curve.
    """
    return DeRhamIFS(0.5 + 1j, delta, epsilon, zeta, eta, random_state=random_state)


def cesaro_curve_ifs(a: complex,
                     random_state: np.random.Generator | None = None) -> DeRhamIFS:
    """
    Returns the IFS generating the Cèsaro curve with the given half-way point.
    :param a: The half-way point as a complex number.
    :param random_state: A seed for initializing the random state of the iterated function system.
    :return: A DeRhamIFS object for the iterated function system of this curve.
    """
    alpha, beta = a.real, a.imag
    return DeRhamIFS(a, -beta, alpha, beta, 1 - alpha, random_state=random_state)


def takagi_curve_ifs(w: float,
                     random_state: np.random.Generator | None = None) -> DeRhamIFS:
    """
    Returns the IFS generating the Takagi curve with the given parameter.
    :param w: The parameter for the Takagi curve.
    :param random_state: A seed for initializing the random state of the iterated function system.
    :return: A DeRhamIFS object for the iterated function system of this curve.
    """
    return DeRhamIFS(0.5 + 1j, 0, w, 0, w, random_state=random_state)


def koch_peano_curve_ifs(a: complex,
                         random_state: np.random.Generator | None = None) -> DeRhamIFS:
    """
    Returns the IFS generating the Koch-Peano curve with the given half-way point/apex.
    :param a: The half-way point as a complex number.
    :param random_state: A seed for initializing the random state of the iterated function system.
    :return: A DeRhamIFS object for the iterated function system of this curve.
    """
    alpha, beta = a.real, a.imag
    return DeRhamIFS(a, beta, -alpha, -beta, alpha - 1, random_state=random_state)
