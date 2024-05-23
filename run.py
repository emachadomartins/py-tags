from src.main.server.server import server

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=3000, debug=True)
