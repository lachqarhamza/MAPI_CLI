#!/bin/bash

# Create a copy of the Python file
cp main.py main_copy.py

# Make the copy executable
chmod +x main_copy.py

# Add shebang line to the top of the copy
echo "#!/usr/bin/env python3" | cat - main_copy.py > temp && mv temp main_copy.py

# Move the copy to /usr/local/bin
sudo mv main_copy.py /usr/local/bin/mapi

# Update the permissions of the moved file
sudo chmod 755 /usr/local/bin/mapi
