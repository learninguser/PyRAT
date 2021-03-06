import pyrat
import numpy as np


class RotateLeft(pyrat.FilterWorker):
    """
    Rotate data set by multiples of 90 degrees
    
    :param times: How often to rotate
    :type int:
    :author: Andreas Reigber
    """
    gui = {'menu': 'Tools|Geometry', 'entry': 'Rotate left'}

    def __init__(self, *args, **kwargs):
        super(RotateLeft, self).__init__(*args, **kwargs)
        self.name = "ROTATE LEFT"
        self.blockprocess = False

    def filter(self, array, *args, **kwargs):
        if array.ndim > 2:
            for k in range(array.ndim - 2):
                array = np.rollaxis(array, axis=0, start=array.ndim)
        array = np.rot90(array, 1)
        if array.ndim > 2:
            for k in range(2):
                array = np.rollaxis(array, axis=0, start=array.ndim)
        return array


class RotateRight(pyrat.FilterWorker):
    """
    Rotate data set by multiples of 90 degrees

    :param times: How often to rotate
    :type int:
    :author: Andreas Reigber
    """
    gui = {'menu': 'Tools|Geometry', 'entry': 'Rotate right'}

    def __init__(self, *args, **kwargs):
        super(RotateRight, self).__init__(*args, **kwargs)
        self.name = "ROTATE Right"
        self.blockprocess = False

    def filter(self, array, *args, **kwargs):
        if array.ndim > 2:
            for k in range(array.ndim - 2):
                array = np.rollaxis(array, axis=0, start=array.ndim)
        array = np.rot90(array, 3)
        if array.ndim > 2:
            for k in range(2):
                array = np.rollaxis(array, axis=0, start=array.ndim)
        return array


class Transpose(pyrat.FilterWorker):
    """
    Rotate data set by multiples of 90 degrees

    :param times: How often to rotate
    :type int:
    :author: Andreas Reigber
    """
    gui = {'menu': 'Tools|Geometry', 'entry': 'Transpose'}

    def __init__(self, *args, **kwargs):
        super(Transpose, self).__init__(*args, **kwargs)
        self.name = "TRANSPOSE"
        self.blockprocess = False

    def filter(self, array, *args, **kwargs):
        # array = np.transpose(array, axes=list(range(array.ndim-2, array.ndim)))
        array = np.swapaxes(array, array.ndim - 2, array.ndim - 1)
        return array


class MirrorHorizontal(pyrat.FilterWorker):
    """
    Rotate data set by multiples of 90 degrees

    :param times: How often to rotate
    :type int:
    :author: Andreas Reigber
    """
    gui = {'menu': 'Tools|Geometry', 'entry': 'Mirror horizontal'}

    def __init__(self, *args, **kwargs):
        super(MirrorHorizontal, self).__init__(*args, **kwargs)
        self.name = "MIRROR HORIZONTAL"
        self.blockprocess = False

    def filter(self, array, *args, **kwargs):
        array = array[..., ::-1]
        return array


class MirrorVertical(pyrat.FilterWorker):
    """
    Rotate data set by multiples of 90 degrees

    :param times: How often to rotate
    :type int:
    :author: Andreas Reigber
    """
    gui = {'menu': 'Tools|Geometry', 'entry': 'Mirror vertical'}

    def __init__(self, *args, **kwargs):
        super(MirrorVertical, self).__init__(*args, **kwargs)
        self.name = "MIRROR VERTICAL"
        self.blockprocess = False

    def filter(self, array, *args, **kwargs):
        array = array[..., ::-1, :]
        return array


@pyrat.docstringfrom(RotateLeft)
def rotateleft(*args, **kwargs):
    return RotateLeft(*args, **kwargs).run(*args, **kwargs)


@pyrat.docstringfrom(RotateRight)
def rotateright(*args, **kwargs):
    return RotateRight(*args, **kwargs).run(*args, **kwargs)


@pyrat.docstringfrom(Transpose)
def transpose(*args, **kwargs):
    return Transpose(*args, **kwargs).run(*args, **kwargs)


@pyrat.docstringfrom(MirrorHorizontal)
def mirrorhorizonal(*args, **kwargs):
    return MirrorHorizontal(*args, **kwargs).run(*args, **kwargs)


@pyrat.docstringfrom(MirrorVertical)
def mirrorvertical(*args, **kwargs):
    return MirrorVertical(*args, **kwargs).run(*args, **kwargs)
