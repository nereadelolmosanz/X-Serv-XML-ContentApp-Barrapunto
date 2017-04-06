#!/usr/bin/python3

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp
import myContentHandler


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    
    
    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page',
               '/prueba': 'Otra pagina de prueba',
              }
    htmlNews = myContentHandler.htmlNews

    def parse(self, request):
        """Return the resource name (including /)"""
        return request.split(' ', 2)[1]


    def process(self, resourceName):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        html = "<html>\n"
        html += "  <head>\n"
        html += "    <title>ContentAppBarraPunto</title>\n"
        html += "    <meta charset='UTF-8'>\n"
        html += "  </head>\n\n"
        html += "  <body>\n"

        if resourceName in self.content.keys():
            httpCode = "200 OK"
            html += "    <h1>" + self.content[resourceName] + "</h1></br></br>"
            html += self.htmlNews                         
        else:
            httpCode = "404 Not Found"
            html += "    <h1>Not Found</h1></br></br>"
            html += "    <h3>Saved pages:</h3>"
            html += str(self.content.keys())
        
        html += "  </body>\n</html>"
        return (httpCode, html)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
