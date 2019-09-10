# hand-signature-extractor
To produce a PNG with transparency of the hand signature

## Dependency
There are a few dependencies required to use this project. I may produce an executable release with dependency included, but that is a long-term development.

- opencv-python: use `conda install -c conda-forge opencv-python` to install
- numpy: (will be included with installation of opencv-python through conda)
- notebook: for inline visualisation, use `conda install -c conda-forge notebook` to install
- matplotlib: for inline visualisation, use `conda install -c conda-forge matplotlib` to install

## Usage
Run the following command at the command line to get the help message
```bash
$ python main.py -h
```

The help message that is displayed:
```
usage: main.py [-h] --source SOURCE [--threshold THRESHOLD]
               [--op-ksize OP_KSIZE] [--op-shape {rect,cross,ellipse}]
               [--verbose VERBOSE] [--inline INLINE] [--ext EXT]

Program to extract signature from source image

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       path to the source of the image
  --threshold THRESHOLD
                        determine the threshold of range [1, 255] for the
                        binarizing of the image anduses cv2.THRESH_OTSU if
                        value is 0 or is not specified [default: 0]
  --op-ksize OP_KSIZE   the dimension of the square kernel size for opening
                        morphological operation [default: 3]
  --op-shape {rect,cross,ellipse}
                        the structuring element shape specified in cv2
                        [default: 'ellipse']
  --verbose VERBOSE     to show verbose debug message [default: False]
  --inline INLINE       bool to display inline instead of saving to file; if
                        type int is specified, the value will be used for the
                        size of the inline image [default: False]
  --ext EXT             the file extension to save the target image file
                        [default: 'png']
```
To visualise inline in jupyter notebook, use this snippet of code and get the help message at the first run
```python
import extract_signature
help(extract_signature.obtain_signature)
```
