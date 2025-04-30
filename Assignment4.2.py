
def file_operations():
    # Step 1: Write initial user input to file
    initial_text = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(initial_text + "\n")
    print("Data successfully written to output.txt.\n")

    # Step 2: Append additional user input
    append_text = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(append_text + "\n")
    print("Data successfully appended.\n")

    # Step 3: Read and display final content
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    file_operations()