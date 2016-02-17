import os
import re
import shutil
try:
    import unittest2 as unittest
except ImportError:
    import unittest
    

from subprocess import Popen, PIPE
from bs4 import BeautifulSoup 
import bs4

from HTMLParser import HTMLParser

paragraph_text1 = """
April is the cruellest month, breeding
Lilacs out of the dead land, mixing
Memory and desire, stirring 
Dull roots with spring rain ...
"""

paragraph_text2 = """
The Chair she sat in, like a burnished throne,
Glowed on the marble, where the glass
Held up by standards wrought with fruited vines
From which a golden Cupidon peeped out
(Another hid his eyes behind his wing)
Doubled the flames of sevenbranched candelabra ...
"""

html_doc =  """

<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8"></meta>
    <title>Text Example</title>
</head>
<body>
<h1>Text Example</h1>
<h2>T. S. Eliot: THE WASTE LAND</h2>
<h3>I. THE BURIAL OF THE DEAD</h3>

<p>April is the cruellest month, breeding<br>
Lilacs out of the dead land, mixing<br>
Memory and desire, stirring <br>
Dull roots with spring rain ...</p>

<h3>II. A GAME OF CHESS</h3>
<p>The Chair she sat in, like a burnished throne,<br>
Glowed on the marble, where the glass<br>
Held up by standards wrought with fruited vines<br>
From which a golden Cupidon peeped out<br>
(Another hid his eyes behind his wing)<br>
Doubled the flames of sevenbranched candelabra ... </p>

</body>
</html>

"""

soup = BeautifulSoup(html_doc, 'html.parser')

def test_for_correct_doctype(self):
    # items = [item for item in soup.contents if isinstance(item, bs4.Doctype)]
    # return items[0] if items else None
    items = [item for item in self.contents]
    # for a in range(len(items)):
    # 	if isinstance(items[a], bs4.Doctype):

    return str(items[1])


print test_for_correct_doctype(soup)

def stripper(text):
    """ Sripper takes a string as input. It 
    removes (1) all manner of whitespace 
    (2) commas (3) periods (4) different kinds
    of br tags and (5) p tags. This is useful
    for checking if the text content of 
    a p or h1-6 matches another while ignoring
    whitespace. 
    
    Should be redone at somepoint with regexp
    to be robust to style attributes and remove
    more internal tags.
    """
    return text.lower().replace('\n',''
                      ).replace('\f',''
                      ).replace('\v',''                      
                      ).replace('\t',''
                      ).replace('\r',''
                      ).replace(' ',''
                      ).replace('</br>',''
                      ).replace('<br/>',''
                      ).replace('<br>',''
                      ).replace(',',''
                      ).replace('.',''
                      ).replace('<p>',''
                      ).replace('</p>',''
                      )


# def test_p1_good_contents(self):
#     l = self("p")
#     a = l[1]
#     for child in a.children:
#         txt = child
# 	# if (stripper(txt) == paragraph_text1):
# 	# 	return true
# 	# return stripper(txt)
# 	return txt

# print test_p1_good_contents(soup)

# print soup.find_all('p')[0].string


mystr = str(soup.find_all('p')[1])
wordList = re.sub("[\Z]", " ",  mystr).split()
for word in wordList:
  if ('throne,<br>' == word):
      print "True"
