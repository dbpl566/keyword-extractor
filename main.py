from tkinter import *
import yake

# Specifying parameters for keyword extractor using YAKE
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numofKeywords = 10

kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numofKeywords, features=None)

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
    keywords = kw_extractor.extract_keywords(output_text)
    keywords = '\n'.join(str(kw) for kw in keywords)
    output_textbox.insert("1.0", keywords)
    print(keywords)

def main():
    check_keywords()
    window.mainloop()

if __name__ == '__main__':
    main()
