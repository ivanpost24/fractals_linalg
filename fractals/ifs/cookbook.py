"""A collection of well-known curves' iterated function systems."""


import numpy as np

from fractals.ifs.de_rham import simple_de_rham_ifs, cesaro_curve_ifs, takagi_curve_ifs, koch_peano_curve_ifs


__all__ = ['levy_c_curve', 'cesaro_vepstas_fig2', 'blancmange_curve', 'koch_curve', 'koch_peano_vepstas_fig3',
           'koch_peano_vepstas_fig4', 'peano_space_filling_curve', 'vepstas_gallery01', 'vepstas_gallery02',
           'vepstas_gallery03', 'vepstas_gallery04', 'vepstas_gallery05', 'vepstas_gallery06', 'vepstas_gallery07',
           'vepstas_gallery08', 'vepstas_gallery09', 'vepstas_gallery10', 'vepstas_gallery11', 'vepstas_gallery12',
           'vepstas_gallery13', 'vepstas_gallery14', 'vepstas_gallery15', 'vepstas_gallery16', 'vepstas_gallery17',
           'vepstas_gallery18', 'vepstas_gallery19', 'vepstas_gallery20', 'vepstas_gallery21', 'vepstas_gallery22',
           'vepstas_gallery23', 'vepstas_gallery24', 'vepstas_gallery25', 'vepstas_gallery26', 'vepstas_gallery27',
           'vepstas_gallery28', 'vepstas_gallery29', 'vepstas_gallery30', 'vepstas_gallery31', 'vepstas_gallery32',
           'vepstas_gallery33', 'vepstas_gallery34', 'vepstas_gallery35', 'vepstas_gallery36', 'vepstas_gallery37',
           'vepstas_gallery38', 'vepstas_gallery39', 'vepstas_gallery40', 'vepstas_gallery41', 'vepstas_gallery42']


levy_c_curve = cesaro_curve_ifs(0.5 + 0.5j)
cesaro_vepstas_fig2 = koch_peano_curve_ifs(0.3 + 0.3j)
blancmange_curve = takagi_curve_ifs(0.6)
koch_curve = koch_peano_curve_ifs(0.5 + np.sqrt(3) / 6 * 1j)
koch_peano_vepstas_fig3 = koch_peano_curve_ifs(0.6 + 0.37j)
koch_peano_vepstas_fig4 = koch_peano_curve_ifs(0.6 + 0.45j)
peano_space_filling_curve = koch_peano_curve_ifs((1 + 1j) / 2)

vepstas_gallery01 = simple_de_rham_ifs(+0.25, -0.47, -0.25, -0.47)
vepstas_gallery02 = simple_de_rham_ifs(+0.25, -0.25, -0.25, -0.25)
vepstas_gallery03 = simple_de_rham_ifs(+0.25, +0.00, -0.25, +0.00)
vepstas_gallery04 = simple_de_rham_ifs(+0.18, -0.38, -0.18, -0.42)
vepstas_gallery05 = simple_de_rham_ifs(+0.49, -0.38, +0.10, -0.42)
vepstas_gallery06 = simple_de_rham_ifs(+0.33, -0.38, -0.18, -0.42)
vepstas_gallery07 = simple_de_rham_ifs(+0.18, -0.28, -0.18, -0.72)
vepstas_gallery08 = simple_de_rham_ifs(+0.41, -0.28, +0.00, -0.58)
vepstas_gallery09 = simple_de_rham_ifs(+0.41, -0.06, +0.00, -0.58)
vepstas_gallery10 = simple_de_rham_ifs(+0.41, +0.10, +0.00, -0.58)
vepstas_gallery11 = simple_de_rham_ifs(+0.51, -0.10, +0.00, -0.58)
vepstas_gallery12 = simple_de_rham_ifs(+0.51, +0.10, -0.20, -0.58)
vepstas_gallery13 = simple_de_rham_ifs(+0.10, +0.15, +0.35, +0.88)
vepstas_gallery14 = simple_de_rham_ifs(-0.05, +0.15, +0.35, +0.88)
vepstas_gallery15 = simple_de_rham_ifs(+0.00, +0.60, +0.30, +0.60)
vepstas_gallery16 = simple_de_rham_ifs(+0.00, +0.60, +0.18, +0.60)
vepstas_gallery17 = simple_de_rham_ifs(+0.00, +0.60, +0.00, +0.60)
vepstas_gallery18 = simple_de_rham_ifs(-0.00, -0.70, -0.00, +0.70)
vepstas_gallery19 = simple_de_rham_ifs(-0.10, -0.40, -0.10, +0.80)
vepstas_gallery20 = simple_de_rham_ifs(+0.00, -0.70, -0.15, +0.80)
vepstas_gallery21 = simple_de_rham_ifs(+0.30, -0.70, -0.15, +0.80)
vepstas_gallery22 = simple_de_rham_ifs(+0.30, -0.70, -0.15, +0.00)
vepstas_gallery23 = simple_de_rham_ifs(+0.30, -0.70, -0.15, -0.30)
vepstas_gallery24 = simple_de_rham_ifs(-0.10, -0.70, -0.15, -0.30)
vepstas_gallery25 = simple_de_rham_ifs(-0.10, -0.80, -0.30, -0.60)
vepstas_gallery26 = simple_de_rham_ifs(-0.10, -0.80, -0.30, -0.80)
vepstas_gallery27 = simple_de_rham_ifs(-0.10, -0.40, -0.30, -0.80)
vepstas_gallery28 = simple_de_rham_ifs(+0.00, -0.60, +0.00, -0.60)
vepstas_gallery29 = simple_de_rham_ifs(-0.35, +0.10, +0.30, -0.40)
vepstas_gallery30 = simple_de_rham_ifs(-0.45, +0.50, +0.35, -0.45)
vepstas_gallery31 = simple_de_rham_ifs(-0.45, +0.60, +0.50, -0.45)
vepstas_gallery32 = simple_de_rham_ifs(-0.30, +0.60, +0.60, -0.20)
vepstas_gallery33 = simple_de_rham_ifs(+0.30, +0.15, +0.75, +0.18)
vepstas_gallery34 = simple_de_rham_ifs(+0.30, +0.15, +0.75, -0.48)
vepstas_gallery35 = simple_de_rham_ifs(-0.35, +0.60, -0.16, +0.60)
vepstas_gallery36 = simple_de_rham_ifs(-0.20, +0.40, +0.40, +0.00)
vepstas_gallery37 = simple_de_rham_ifs(-0.15, +0.15, +0.15, +0.85)
vepstas_gallery38 = simple_de_rham_ifs(-0.40, +0.40, +0.40, +0.40)
vepstas_gallery39 = simple_de_rham_ifs(-0.30, -0.40, +0.20, +0.60)
vepstas_gallery40 = simple_de_rham_ifs(-0.35, +0.00, +0.35, +0.00)
vepstas_gallery41 = simple_de_rham_ifs(-0.35, +0.00, -0.35, +0.00)
vepstas_gallery42 = simple_de_rham_ifs(-0.50, +0.00, +0.50, +0.00)