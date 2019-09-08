import numpy as np
import cv2
import matplotlib.pyplot as plt

def plot_point(data, plot = True):

    """
    This function outputs the probability of the given pixel
    for being part of a moving element.

    @param: data: array of temporal intensity data

    @returns : p, probability of moving pixels


    """
    t = data
    sp = np.fft.fft(np.sin(t))
    freq = np.fft.fftfreq(t.shape[-1])
    full = (sp.real**2 + sp.imag**2)**0.5

    if plot:
        plt.plot(freq, full, ".")
        plt.ylim(0,50)
        plt.pause(1e-5)
        plt.clf()

    arg_null = np.where(freq==0)

    """
    TODO: Calculate probablilty from amplitudes in an interval
    around zero frequency.

    Current Implimentation direclty takes the amplitude corresponding
    to zero frequency. This is effective only for smaller stacks of
    images. For bigger stacks with more images, pixels that are not
    moving lies in an interval around zero.

    """
    p = np.mean(full[arg_null[0]])/ np.sum(full)
    return p

def image_fft(images):
    """

    3D implimentation of plot_point function

    """
    t = images
    sp = np.fft.fft(np.sin(t), axis = 0)
    freq = np.fft.fftfreq(t.shape[0])
    full = (sp.real**2 + sp.imag**2)**0.5
    arg_null = np.where(freq==0)

    """
    TODO: Calculate probablilty from amplitudes in an interval
    around zero frequency.

    Current Implimentation direclty takes the amplitude corresponding
    to zero frequency. This is effective only for smaller stacks of
    images. For bigger stacks with more images, pixels that are not
    moving lies in an interval around zero.

    """
    p = full[arg_null[0], :, :]
    sum = np.sum(full, axis = 0)
    p = np.nan_to_num(p/sum)
    return p

def softmax(x):
    x = x - np.max(x)
    x = np.exp(x)
    x = x / np.sum(x)
    return x
