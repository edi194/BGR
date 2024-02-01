from datetime import datetime
from rembg import new_session, remove
from pathlib import Path
from pick import pick
import logging
import os


def process_images(input_folder):
    getdatetime = datetime.now()
    date_time = getdatetime.strftime("%d_%m_%Y_%H_%M_%S")

    logging.basicConfig(filename=date_time + '_bgr.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')
    logging.warning('Warming up...')
    title = 'Choose model which will be used for background removal: '
    options = ['u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg', 'silueta', 'isnet-general-use', 'isnet-anime', 'sam']
    option, index = pick(options, title, indicator='=>', default_index=0)
    selected_model = option

    before_folder = input_folder / 'before_bgr'
    before_folder.mkdir(exist_ok=True)
    output_folder = input_folder / 'after_bgr'
    output_folder.mkdir(exist_ok=True)
    model_name = new_session(selected_model)
    print('Processing files using model: ' + selected_model)
    logging.warning('Processing files using model: ' + selected_model)

    for file in before_folder.glob('*'):
        if file.suffix in ['.jpg', '.jpeg','.png', '.JPG', '.JPEG','.PNG']:
            output_path = output_folder / (file.stem + "_" + selected_model + "_" + date_time + ".png")
            print('Opening ' + file.stem)
            logging.warning('Opening ' + file.stem)

            with open(file, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img_data = i.read()
                    output = remove(img_data, session=model_name)
                    o.write(output)
                    print('File ' + file.stem + ' done')
                    logging.warning('File ' + file.stem + ' done')
                    
if __name__ == "__main__":
    current_folder = Path(os.getcwd())
    process_images(current_folder)
    logging.warning('Processing done')