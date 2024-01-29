from rembg import remove
from pathlib import Path
import os


def process_images(input_folder):
    output_folder = input_folder / 'output'
    output_folder.mkdir(exist_ok=True)

    for file in input_folder.glob('*'):
        if file.suffix in ['.jpg', '.jpeg','.png', '.JPG', '.JPEG','.PNG']:
            output_path = output_folder / (file.stem + ".png")
            print('Opening ' + file.stem)

            with open(file, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img_data = i.read()
                    output = remove(img_data)
                    o.write(output)
                    print('File ' + file.stem + ' done')


if __name__ == "__main__":
    current_folder = Path(os.getcwd())
    process_images(current_folder)
