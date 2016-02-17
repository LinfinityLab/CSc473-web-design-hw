from flask import render_template
from flask import url_for
import re
from bs4 import BeautifulSoup
from coreapp import app

def get_chap_links(page):
    soup = BeautifulSoup(page)
    links = [str(link.get('href'))[1:]
             for link in soup.find_all('a') if link.get('href')]
    return links

def parse_wizofoz():
    page = render_template('wizofoz.html')
    links = get_chap_links(page)
    sections = {}
    for ind in range(len(links)):
        section = {}
        start = links[ind]
        if ind < len(links)-1:
            end = links[ind+1]
            patt = ('<a name="{}"></a>(.*)' + '<a name="{}"></a>').format(start,end)
            match = re.search(patt,page,re.MULTILINE|re.DOTALL)
        else:
            patt = '<a name="{}"></a>(.*)<pre>'.format(start)
            match = re.search(patt,page,re.MULTILINE|re.DOTALL)
        if match:
            soup = BeautifulSoup(match.group(1))
            plist = [p.contents[0] for p in soup.find_all('p')]
            section['title']= (soup.find('h3').contents)[0]
            section['plist']= plist
            sections[start] = section
    return links, sections



@app.route('/')
def home():
    links, sections = parse_wizofoz()
    chap = len(links)
    title = "The Wonderful Wizard of Oz"
    section = []
    for i in range(chap):
        section.append(str(sections[links[i]]['title']))
    image_url = '/static/title_img.jpg'
    return render_template('home.html', title = title, image_url = image_url, section = section, n = chap, links = links)


@app.route('/<page>')
def section(page):
    links, sections = parse_wizofoz()
    chap = len(links)
    title=sections[links[int(page)]]['title']
    section = []
    paragraphs = []
    for i in range(chap):
        section.append(str(sections[links[i]]['title']))
    paragraphs = sections[links[int(page)]]['plist']
    return render_template('section.html', n = chap, section = section, title = title, paragraphs = paragraphs)


