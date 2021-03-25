from flask import request, Flask
import aiml
import os

app = Flask(__name__)
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

def register(name, address, phno, dad, mom, emcon, guardian, age):
    kernel.setPredicate('name', name)
    kernel.setPredicate('address', address)
    kernel.setPredicate('phno', phno)
    kernel.setPredicate('fname', dad)
    kernel.setPredicate('mom', mom)
    kernel.setPredicate('emcon', emcon)
    kernel.setPredicate('guardian', guardian)
    kernel.setPredicate('age', age)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.args['type'] == 'register':
        register(request.args['name'], request.args['address'], request.args['phno'], request.args['dad'], request.args['mom'], request.args['emcon'], request.args['guardian'], request.args['age']);
    elif request.args['type'] == 'response':
        string = kernel.respond(request.args['message'])
        if(len(string)==0): return "I didn't get you."
        else: return kernel.respond(request.args['message'])
    return "something"

app.run(host="0.0.0.0", port=5000, debug=True)