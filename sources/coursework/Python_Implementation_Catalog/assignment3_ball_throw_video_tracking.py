#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:05:12 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
import os

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



# Iterate over all images
img_index = 0
img_path = format("ball_throw_vid_imgs/ball_throw_img_%i.png" %(img_index + 1))

collection = []

# The following functíon is used to verify if 2 sample groups are neighbors
def AreNeighbors(a, b) :
    # Verify the vertical coordinate of the samples are adjecents
    if (np.abs(a[1] - b[1]) > 1):
        return False
    # Verify the horizontal coordinate of the samples are adjecents
    if ((np.abs(a[2] - b[2]) > 1)):
        return False
    return True

# Calculates the mean value of the pixel color for the sample area specfied by i, j
# sample_dim - The dimention in pixels of the square defining the sample area
# scattering_factor - Number of pixels skipped from each line and collumn on 
# each iteration over the sample area
def MeanScatteredSample(img, sample_dim, scattering_factor, i, j):
    mean = 0
    # The points used for the sample are contained on a square of "sample_dim" pixels
    # However, the samplling skips "scattering_factor" pixels for each line and column on the square
    num_points = (sample_dim/scattering_factor)**2

    # Iterate inside the current sample area specfied by i, j    
    for y in range(i*sample_dim, (i+1)*sample_dim, scattering_factor):
        for x in range(j*sample_dim, (j+1)*sample_dim, scattering_factor):    
            mean += img[y][x]
            
    return mean/num_points


def FindAoI(img, sample_dim, scattering_factor, aoi_dim):
    sampling = []
    # Iterate over the image, spltting each dimention into smaller aread of "sample_dim" X "sample_dim" pixels 
    for i in range(0, int(img.shape[0]/sample_dim)):
        for j in range(0, int(img.shape[1]/sample_dim)):
            # The mean value for the coller on each sample is saved to be classified later
            sampling.append((MeanScatteredSample(img, sample_dim, scattering_factor, i, j), i, j))
    
    # Step 1: Sorte the samples by increasing intensity of color (from darkest to ligthtest)
    sampling.sort(key=lambda x : x[0])
    
    # The number of samples for the area we are looking for can be calculated 
    # by dividng the total size of the area of interest, by the size of each sample
    group_size = int(aoi_dim/sample_dim)
    # Consider a number of candidates beyond, so the criterial of "neighborhooding" can be taken into account 
    filtered = sampling[:2*group_size]
    
    
    # Step 2 - resort by postion, from top to bottom, left to right 
    filtered.sort(key=lambda x : (x[1], x[2]))
    
    group_index = 0
    grouped = []
    grouped.append([])
    grouped[group_index].append(filtered[0])
    
    # Navigate through the sample candidates and group by neighbors
    for i in range(1, len(filtered)):
        if(AreNeighbors(filtered[i], filtered[i-1])):
            grouped[group_index].append(filtered[i])
        else :
            grouped.append([])
            group_index = group_index + 1
            grouped[group_index].append(filtered[i])
            

    # Step 3: Find the darkest group and make it first            
    def mean(group):
        mean = 0
        for x in group:
            mean += x[0]
        return mean / len(group)
    
    grouped.sort(key=mean)
                 
    return grouped

################
# MAIN PROGRAM #
################

ydata = []
tdata = [] 
fps = 23.73

img_index = 0


# Iterate through each image from the vide
while(os.path.isfile(img_path)):
#for img_index in range(0, 23):
    # read image 
    img = plt.imread(img_path) 
    
    # Convert the image in gray scale and save in a list
    collection.append(rgb2gray(img))
    
    # We can only process the image by subtraction once we have more than one frame
    if(img_index > 0):
        # Subtract the current frame from the previous one to highlight moving elements
        img_proc = collection[img_index] - collection[img_index - 1]    
        
        # Define the parameters for the image processing algorithm
        sample_dim = 20
        scattering_factor = 4
        aoi_dim = 400
        
        # Use the image processing algorithm to find the area of interest in which the ball likely is
        sampling = FindAoI(img_proc, sample_dim, scattering_factor, aoi_dim)
        
        # Initialize the vectors for saving the pixel index from the sampled areas
        x_coord = np.zeros((len(sampling[0])), dtype=float)
        y_coord = np.zeros((len(sampling[0])), dtype=float)

        # This logic iterates over the sample areas from the group most likely to contain the ball
        # The index of each sample is converted into pixel index and saved
        coords_count = 0
        for group in sampling[:1]:
            for x in group:
                x_coord[coords_count] = x[2]*sample_dim
                y_coord[coords_count] = x[1]*sample_dim
                coords_count = coords_count + 1
                #for i in range(x[1]*sample_dim, (x[1]+1)*sample_dim):
                #    for j in range(x[2]*sample_dim, (x[2]+1)*sample_dim):
                #        img_proc[i, j] = 1

        # Calculate a mean value for the pixel indexes where the ball was likely found
        x = int(x_coord.mean())
        y = int(y_coord.mean())
        
        # For calculating the fit polynomio we are only interested on the y coordinates of the ball
        # and the time t of each frame
        ydata.append(y)
        tdata.append(img_index/fps)
        
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        fig = plt.figure(figsize=(img_proc.shape[0]*px, img_proc.shape[1]*px))

        # Display the image 
        ax = plt.subplot(2, 1, 1)
        ax.imshow(collection[img_index] , cmap="gray") # plot original image
        
        # Create the dashed lines to highlght the target
        plt.vlines(x, 0, y, linestyle="dashed")
        plt.hlines(y, 0, x, linestyle="dashed")
        
        
 
        # Convert ydata into an array to allow math operations and invert the coordinates orientation
        ydata_arr = img_proc.shape[0] - np.array(ydata, dtype=float) 

        # The system on the image goes from 0 to 1. Extrapolating precision,
        # the ball seems to start from 0 and reach maximum height at 1.
        # In this case, we will normalize the ball coordinates from 0 to 1
        ydata_norm = (ydata_arr - ydata_arr.min())/(ydata_arr.max() - ydata_arr.min())     
        
        
        ax = plt.subplot(2, 1, 2)
        ax.plot(tdata, ydata_norm, "o")

        # Find a quadratic polynomio fitting the data extracted from the experiment 
        fit = poly.polyfit(tdata,ydata_norm,2)
        
        # Calculate gracity in the normalized unit system
        g = 2*(fit[2])
        
        
        tdata_dense = np.linspace(0, 0.7)
        ydata_dense = poly.polyval(tdata_dense, fit)
        ax.plot(tdata_dense, ydata_dense, label=format(r"$y=%.2f+%.2f.t %.2f.t^2$" %(fit[0], fit[1], fit[2])))
        ax.legend(loc="upper left")
        
        ax.set_title("Exercise 3")
        ax.set_ylabel("Time (seconds)", fontsize=10)
        ax.set_xlabel(format(r"Ball height in the coordinates system, for $g=%.3f$" %(g)), fontsize=10)
        plt.ylim(0, 1.2)

    
    img_index = img_index + 1
    # Construct the path for the next image file
    img_path = format("ball_throw_vid_imgs/ball_throw_img_%i.png" %(img_index + 1))