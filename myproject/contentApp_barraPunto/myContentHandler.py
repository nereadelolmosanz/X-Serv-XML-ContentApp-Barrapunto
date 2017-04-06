#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xml.sax import SAXParseException
import urllib


class myContentHandler (ContentHandler):

    def __init__(self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.htmlNews = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True


    def endElement(self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                # To avoid Unicode trouble
                self.newsTitle = self.theContent + "."
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.htmlNews += "      <li>\n"
                self.htmlNews += "        <a href='" + self.theContent + "' "
                self.htmlNews += 'target="_blank">'
                self.htmlNews += self.newsTitle
                self.htmlNews += "</a>\n      </li>\n"
                self.inContent = False
                self.theContent = ""


    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


# --- Main prog

# Load parser and driver
theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

# Ready, set, go!
try:
    # Si no existe salta la excepcion y no se ejecuta nada mas
    # file descriptor
    # Get news from RSS
    rss = urllib.urlopen("http://www.barrapunto.com/index.rss")

    htmlNews = "    <div align=center>\n"
    htmlNews += "      <h1>Titulares Barrapunto</h1>\n"
    htmlNews += "    </div>\n"
    htmlNews += '    <HR align="center" size="2" width="450" color="black" noshade>\n'
    htmlNews += "    <ul type=square>\n"
    theParser.parse(rss)
    rss.close()
    htmlNews += theHandler.htmlNews
    htmlNews += "    </ul>\n"
    print "Parse complete"

except SAXParseException:
    print "  Error: <" + sys.argv[1] + ">  does not exist"

