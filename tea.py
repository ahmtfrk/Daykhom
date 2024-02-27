from flask import Flask, render_template, request

app = Flask(__name__)

# Poll questions related to the Tea project
poll_questions = [
    "How long have you been following the Tea project?",
    "Which feature of the Tea project is most important to you?"
]

# Poll results
poll_results = {
    question: {} for question in poll_questions
}

@app.route('/')
def index():
    return render_template('index.html', questions=poll_questions)

@app.route('/poll', methods=['POST'])
def poll():
    for question in poll_questions:
        answer = request.form.get(question)
        if answer:
            poll_results[question][answer] = poll_results[question].get(answer, 0) + 1
    return render_template('results.html', results=poll_results)

if __name__ == '__main__':
    app.run(debug=True)
