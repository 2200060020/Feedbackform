from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def handle_form():
    name = request.form['name']
    feedback = request.form['feedback']

    with open('feedback.txt', 'a') as f:
        f.write(f'Name: {name}, Feedback: {feedback}\n')

    return render_template('result.html', name=name, feedback=feedback)


# Add this block at the end
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
