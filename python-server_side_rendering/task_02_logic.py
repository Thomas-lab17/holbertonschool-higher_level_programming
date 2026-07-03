import os
from flask import Flask, render_template
import json

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
