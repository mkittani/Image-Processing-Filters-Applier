from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import cv2
import numpy as np

root=Tk()
root.title("Filter Applier")

grayscale_image, result_image = None,None
def open_image():
    global grayscale_image, result_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;")])
    if file_path:
        image = Image.open(file_path)
        grayscale_image=image.convert("L")  #The argument "L" stands for luminance, and it specifies that the image should be converted to grayscale
        
        display_image(grayscale_image)

def display_image(image):
    converted_image = ImageTk.PhotoImage(image) #to convert the image to be TKinter compatible
    
    image_label.config(image=converted_image)
    image_label.image = converted_image

def apply_point_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image) #to convert the grayscale image into NumPy array
        filter = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])
        
        result_image = cv2.filter2D(image_array,-1, filter) #to apply filter -1 to maintain the data typeof input image

        result_image = Image.fromarray(result_image)    #to convert the array of the result_image to a PIL object to deal w/it

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_horizontal_line_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-1, -1, -1],
                           [2,   2,  2],
                           [-1, -1, -1]])
        
        result_image = cv2.filter2D(image_array,-1, filter)
        
        result_image = Image.fromarray(result_image)

        display_image(result_image)

    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_pos45_line_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-1, -1, 2],
                           [-1,  2,-1],
                           [2, -1, -1]])
        
        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_neg45_line_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[2, -1, -1],
                           [-1,  2,-1],
                           [-1, -1, 2]])

        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_vertical_line_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-1, 2, -1],
                           [-1,  2,-1],
                           [-1, 2, -1]])
        
        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")
    


def apply_horizontal_edge_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-1, -2, -1],
                           [0,   0,  0],
                           [1,   2,  1]])
        
        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_pos45_edge_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-2, -1, 0],
                           [-1,  0, 1],
                           [0,   1, 2]])

        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_neg45_edge_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[ 0,  1, 2],
                           [-1,  0, 1],
                           [-2, -1, 0]])

        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")

def apply_vertical_edge_detection():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)
        filter = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

        result_image = cv2.filter2D(image_array,-1, filter)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_laplacian():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        result_image = cv2.Laplacian(image_array, -1)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_laplacian_of_gaussian():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        blurred_image = cv2.GaussianBlur(image_array, (5, 5), 0) #5,5 is the kernel size of the blurring effect
                                                                 #0 tells the OpenCV to calculate the standard deviation automatically
        result_image = cv2.Laplacian(blurred_image, -1)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_zero_crossing():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        blurred_image = cv2.GaussianBlur(image_array, (5, 5), 0)

        laplacian_of_gaussian_result = cv2.Laplacian(blurred_image, -1)

        result_image = np.zeros_like(laplacian_of_gaussian_result)
        result_image[laplacian_of_gaussian_result > 0] = 255    #to make all pixels' values that are more than 0, white(if pixel>0 then =255)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_threshold():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        result_image = cv2.threshold(image_array, 128, 255, cv2.THRESH_BINARY)
        #any value below threshold value 128 is set to 0 and any value above is set to 255

        result_image = Image.fromarray(result_image[1])

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_adaptive_threshold():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        result_image = cv2.adaptiveThreshold(image_array, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #adap_thres_gauss_C is a built in function that uses the weighted sum from the neighbor values
        #11 is the size of the neighbor block to take into considiration which must be an odd no.
        #a constant subtraced from the mean of the neighbors to get a better result for the thresholding 

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def apply_user_defined_filter():
    global grayscale_image, result_image
    if grayscale_image:
        image_array = np.array(grayscale_image)

        filter_size = simpledialog.askinteger("Filter Size", "Enter filter size:")
        coefficients_str = simpledialog.askstring("Filter Coefficients", "Enter filter coefficients (comma-separated):")

        coefficients=[]
        coefficients_str=coefficients_str.split(',') #split the given coefficients and save into a list
        for i in coefficients_str:
            coefficients.append(float(i))

        filter_matrix = np.array(coefficients).reshape((filter_size, filter_size))
        #to generate a matrix with the given size

        result_image = cv2.filter2D(image_array, -1, filter_matrix)

        result_image = Image.fromarray(result_image)

        display_image(result_image)
    else:
        messagebox.showerror("Error","You should open an Image First!")


def save_image():
    global grayscale_image, result_image
    if grayscale_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            result_image.save(file_path)
    else:
        messagebox.showerror("Error","No image to save. Open an image first!")



openImageButton=Button(root,text="Open an image", command=open_image, fg="white", bg="red", width=25)
openImageButton.grid(pady=10,padx=5)


pointDetection=Button(root,text="Apply point detection", command=apply_point_detection, fg="white", bg="cyan", width=25)
pointDetection.grid(column=4,row=2,pady=10,padx=5)


horizontalLineDetection=Button(root,text="Apply horizontal line detection ", command=apply_horizontal_line_detection, fg="white", bg="black", width=25)
horizontalLineDetection.grid(column=1,row=0,pady=10,padx=5)

pos45LineDetection=Button(root,text="Apply +45 line detection ", command=apply_pos45_line_detection, fg="white", bg="black", width=25)
pos45LineDetection.grid(column=1,row=1,pady=10,padx=5)

neg45LineDetection=Button(root,text="Apply -45 line detection ", command=apply_neg45_line_detection, fg="white", bg="black", width=25)
neg45LineDetection.grid(column=1,row=2,pady=10)

verticalLineDetection=Button(root,text="Apply vertical line detection ", command=apply_vertical_line_detection, fg="white", bg="black", width=25)
verticalLineDetection.grid(column=1,row=3,pady=10,padx=5)




horizontalEdgeDetection=Button(root,text="Apply horizontal edge detection ", command=apply_horizontal_edge_detection, fg="white", bg="blue", width=25)
horizontalEdgeDetection.grid(column=2,row=0,pady=10,padx=5)

pos45EdgeDetection=Button(root,text="Apply +45 edge detection ", command=apply_pos45_edge_detection, fg="white", bg="blue", width=25)
pos45EdgeDetection.grid(column=2,row=1,pady=10,padx=5)

neg45EdgeDetection=Button(root,text="Apply -45 edge detection ", command=apply_neg45_edge_detection, fg="white", bg="blue", width=25)
neg45EdgeDetection.grid(column=2,row=2,pady=10,padx=5)

verticalEdgeDetection=Button(root,text="Apply vertical edge detection ", command=apply_vertical_edge_detection, fg="white", bg="blue", width=25)
verticalEdgeDetection.grid(column=2,row=3,pady=10,padx=5)


laplacianEdgeDetection = Button(root, text="Apply Laplacian Filter", command=apply_laplacian, fg="white", bg="purple", width=25)
laplacianEdgeDetection.grid(column=3,row=0,pady=10,padx=5)

LogDetection = Button(root, text="Apply Laplacian of Gaussian Filter", command=apply_laplacian_of_gaussian, fg="white", bg="green", width=25)
LogDetection.grid(column=3,row=1,pady=10,padx=5)

zeroCrossingDetection = Button(root, text="Apply Zero Crossing Filter", command=apply_zero_crossing, fg="white", bg="pink", width=25)
zeroCrossingDetection.grid(column=3,row=2,pady=10,padx=5)

thresholdDetection = Button(root, text="Apply Threshold Filter", command=apply_threshold, fg="white", bg="orange", width=25)
thresholdDetection.grid(column=3,row=3,pady=10,padx=5)

adaptiveThresholdDetection = Button(root, text="Apply Adaptive Threshold Filter", command=apply_adaptive_threshold, fg="white", bg="green", width=25)
adaptiveThresholdDetection.grid(column=4,row=0,pady=10,padx=5)

userDefinedFilterButton = Button(root, text="Apply User-Defined Filter", command=apply_user_defined_filter, fg="white", bg="brown", width=25)
userDefinedFilterButton.grid(column=4,row=1,pady=10,padx=5)

saveImageButton = Button(root, text="Save Image", command=save_image, fg="white", bg="red", width=25)
saveImageButton.grid(column=4,row=3,pady=10,padx=5)


image_label = Label(root)
image_label.grid()


root.mainloop()