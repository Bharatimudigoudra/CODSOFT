from flask import Flask, render_template, request
import random

app = Flask(__name__)

user_score = 0
computer_score = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ['rock', 'paper', 'scissors']
    user_choice = request.form.get('choice')
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    return render_template('result.html', user_choice=user_choice.capitalize(),
                           computer_choice=computer_choice.capitalize(),
                           result=result, user_score=user_score, computer_score=computer_score)

def determine_winner(user, computer):
    global user_score, computer_score

    if user == computer:
        return 'It\'s a tie!'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        user_score += 1
        return 'You win!'
    else:
        computer_score += 1
        return 'You lose!'

if __name__ == '__main__':
    app.run(debug=True)
