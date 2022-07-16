import ebooklib
# import os
from ebooklib import epub

# from bs4 import BeautifulSoup
# import nltk

## relative epub file path
epub_file_path = './data/epubFile.epub'
  


book = epub.read_epub(epub_file_path)

for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    print(doc.content)

 