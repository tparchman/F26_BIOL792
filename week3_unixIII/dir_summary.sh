#!/bin/zsh
# Tell the system to run this script using zsh.

DIR=$1
# Store the first command-line argument in a variable called DIR.

echo "Directory summary for: $DIR"
# Print a heading showing the directory being summarized.

echo "----------------------------------------"
# Print a divider to make the output easier to read.

NFILES=$(find "$DIR" -type f | wc -l)
# Find all files in the directory and its subdirectories, then count them.

NDIRS=$(find "$DIR" -type d | wc -l)
# Find all directories, including DIR itself, and count them.

SIZE=$(du -sh "$DIR" | cut -f1)
# Calculate the total disk space used by the directory and save only the size.

echo "Number of files:       $NFILES"
# Print the number of files.

echo "Number of directories: $NDIRS"
# Print the number of directories.

echo "Total disk space:      $SIZE"
# Print the total disk space occupied by the directory and its contents.

echo
# Print a blank line.

echo "Directory tree:"
# Print a heading for the directory tree.

echo "----------------------------------------"
# Print another divider.

tree "$DIR"

# Display the directory and its contents as a tree.