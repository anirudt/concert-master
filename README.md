## What?
Concert-Master is a gesture based music synthesis tool.

## Build Instructions
Fire up a terminal and run the above command.
```
$ python concert.py
```

## TODO:
- Keep trackbars for each of them for more robust fingertip detection.

## Preprocessing involved
The following preprocessing is conducted:
- Convert the color space to HSV from RGB.
- Apply a range thresholding
- Apply Dilation / Erosion.
- Apply Medianblur to remove small outlier white points.
