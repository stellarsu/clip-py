import argparse
import subprocess

# Function to copy text to the clipboard using the system's pbcopy command
def copy_clipboard(text):
    try:
        # Using the subprocess module to run the pbcopy command and passing the text as input
        subprocess.run(['pbcopy'], input=text, check=True, encoding='utf-8')
        # Returning the copied text
        return text
    except subprocess.CalledProcessError as e:
        print(f'Error: Failed to copy text to clipboard. {e}')

# Function to paste text from the clipboard using the system's pbpaste command
def paste_clipboard():
    try:
        # Using the subprocess module to run the pbpaste command and capturing the output
        return subprocess.run(['pbpaste'], capture_output=True, check=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        print(f'Error: Failed to paste text from clipboard. {e}')

def main():
    # Creating an ArgumentParser object to handle command line arguments
    parser = argparse.ArgumentParser(description='Copy or paste text to/from the clipboard')
    # Adding a mutually exclusive group of arguments, where only one of the options can be used at a time
    group = parser.add_mutually_exclusive_group(required=True)
    # Adding the -c or --copy option to copy text to the clipboard
    group.add_argument('-c', '--copy', metavar='text', help='text to copy to the clipboard')
    # Adding the -p or --paste option to paste text from the clipboard
    group.add_argument('-p', '--paste', action='store_true', help='paste text from the clipboard')
    # Adding the -v or --variable option to store the copied text in a variable
    parser.add_argument('-v', '--variable', metavar='var', help='name of variable to store copied text')
    # Parsing the command line arguments
    args = parser.parse_args()

    if args.copy:
        # Copying the text to the clipboard and storing it in a variable
        copied_text = copy_clipboard(args.copy)
        if args.variable:
            try:
                # Using the exec() function to create a variable with the provided name and assign the copied text to it
                exec(f'{args.variable} = "{copied_text}"')
                print(f'Copied text stored in variable "{args.variable}"')
            except SyntaxError as e:
                print(f'Error: Failed to create variable "{args.variable}". {e}')
    elif args.paste:
        # Pasting the text from the clipboard and printing it to the console
        print(paste_clipboard())

# Checking if the script is being run directly
if __name__ == '__main__':
    main()
