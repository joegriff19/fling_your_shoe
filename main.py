# code that runs the app
from pages import index

if __name__ == '__main__':
    index.app.run_server(debug=True)
