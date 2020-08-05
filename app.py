from flask import Flask, render_template, redirect, url_for, jsonify
import poembot

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello sun!"

@app.route('/poem')
def poem():
 poem = poembot.generate_poem()
 return poem

if __name__ == '__main__':
    app.run(debug=True)