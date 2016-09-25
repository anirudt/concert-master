## What?
Concert-Master is a gesture based music synthesis tool.

## Dependencies
- ```opencv```
- ```pyknon```

## Build Instructions
Fire up a terminal and run the above command.
```
$ python concert.py
```

## TODO:
- Duplicate the code for a single and a double hand system.
- Optparse coming soon.

## Preprocessing involved
The following preprocessing is conducted:
- Convert the color space to HSV from RGB.
- Apply a range thresholding
- Apply Dilation / Erosion.
- Apply Medianblur to remove small outlier white points.
- Apply contouring to get the contours with the largest areas.
- Done with music synthesis for a double hand system.
