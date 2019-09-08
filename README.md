# Fourier Analysis for Background Estimation of Surveilance Videos
A small python implimentation of background estimation of surveilance videos using fourrier analysis.

## Method
Fourier transform of temporal pixel data helps us understand the behaviour of each pixels in time within the specified interval.
A pixel with its maximum amplitude peak at zero frequency is more likely to correspond to a static element in an image.
So we can generate a probability map of pixels that belongs to moving elements. The inverse of this mask is used to extract the background from each frame. Information from multiple frames are combined to stitch together the entire background. So it takes some time to build up the full image. This method works if the background is stationary.

## Test Results
