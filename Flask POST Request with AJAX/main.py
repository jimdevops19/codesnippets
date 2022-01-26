from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_file', methods=['POST'])
def create_file():
    if request.method == 'POST':
        with open(f"{request.form.get('name')}.txt", "w") as f:
            f.write('FILE CREATED AND SUCCESSFULL POST REQUEST!')
        return ('', 204)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )