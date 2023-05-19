#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """
    Route to display a HTML page
     (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present \
        in DBStorage sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    all_states = list(storage.all(State).values())
    table = "States"
    return render_template("7-states_list.html", table=table,
                           all_states=all_states)


@app.teardown_appcontext
def teardown():
    """
    Closes the session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
