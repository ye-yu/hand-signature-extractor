import argparse

parser = argparse.ArgumentParser(description='Program to extract signature from source image')
parser.add_argument('--source', 
    help='path to the source of the image', 
    required=True)

parser.add_argument('--threshold', 
    help='determine the threshold of range [1, 255] for the binarizing of the image anduses cv2.THRESH_OTSU if value is 0 or is not specified [default: 0]', 
    default=0, type=int)

parser.add_argument('--op-ksize', 
    help='the dimension of the square kernel size for opening morphological operation [default: 3]', 
    default=3, type=int)

parser.add_argument('--op-shape', 
    help='the structuring element shape specified in cv2 [default: \'ellipse\']', 
    choices=['rect', 'cross', 'ellipse'], 
    default='ellipse', type=str)

parser.add_argument('--verbose', 
    help='to show verbose debug message [default: False]', 
    default=False, type=bool)

parser.add_argument('--inline', 
    help='bool to display inline instead of saving to file; if type int is specified, the value will be used for the size of the inline image [default: False]', 
    default=False, type=str)

parser.add_argument('--ext', 
    help='the file extension to save the target image file [default: \'png\']', 
    default='png', type=str)

args = parser.parse_args()
source = args.source
threshold = args.threshold
op_ksize = args.op_ksize
op_shape = args.op_shape
verbose = args.verbose
try:
    inline = int(args.inline)
except:
    if 'True' in args.inline:
        inline = True
    elif 'False' in args.inline:
        inline = False
    else:
        raise ValueError('Value is not boolean or integer.')
ext = args.ext

args = dict(
    threshold=threshold,
    op_ksize=op_ksize,
    op_shape=op_shape,
    verbose=verbose,
    inline=inline,
    ext=ext
)
print(args)