import os, sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=("GET", "POST"))
def initial():
    if request.method == "POST":
        initial = request.form["initial"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "You are a math tutor designed to help provide simple math equation problems to students. Questions have to be suitable for average public school students ranging from grades 1-6, and can consist of addition, subtraction, multiplication, or division. In addition to questions being of the appropriate difficulty level for students in this grade range, their difficulty can also range from 'very easy' to 'very hard'. When the user states what school grade they are in, and what difficulty question they would like, you will in response state the desired math question. In response, the user will reply with the asked question, as well as their answer. If the user correctly answers the question, you will give the user a slightly more difficult question. However, if the user incorrectly answered the question, you will give them a slightly easier question."},
                {"role": "user", "content": initial}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO prompts (initial, msg) VALUES (?, ?)",
                     (initial, msg))
        conn.commit()
        conn.close()
        result = request.args.get("result")
        return redirect(url_for("question", result=msg))
    
    result = request.args.get("result")
    return render_template("initial.html", result=result)

@app.route('/question', methods=("GET", "POST"))
def question():
    if request.method == "POST":
        answer = request.form["answer"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "You are a math tutor designed to help provide simple math equation problems to students. Questions have to be suitable for average public school students ranging from grades 1-6, and can consist of addition, subtraction, muliplication, or division. In addition to questions being of the appropriate difficulty level for students in this grade range, their difficulty can also range from 'very easy' to 'very hard'. When the user states what school grade they are in, and what difficulty question they would like, you will in response state the desired math question. In response, the user will reply with the asked question, as well as their answer. If the user correctly answers the question, you will give the user a slightly more difficult question. However, if the user incorrectly answered the question, you will give them a slightly easier question."},
                {"role": "user", "content": answer}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO prompts (answer, msg) VALUES (?, ?)",
                     (answer, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("question", result=msg))
    
    result = request.args.get("result")
    return render_template("question.html", result=result)
