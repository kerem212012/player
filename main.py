from livereload import Server

if __name__ == '__main__':
    server = Server()
    server.watch('index.html')
    server.serve(root='.')