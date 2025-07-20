# Method 1: Using try-except with manual file closing
try:
    f = open("demo.txt", "r")
    content = f.read()  # Note: f.read() with parentheses to call the method
    print("File content:")
    print(content)
    f.close()  # Always close the file
except FileNotFoundError:
    print("Error: 'demo.txt' file not found!")
except Exception as e:
    print(f"Error reading file: {e}")

print("-" * 40)

# Method 2: Better approach using 'with' statement (recommended)
try:
    with open("demo.txt", "r") as file:
        content = file.read()
        print("File content (using 'with' statement):")
        print(content)
except FileNotFoundError:
    print("Error: 'demo.txt' file not found!")
except Exception as e:
    print(f"Error reading file: {e}")

print("-" * 40)

# Method 3: Reading line by line
try:
    with open("demo.txt", "r") as file:
        print("File content (line by line):")
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.rstrip()}")  # rstrip() removes trailing newline
except FileNotFoundError:
    print("Error: 'demo.txt' file not found!")
except Exception as e:
    print(f"Error reading file: {e}")