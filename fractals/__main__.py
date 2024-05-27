import cmath
from pathlib import Path
from tkinter.filedialog import asksaveasfilename

from fractals import cookbook
from fractals.de_rham import simple_de_rham_ifs, DeRhamIFS



def main() -> None:
    a = cmath.rect(0.5, cmath.pi/4)

    img = DeRhamIFS.from_complex_functions(lambda z: z/(z+1), lambda z: 1/(z+1)).make_image(1000, 1000, batch_size=100, print_progress=True)

    # Save the resulting image to a file; ask the user for the target file.
    if (target_path := asksaveasfilename(confirmoverwrite=True,
                                         initialdir=Path.cwd().parent / 'images',
                                         initialfile='fractal_output',
                                         filetypes=[('JPEG', ('.jpeg', '.jpg')),
                                                    ('PNG', '.png'),
                                                    ('TIFF', '.tiff')])):
        img.save(target_path)
    else:
        img.show('Fractal curve')


if __name__ == '__main__':  # Don't worry about what this does
    main()
