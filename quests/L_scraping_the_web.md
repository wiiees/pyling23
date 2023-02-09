# Python for Linguists 2023

## Coding Quest L: Scraping the web

**_Finish [Section 20](../exercises/20_reading_and_writing_files.md) before attempting this quest._**


**L.1.** With Python you can read not only local files on your computer, but also, e.g., webpages, with similar syntax as before but using `urlopen` from the `urllib.request` module (https://nos.nl is the Dutch public broadcaster's website): 

```python
from urllib.request import urlopen

with urlopen('https://nos.nl') as htmlreader:
    web_content = htmlreader.read()
```

**L.2.** What is the `type` of the resulting object? It is not a string, because it has not been _decoded_ yet: if you did the optional Section 4 you may recall that which bytes (i.e., sequences of 8 bits) correspond to which characters depends on the file's _encoding_ or _character set_ (charset). `.html` pages should specify the intended encoding in the 'header' of the file. By printing `web_content` and then manually browsing or searching (`ctrl`+`f`), can you find something about a `charset`? Which charset does the above webpage use? Verify that the same charset is the one automatically retrieved by calling `htmlreader.headers.get_content_charset()` on the file's `htmlreader`.

**L.3.** Decode the plain bytes you stored in `web_content` into the intended characters (i.e., a plain string) by calling the method `web_content.decode(...)` with the right encoding as an argument, and print the result. (If you have ever used an ordinary web browser to look at the _source_ of a website, this is the same thing.)

**L.4.** With the content of a website loaded in Python, you can process it as any ordinary string (e.g., split, strip, loop over it), but that is not ideal, as html-code has a specific structure that we should exploit. For instance, images are included with the `<img>` tag and have a `src=...` attribute:
```html
<img alt="" decoding="async" loading="lazy" src="https://cdn.nos.nl/image/2023/01/15/934129/576x768a.jpg" class="sc-7ad7f778-1 iyuVbh"/>
```
The library **BeautifulSoup** provides ways to parse and search through `.html` code (as well as `.xml` files, which are sometimes used in linguistics for annotated corpora); it is named after 'tag soup' as a metaphor for badly written html/xml code. Do `import bs4` and then call `bs4.BeautifulSoup(...)` on the web content you, and inspect the resulting object (e.g., with `type`, `dir`) to get an overview of its methods. 

**L.5.** In fact, if you use BeautifulSoup to parse the html, then you can skip the manual decoding step we did earlier, as BeautifulSoup takes care of this automatically. Indeed, you can even pass the `htmlreader` into BeautifulSoup directly, without first calling `read()` on it. Verify this with code. 

**L.6.** ⭐ One of the methods that exists on the resulting object of parsed html is `findall`. Call its method `find_all('img')` (i.e., as a method 'on' the object) to find all image tags. Loop over these, and from each image retrieve the `src` attribute (with the same syntax as retrieving the value of a key from a dictionary), and print it.

**L.7.** ⭐⭐ Note that the resulting 'image sources' are themselves urls. This means you can use `urlopen` to retrieve the images. Find a way to save all images to a folder on your computer (with appropriate filenames derive from the original image url). You should know enough now, about reading and writing files, to experiment your way towards a solution, with the occasional help of a web search if you encounter an unfamiliar error (e.g., you will likely encounter `TypeError: write() argument must be str, not bytes`).

**L.8.** ⭐ (Conceptual, no programming:) Of course scraping the web can be done not just to obtain html pages or images, but also videos or sound files, and any other files you may find online. Think of a number of (types of) websites where you think one could retrieve data interesting for linguistic analysis.