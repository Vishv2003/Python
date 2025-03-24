# Writing 
def write_to_file(filename, content):
    with open(filename, "w") as file:  
        file.write(content)
    print(f"Data written to {filename} successfully!")

# Reading 
def read_from_file(filename):
    try:
        with open(filename, "r") as file: 
            content = file.read()
        print(f"Content of {filename}:")
        print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")

# Appending
def append_to_file(filename, content):
    with open(filename, "a") as file: 
        file.write("\n" + content)
    print(f"Data appended to {filename} successfully!")

filename = "example.txt"
write_to_file(filename, "Hello, Vishv!\nThis is a file handling example.")
read_from_file(filename)
append_to_file(filename, "Appending new data to the file.")
read_from_file(filename)
