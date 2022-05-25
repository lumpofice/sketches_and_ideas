This is a repository in which ideas and sketches are kept for potential use in more serious projects in the future.



------------------------------------------------
inverse_matrix_3x3
------------------------------------------------
This repository contains a python file that finds a solution for the linear equation of an invertible 3x3 matrix composed with a column vector of 3 rows, then uses NumPy to compute the inverse of the matrix and uses that inverse to check that its composition with the previously computed solution gives us the column vector of 3 rows in return. The initial matrix is constructed using a class called Vec, which uses dictionaries and sets to define coordinates of the row vectors used in constructing this matrix.



-----------------------------------------------------------------
finding_max_dot_product_between_two_vectors_of_unequal_dimensions
-----------------------------------------------------------------
In this script, we are to find the maximum of a set of outputs computed by the dot product of two vectors of unequal dimensions. Specifically, in this example, one vector, v, is 6x1, while the other, u, is 9x1. If both coordinates in the product of coordinates are positive or if both are negative, the dot product will contribute a positive value to its sum. If one coordinate is negative and one positive in the product of coordinates, then the dot product will contribute a negative value to its sum. Iterating over each index between 0 and the difference in rows between these two vectors, which is 3 in this example, we take the maximum of the dot products computed at each.  



------------------------------------------------
max_min_temperature_plot
------------------------------------------------
This function uses a csv file, bearing temperatures and dates
at which those temperatures were recorded, to plot maximum and minimum
temperature values (by date) within the same visual. Once the file is
read, a header with column values and their associated indices will be
printed for the purposes of informing the user which data is desired for
plotting.


------------------------------------------------
mini_search_engine
------------------------------------------------
This repository contains a miniature search engine I was prompted to create by an author while working through a set of his textbook exercises. To be honest, I cannot know if what I've create meets the author's expectations. The goal was to create a miniature search, and I was successful in that much, at least.



------------------------------------------------
sudoku_solver
------------------------------------------------
This is a sudoku puzzle solver written in python. The user will be burdened with providing the sudoku puzzle themselves, as the grid variable, using zeros to represent blank spaces.



------------------------------------------------
team_strength
------------------------------------------------
These scripts were built purely with the intentions of marrying two languages that work towards the same goal. The bash script is taking user input and storing it into a local csv file, while python is pulling the data from that csv file for analysis. I imagine this set of scripts could be useful for an athletic coach who may be interested in analyzing their team's strength stats. 

Instructions: Clone this repository to your local machine, then run the python script in a bash editor. 



------------------------------------------------
timer
------------------------------------------------
This repository holds a timer that displays in the bash shell. The shell script may be run directly, or the script may be run from python to display within the python shell. 
