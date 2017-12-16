from os import listdir
from os.path import join
import pandas as pd

directory = '/path/to/your/files'
output_filename = 'combined.xlsx'
blankValue = 'None'
files = []

# Reads all .xlsx files in given directory.
for f in listdir(directory):
    if f.endswith('.xlsx'):
        files.append(join(directory, f))

# Loops through all files and creates dataframes
for i in range(0,len(files)):

    if i is 0:
        print('Reading file %s' % files[i])
        df1 = pd.read_excel(files[i])
    else:
        print('Reading file %s' % files[i])
        df2 = pd.read_excel(files[i])
        print('Appending...')
        df1 = df1.append(df2)

# Replace periods in column header
df1.columns = df1.columns.str.lower().str.replace('.','_')

# Replace blank cells with a value (e.g. None)
df1 = df1.fillna(blankValue)

# Write the new file
print('Writing new file...')
df1.to_excel(directory + '/' + output_filename, index=False)