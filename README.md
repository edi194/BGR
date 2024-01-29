# BGR - Background removal tool

## Features

- Model selector (same as rembg)
- Will automatically get every image in current directory and remove the Background
- Uses [Rembg](https://github.com/danielgatis/rembg)
- Save output image with the same exact Name 
- All results are saved in a new created dir 'output'


## Usage  

1. Clone this repo
2. Add the script at the desired folder  
3. Open terminal and navigate to that folder
4. Run `python main.py`


## Installation
```bash
git clone https://github.com/edi194/BGR.git
```

Go to the project directory

```bash
cd BGR
```

Requires OpenCV and Python.

```

pip install -r requirements.txt

```
Move the app at the desired location and run App

```bash
python main.py
```

### Acknowledgements
  Credits goes [ @danielgatis ](https://github.com/danielgatis) for making Rembg CLI tool and [ @beephole ](https://github.com/beephole) for original script
 
 - Install  [Rembg](https://github.com/danielgatis/rembg)

```bash
  pip install rembg # for library
  pip install rembg[cli] # for library + cli
```
