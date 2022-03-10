from tkinter import *

window = Tk()
window.title("Keyword Extractor")

# Input single or multiple lines of text
input_textbox = Text(window)
input_textbox.grid(row=0, column=0, padx=10, pady=(30, 50), sticky=E)

# Output single or multiple lines of text
output_textbox = Text(window)
output_textbox.grid(row=0, column=1, padx=10, pady=(30, 50))

# Creates button to process input text when clicked
def check_keywords():
    print_button = Button(window, text="Find Keywords", command= lambda:print_output())
    print_button.grid(row=1, column=0, sticky=E, padx=(0, 10), pady=(5, 5))

# Print input from text box
def print_output():
    output_text = input_textbox.get("1.0", "end-1c")
    output_textbox.insert("1.0", output_text)
    print(output_text)

def main():
    check_keywords()
    window.mainloop()

if __name__ == '__main__':
    main()
