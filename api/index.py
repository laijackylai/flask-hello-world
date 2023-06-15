from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    '''
    default route
    '''
    return 'Search Canadian Fire Data with NLTK(/data?strategy=<STRATEGY>&query=<QUERY>)'

@app.route('/data', methods=['GET'])
def data():
    '''
    get nltk data
    '''
    return 'Data'