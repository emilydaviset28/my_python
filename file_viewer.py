filename = input("Enter file name: ")

try:
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
