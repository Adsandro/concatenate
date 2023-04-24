import os
import pandas as pd

def concatenate(dir_path, type_file, new_column):
    for filename in os.listdir(dir_path):
        try:
            if filename.endswith(type_file):
                df = pd.read_excel(os.path.join(dir_path, filename))
                
                df[new_column] = df.apply(lambda row: '\n'.join([f"{col.rstrip(':?')}:{val} - " if not pd.isna(val) else "" for col, val in row.items()]), axis=1)
                
                output_filename = os.path.join(dir_path, 'concatened', filename)
                df.to_excel(output_filename, index=False)
        except FileNotFoundError as fnf:
            print('The specified file was not found, error:', fnf)
        finally:
            print(f'Finalized program: {filename} concatened')

def createRepository(dir_path):
    try:
        os.mkdir(dir_path)
    finally:
        print(f'Repository {dir_path} created, put all your excel files in it')

concatenate(dir_path='teste', type_file='xlsx',new_column='teste')