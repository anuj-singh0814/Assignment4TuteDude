### Read a File and Handle Errors

def read_and_print_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            print(f"Reading file contents:\n")
            # Read and print each line
            for line in file:
                print(line, end='')  # end='' avoids extra newlines (since lines already contain them)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Specify the filename
filename = "sample.txt"

# Call the function
read_and_print_file(filename)