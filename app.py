import ebooklib
from ebooklib import epub
##from bs4 import BeautifulSoup

epub_file_path = './data/epubFile.epub'

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

test = epub2thtml(epub_file_path) 

print(test)