import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        try:
            self.response.header['Content-Type'] = 'text/html'
            self.response.write('<html><body><p>hello world</p></body></html>')

        except:
            self.response.write('<html><body><p>Annie, invalid inputs</p></body></html>')

    def post(self):
        try: 
            self.request.post('second')
        except:
            self.response.write('<html><body><p>Posted.</p></body></html>')

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)