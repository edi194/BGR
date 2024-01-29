from datetime import datetime
from rembg import new_session, remove
from pathlib import Path
from pick import pick
import os


def process_images(input_folder):
    title = 'Choose model which will be used for background removal: '
    options = ['u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg', 'silueta', 'isnet-general-use', 'isnet-anime', 'sam']
    option, index = pick(options, title, indicator='=>', default_index=0)
    selected_model = option

    output_folder = input_folder / 'output'
    output_folder.mkdir(exist_ok=True)
    model_name = new_session(selected_model)
    print('Processing files using model: ' + selected_model)
    
    getdatetime = datetime.now()
    date_time = getdatetime.strftime("%d_%m_%Y_%H_%M_%S")

    for file in input_folder.glob('*'):
        if file.suffix in ['.jpg', '.jpeg','.png', '.JPG', '.JPEG','.PNG']:
            output_path = output_folder / (file.stem + "_" + selected_model + "_" + date_time + ".png")
            print('Opening ' + file.stem)

            with open(file, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img_data = i.read()
                    output = remove(img_data, session=model_name)
                    o.write(output)
                    print('File ' + file.stem + ' done')
                    
if __name__ == "__main__":
    current_folder = Path(os.getcwd())
    process_images(current_folder)