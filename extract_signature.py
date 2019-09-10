import cv2
import numpy as np
import os

def obtain_signature(image_source, 
              threshold=0, 
              opening_ksize=3, 
              opening_shape=cv2.MORPH_ELLIPSE, 
              verbose=False, 
              inline=False,
              ext='png'):
    """
    To transform the source image to the image containing hand signature

    Parameters
    ----------
    image_source : str
        path to the source of the image
    threshold : int, optional
        determine the threshold of range [1, 255] for the binarizing of the image and
        uses cv2.THRESH_OTSU if value is 0 or is not specified [default: 0]
    opening_ksize : int, optional
        the dimension of the square kernel size for opening morphological operation
        [default: 3]
    operning_shape : optional
        the structuring element shape specified in cv2 [default: cv2.MORPH_ELLIPSE]
    verbose : bool, optional
        to show verbose debug message [default: False]
    inline : int or bool, optional
        to display inline instead of saving to file; if type int is specified, the
        value will be used for the size of the inline image [default: False]
    ext : str, optional
        the file extension to save the target image file [default: 'png']
    """

    if verbose:
        def pr(*args, **kwargs):
            print(*args, **kwargs)
        def imshow_verbose(p, **kwargs):
            imshow(p, **kwargs)
    else:
        def pr(*args, **kwargs):
            pass
        def imshow_verbose(p, **kwargs):
            pass
        
    if inline:            
        import matplotlib.pyplot as plt
        try:
            from IPython import get_ipython
            ipy = get_ipython()
            if ipy is not None:
                ipy.run_line_magic('matplotlib', 'inline')
                def imshow(img, cmap='viridis', convert=None, image_size=inline):
                    if convert:
                        img = cv2.cvtColor(img, convert)
                    y = img.shape[0]
                    x = img.shape[1]
                    ratio = x/y
                    display_size = (image_size, image_size*ratio)

                    plt.figure(figsize=display_size)
                    plt.imshow(img, cmap=cmap)
                    plt.axis('off')
                    plt.show()
            else:
                def imshow(img, **kwargs):
                    pr('Image cannot be displayed')
        except:
            def imshow(img, **kwargs):
                pr('Image cannot be displayed')
    
    image = cv2.imread(image_source, 0)
    pr('Reading', image_source)
    imshow_verbose(image, cmap='gray', image_size=(inline if type(inline) == int else 10))
    if threshold:
        pr('Binarising with threshold at', threshold)
        imagem = image
        imagem[imagem >= threshold] = 255
        imagem[imagem < threshold] = 0

    else:
        ret, imgf = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        pr('Binarising with threshold at', ret, 'using OTSU')
        imagem = cv2.bitwise_not(imgf)
    imshow_verbose(imagem, cmap='gray', image_size=(inline if type(inline) == int else 10))

    ksize = opening_ksize
    ksize = (ksize, ksize)
    kernel = cv2.getStructuringElement(opening_shape, ksize)
    opening = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, kernel)
    pr('Performing opening morphological operation: kernel size =', opening_ksize)
    imshow_verbose(opening, cmap='gray', image_size=(inline if type(inline) == int else 10))
    canvas = np.zeros((opening.shape), np.uint8)
    signature = cv2.merge((canvas, canvas, canvas, opening))
    pr('Merging into alpha-channeled colour space')
    if inline:
        imshow(signature, cmap='gray', image_size=(inline if type(inline) == int else 10))

    destination = 'target/'
    if not os.system('mkdir target'):
        pr('Created target folder named \'target\'')
    
    filename = '.'.join(image_source.split('/')[-1].split('.')[:-1])
    if '.' not in ext:
        ext = '.' + ext
    path = destination + filename + ext
    if cv2.imwrite(path, signature):
        pr('Saved to', path)
