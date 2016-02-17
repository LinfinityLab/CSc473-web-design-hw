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

def stripper(text):
    # """ Sripper takes a string as input. It 
    # removes (1) all manner of whitespace 
    # (2) commas (3) periods (4) different kinds
    # of br tags and (5) p tags. This is useful
    # for checking if the text content of 
    # a p or h1-6 matches another while ignoring
    # whitespace. 
    
    # Should be redone at somepoint with regexp
    # to be robust to style attributes and remove
    # more internal tags.
    # """
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

 
class TestProblem2(unittest.TestCase):
        @classmethod
        def setUp(cls):
            # """ Function that loads up the html file
            # for testing. The file is processed
            # using BeautifulSoup and made available
            # to the testing through the soup variable.
            # """
            cls.html = None
            with open("index.html") as fid:
                cls.html = fid.read()
                cls.soup = BeautifulSoup(cls.html)
            if not cls.html:
                raise Exception('File not read')
                
            
        @classmethod
        def tearDown(cls):
            # """ Function for cleaning up after tests:
            # You could delete index.html but
            # not neccessary
            # """
            pass


        def test_open_close_html(self):
            # """ This test must check that there is exaclty one
            # open and closing html tag
            # """
            List = self.soup.find_all("html")
            self.assertEqual(len(List), 1, "test_open_close_html failed")

        
        def test_head_in_html(self):
            # """ This test must check that there is a single head
            # tag and that it is inside the html open/close tags.
            # """

            self.assertTrue(self.soup.head in self.soup.html, "test_head_in_html failed")

            
        def test_body_in_html(self):
            # """ This test must check that there is a single body
            # tag and that it is inside the html open/close tags.
            # """ 
            n = 0
            if self.soup.body in self.soup.html:
                n += 1
            self.assertEqual(n, 1, "test_body_in_html failed")


        def test_meta(self):
            # """ This test must check that there is meta tag
            # with attribute 'charset' and value 'utf-8'
            # """
            self.assertTrue(self.soup.find_all('meta', charset="UTF-8"), "test_meta failed")
                                 
                        
        def test_title(self):
            # """ This checks that the html title is 
            # 'Text Example'.
            # """
            title_tag = self.soup.title
            for child in title_tag.children:
                txt = child
            self.assertEqual(txt, 'Text Example', "test_title failed")


        def test_for_correct_doctype(self):
            # """ This checks that the doctype is
            # present and that its html
            # """

            items = [item for item in self.soup.contents if isinstance(item, bs4.Doctype)]
            self.assertEqual(len(items), 1, "No Doctype presented")
            self.assertEqual(str(items[0]), "html", "test_for_correct_doctype failed")

        def test_h1_good_contents(self):
            # """ This checks that there is a single 
            # h1 tag present and that its contents is
            # 'Text Example' (no quotation marks).
            # """
            h1_tag = self.soup.h1
            for child in h1_tag.children:
                txt = child

            self.assertEqual(len(self.soup.find_all("h1")), 1, "test_h1_good_contents failed")
            self.assertEqual(txt, 'Text Example', "test_h1_good_contents failed")


        def test_h2_good_contents(self):
            # """ This checks that there is only one h2
            # and that it has 'T. S. Eliot: THE WASTE LAND'
            # in it. 
            # """
            h2_tag = self.soup.h2
            for child in h2_tag.children:
                txt = child

            self.assertEqual(len(self.soup.find_all("h2")), 1, "test_h2_good_contents failed")
            self.assertEqual(txt, "T. S. Eliot: THE WASTE LAND", "test_h2_good_contents failed")                
        

        def test_h3_good_contents(self):
            # """ This checks that the first of two h3
            # contains 'I. THE BURIAL OF THE DEAD' and the
            # second h3 has 'II. A GAME OF CHESS'
            # in it.
            # """

            l = self.soup("h3")
            a = l[0]
            b = l[1]
            for child1 in a.children:
                child1_txt = child1
            for child2 in b.children:
                child2_txt = child2

            self.assertEqual(child1_txt, "I. THE BURIAL OF THE DEAD", "test_h3_good_contents failed")
            self.assertEqual(child2_txt, "II. A GAME OF CHESS", "test_h3_good_contents failed")

            
            
            
        def test_p1_good_contents(self):
            # """ This compares the first paragraph to
            # the string paragraph_text1 after striping and
            # lowercasing
            # """
            if self.soup.find_all('p'):
                self.assertEqual(stripper(self.soup.find_all('p')[0].text), stripper(paragraph_text1))
            else:
                self.assertTrue(False)


        def test_p2_good_contents(self):
            # """ This compares the first paragraph to
            # the string paragraph_text2 after striping and
            # lowercasing
            # """      
            if self.soup.find_all('p'):
                self.assertEqual(stripper(self.soup.find_all('p')[1].text), stripper(paragraph_text2))
            else:
                self.assertTrue(False)
        

        def test_breaks(self):
            # """ For this one you are checking that each
            # of the lines in the verse that is suppose
            # to break has a break tag. You probably
            # should list the words you expect need to 
            # end with a break tag and use regular
            # expressions to allow for whitespace
            # between the break tag and the last word.
            # Rememver the last sentence will break because
            # of the <p> so it doesn't need a break.
            # """

            a=False
            if self.soup.find_all('p'):
                s1=str(self.soup.find_all('p')[0])
                s2=str(self.soup.find_all('p')[1])

                if re.findall(r'breeding<br>',s1)[0]=='breeding<br>' and re.findall(r'mixing<br>',s1)[0]=='mixing<br>' and \
                    re.findall(r'stirring <br>',s1)[0]=='stirring <br>'  and \
                    re.findall(r'throne,<br>',s2)[0]=='throne,<br>' and re.findall(r'glass<br>',s2)[0]=='glass<br>' and \
                    re.findall(r'vines<br>',s2)[0]=='vines<br>' and re.findall(r'out<br>',s2)[0]=='out<br>' and \
                    re.findall(r'wing\)<br>',s2)[0]=='wing)<br>' :
                    a=True
                self.assertTrue(a)
            else:
                self.assertTrue(a)

