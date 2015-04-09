#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string


def normalize_whitespace(text):
    return string.join(string.split(text), ' ')


class CounterHandler(ContentHandler):

    def __init__(self):
        self.inContent = 0
        self.theContent = ""
        self.news = 1
        self.xml = open("file.html", "w")
        self.out = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.link = normalize_whitespace(attrs.get('rdf:about'))
            self.inContent = 1

def endElement(self, name):
    if self.inContent:
        self.theContent = normalize_whitespace(self.theContent)
    if name == 'title' and self.inContent:
        self.out = ("<li><a href=" + self.link + ">" +
                    "Title " + str(self.news) + ": " +
                    self.theContent + "</a></li>\n")
        self.xml.write(self.out.encode('utf8'))
        self.inContent = 0
        self.theContent = ""
        self.news = self.news + 1

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


# --- Main prog

if len(sys.argv) < 2:
    print "Usage: python xml-parser-barrapunto.py <document>"
    print
    print " <document>: file name of the document to parse"
    sys.exit(1)

# Load parser and driver

JokeParser = make_parser()
JokeHandler = CounterHandler()
JokeParser.setContentHandler(JokeHandler)

# Ready, set, go!

xmlFile = open(sys.argv[1], "r")
JokeParser.parse(xmlFile)

print "Parse complete"

