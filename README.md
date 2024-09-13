# Image Processing Filters Applier

A Tkinter-based Python application that allows users to apply a variety of filters to grayscale images. The app supports filters like line detection, edge detection, and custom user-defined filters.

## Features

- Open and display grayscale images.
- Apply different types of filters:
  - Line detection (horizontal, vertical, +45°, -45°)
  - Edge detection (horizontal, vertical, +45°, -45°)
  - Laplacian filter
  - Laplacian of Gaussian (LoG)
  - Zero-crossing filter
  - Thresholding (simple and adaptive)
  - User-defined filters
- Save the processed image after applying the filters.

## Prerequisites

To run this project, you need the following libraries installed:

- **OpenCV** (`opencv-python`)
- **Pillow** (`PIL`)
- **NumPy** (`numpy`)
- **Tkinter** (comes pre-installed with Python on most systems)

You can install each required library using these commands:

```bash
pip install opencv-python
pip install Pillow
pip install numpy
```
## How to Run
1. Clone the repository:
```
git clone https://github.com/mkittani/Image-Processing-Filters-Applier.git
cd Image-Processing-Filters-Applier
```
2. Install the required libraries:
```
pip install opencv-python
pip install Pillow
pip install numpy
```
3. Run the application:
```
python filter_applier.py
```
## GUI Overview
- Open an Image: Load an image (PNG, JPG) from your local machine.
- Apply Filters: Select one of the predefined filters or input a custom filter.
- Save Image: Save the processed image after applying the filter.

## Contributing
Feel free to contribute by opening an issue or submitting a pull request.
