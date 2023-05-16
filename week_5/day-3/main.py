import json
import logging
import threading
import time
import os

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler()] 
)

TODO_FILE_NAME = "/app/data/todo.json" 


def load_todo_items():
    if os.path.exists(TODO_FILE_NAME):
        with open(TODO_FILE_NAME) as f:
            return json.load(f)
    return []


def save_todo_items():
    while True:
        time.sleep(10)
        with open(TODO_FILE_NAME, "w") as f:
            json.dump(app.config["TODO_ITEMS"], f)


@app.before_first_request
def initialize_todo_items():
    app.config["TODO_ITEMS"] = load_todo_items()
    saving_thread = threading.Thread(target=save_todo_items)
    saving_thread.start()


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        app.config["TODO_ITEMS"].append(content)

    return render_template("index.html", todo_items=app.config["TODO_ITEMS"])


if __name__ == "__main__":
    if os.getenv('FLASK_ENV') == 'production':
        app.debug = False
    app.run(host="0.0.0.0", port=7000)
