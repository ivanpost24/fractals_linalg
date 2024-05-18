from pathlib import Path
from tkinter.filedialog import asksaveasfilename

from fractals import cookbook
from fractals.de_rham import simple_de_rham_ifs


def main() -> None:
    img = simple_de_rham_ifs(-0.1, +0.2, -0.1, +0.2).make_image(4096, 2160, batch_size=10000, print_progress=True)

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
