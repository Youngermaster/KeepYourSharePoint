from sharepoint import SharePoint

# Set file name
file_name = 'test_sharepoint.txt'

# Set folder name
folder_name = ''

# Get file
file = SharePoint().download_file(file_name, folder_name)

# Save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()
