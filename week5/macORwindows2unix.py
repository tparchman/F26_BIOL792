#!/usr/bin/env python3

import sys

# Loop through all filenames given on the command line
for filename in sys.argv[1:]:

    # Open and read the file
    with open(filename, "r") as infile:
        data = infile.read()

    # Create a name for the output file
    output_filename = "unixendings_" + filename

    # Write the file using Unix line endings
    with open(output_filename, "w", newline="\n") as outfile:
        outfile.write(data)

    print("Converted", filename, "->", output_filename)