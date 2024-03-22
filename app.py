from flask import Flask, render_template, request
from wordSearchSolver import find_word

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    wordsearch = [row.split() for row in request.form['wordsearch'].split('\n')]
    results = []
    words = request.form['words'].split(',')

    for word in words:
        position = find_word(wordsearch, word.strip())
        if position:
            results.append({'word': word.strip(), 'position': position})

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
