# Code Explanation
The *concatenate* function receives a directory path, a file type and a new column name as arguments. It iterates through all the files in the specified directory that have the same file extension as the one provided as an argument. For each file, it reads it as a Pandas DataFrame, applies a lambda function that concatenates all non-null values of each row into a string separated by the provided separator, and saves the resulting DataFrame to a new file with the same name as the original one, but inside a newly created *concatened* directory.

If the specified directory does not exist, the *createRepository* function is called to create it. If the directory already exists, nothing happens.

Example Usage
``` concatenate('/path/to/directory', '.xlsx', 'concatenated_values')
```

This will iterate through all Excel files (*'.xlsx'*) in the */path/to/directory* directory, concatenate all non-null values in each row into a string separated by a colon and a dash (*:* and *-*), add a new column with the name *'concatenated_values'*, and save the resulting DataFrame to a new Excel file with the same name as the original one, but inside a new *concatened* directory.# concatenate
