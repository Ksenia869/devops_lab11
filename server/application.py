""" test ci """
import http.server
import socketserver

PORT = 8000

class TestMe():
    """test class"""
    def take_five(self):
        """4 replace with 5"""
        return 5

    def port(self):
        """port"""
        return PORT

if __name__=='__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("",PORT),Handler) as http:
        print("servingatport", PORT)
        http.serve_forever()