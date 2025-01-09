def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

function_with_closed_file("my_file.txt")

# Example of creating a file and ensuring it is closed.
with open("new_file.txt","w") as f:
    f.write("This is a test line.") 