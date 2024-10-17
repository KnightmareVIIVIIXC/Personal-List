import os

def sort_personal_list(filename):
    """Sorts entries in a file alphabetically, ignoring comment lines.

    Args:
        filename: The path to the file to sort.

    Returns:
        A list of the sorted entries.
    """

    # Get the current working directory
    current_directory = os.getcwd()

    # Join the current directory with the provided filename
    full_path = os.path.join(current_directory, filename)

    with open(full_path, 'r') as f:
        lines = f.readlines()

    # Separate comment and non-comment lines
    comment_lines = [line.strip() for line in lines if line.startswith(('!', '#'))]
    non_comment_lines = [line.strip() for line in lines if not line.startswith(('!', '#'))]

    # Sort non-comment lines
    sorted_non_comment_lines = sorted(non_comment_lines)

    # Combine sorted lines with comment lines
    sorted_file_content = []
    sorted_non_comment_index = 0

    for line in lines:
        if line.startswith(('!', '#')):
            sorted_file_content.append(line.strip())
        else:
            sorted_file_content.append(sorted_non_comment_lines[sorted_non_comment_index])
            sorted_non_comment_index += 1

    return sorted_file_content

# Example usage
filename = "personal_disallowed_domains.txt"
sorted_content = sort_personal_list(filename)

# Write the sorted content back to the file with newline characters
with open(filename, 'w') as f:
    f.write('\n'.join(sorted_content))

print("File sorted successfully!")
