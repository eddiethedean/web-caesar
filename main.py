from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

error_msg = ''

form = """
    <!DOCTYPE html>

    <html>
    <head>
        <style>
            .error {{ color: red;}}
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
        <body>
            <h1>Caesar Rotate</h1>
            <form method='POST'>
                <label>Rotate by:
                    <input name="rot" type="text" value='{rot}' />
                </label>
                <p class="error">{rot_error}</p>
                <label>
                    <input name="input" type="textarea" value='{input_val}' />
                </label>
                <br>
                <input type="submit" value="Submit Query" />
            </form>
        </body>
    </html>
    """
def is_integer(num):
    temp = num
    if len(num)>1 and num[0]=='-':
        temp=temp[1:]
    if temp.isnumeric():
        return True
    else:
        return False

@app.route("/")
def index():
    return form.format(rot='0', rot_error='', input_val='')

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    input_val = request.form['input']
    #validate the rot is an integer
    if is_integer(rot):
        error_msg = ''
        input_val = rotate_string(input_val,int(rot))
    else:
        error_msg = 'Rotation has to be an integer!'
        rot = ''
    
    return form.format(rot=rot,rot_error=error_msg,input_val=input_val)
    #"<h1>{input}</h1>".format(input=input_val)

app.run()