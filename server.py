from flask import request, Flask
import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.args['type'] == 'register':
        main.register(request.args['name'], request.args['address'], request.args['phno'], request.args['dad'], request.args['mom'], request.args['emcon'], request.args['guardian'], request.args['age']);
    return "something"

app.run(host="0.0.0.0", port=5000, debug=True)