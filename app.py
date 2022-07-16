import ebooklib
from ebooklib import epub

epub_file_path = './data/epubFile.epub'

book = epub.read_epub(epub_file_path )
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

print(items)