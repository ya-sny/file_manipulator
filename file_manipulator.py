import sys
import os

def reverse(input_path, output_path):
    with open(input_path, 'r') as infile:
        content = infile.read()
        reversed_content = content[::-1]
        with open(output_path, 'w') as outfile:
            outfile.write(reversed_content)

def copy(input_path, output_path):
    with open(input_path, 'rb') as infile:
        with open(output_path, 'wb') as outfile:
            outfile.write(infile.read())

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as infile:
        content = infile.read()
        duplicated_content = content * n
        with open(input_path, 'w') as outfile:
            outfile.write(duplicated_content)

def replace_string(input_path, needle, new_string):
    with open(input_path, 'r') as infile:
        content = infile.read()
        replaced_content = content.replace(needle, new_string)
    with open(input_path, 'w') as outfile:
        outfile.write(replaced_content)

def main():
    if len(sys.argv) < 4:
        print("Insufficient arguments.")
        return
    command = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    if not os.path.exists(input_path):
        print(f"The specified input file '{input_path}' does not exist.")
        return
    if command == "reverse":
        reverse(input_path, output_path)
    elif command == "copy":
        copy(input_path, output_path)
    elif command == "duplicate-contents":
        if len(sys.argv) != 4:
            print("Insufficient arguments.")
            return
        n = int(sys.argv[3])
        duplicate_contents(input_path, n)
    elif command == "replace-string":
        if len(sys.argv) != 5:
            print("Insufficient arguments")
            return
        needle = sys.argv[3]
        new_string = sys.argv[4]
        replace_string(input_path, needle, new_string)
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
