from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    complexity = request.form['complexity']

    characters = get_characters(complexity)
    generated_password = generate_random_password(length, characters)

    return render_template('index.html', password=generated_password)

def get_characters(complexity):
    if complexity == 'easy':
        return string.ascii_letters
    elif complexity == 'medium':
        return string.ascii_letters + string.digits
    elif complexity == 'hard':
        return string.ascii_letters + string.digits + string.punctuation
    else:
        return string.ascii_letters + string.digits + string.punctuation + string.whitespace

def generate_random_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    app.run(debug=True)
