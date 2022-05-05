@app.route("/scripts/<filename>")
def scripts(filename):
    with open(os.path.join(os.curdir, 'scripts', filename)) as f:
        return f.read()