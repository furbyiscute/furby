class send_function():
    """runs a function on a server!!!"""
    """also return_ is not always a string"""
    def __init__(self, function_code):
        import socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(("192.168.0.199",9546))
        function_code = str(function_code)
        server.send(function_code.encode("ascii"))
        self.return_ = server.recv(1000).decode("ascii")
        exec("self.return_ = " + self.return_)
        server.close()