# Concatenate

Script Description:
This Python script aims to concatenate the data from multiple Excel files in a specified directory and save the merged data to new Excel files in a subdirectory named 'concatened'. It uses the pandas library to read and manipulate the Excel files.

Usage:

Place all the Excel files you want to concatenate into a directory named 'teste'. Ensure that the files have the extension '.xlsx'.
Run the script in your Python environment. It will read each Excel file in the 'teste' directory, concatenate the data, and save the merged data into new Excel files.
Functions:

concatenate(dir_path, type_file, new_column): This function takes three parameters:

dir_path: The directory path where the Excel files are located.
type_file: The file extension of the Excel files to be processed (e.g., 'xlsx').
new_column: The name of the new column that will store the concatenated data.
createRepository(dir_path): This function takes one parameter:

dir_path: The directory path where the new 'concatened' subdirectory will be created.
Note:

Ensure that you have pandas installed in your Python environment to run the script. You can install it using pip install pandas.
The script will create a subdirectory named 'concatened' inside the 'teste' directory and save the concatenated Excel files there.
Author:
Adsandro Carvalho / adsandroxerd@gmail.com
