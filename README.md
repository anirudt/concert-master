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
- Archive the scatterplot and the MIDI file later.
- Try to do a Histogram Backprojection
  - Detected that S and V channels do have a specific trend.
  - Try to get a trend in H channels
  - Collect pertinent data wrt this.
  - Tried, but the fingertip detection is not very robust.
- Try the YCbCr space using the paper written by Ngan and Chai.

## Preprocessing involved
The following preprocessing is conducted:
- Convert the color space to HSV from RGB.
- Apply a range thresholding
- Apply Dilation / Erosion.
- Apply Medianblur to remove small outlier white points.
- Apply contouring to get the contours with the largest areas.
- Done with music synthesis for a double hand system.
