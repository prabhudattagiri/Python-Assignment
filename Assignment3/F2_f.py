# e) Delete the file backup.txt

import os

# Check if the file exists
if os.path.exists("backup.txt"):
    # Delete the file
    os.remove("backup.txt")
    print("backup.txt has been deleted.")
else:
    print("backup.txt does not exist.")
