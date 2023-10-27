import PyPDF2
import requests
import pandas as pd
import re
from collections import Counter

def open_book(url):
    response = requests.get(url)
    with open("/Users/mayconcyprianobatestin/Documents/repositorios/DATA_SCIENCE/GRAMMAR/dataset/temp.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)

    text = ""
    with open("/Users/mayconcyprianobatestin/Documents/repositorios/DATA_SCIENCE/GRAMMAR/dataset/temp.pdf", "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text

url = "https://drive.google.com/uc?export=download&id=0B5oIn4Aw7kojUzRVTEw1WjRrLW8"
text = open_book(url)
tokens = re.findall(r'\b\w+\b', text.lower())  
word_count = Counter(tokens)
df = pd.DataFrame(word_count.items(), columns=["word", "count"])
df["freq"] = df["count"] / df["count"].sum()
df.to_csv("/Users/mayconcyprianobatestin/Documents/repositorios/DATA_SCIENCE/GRAMMAR/dataset/lotr.csv", index=False)
