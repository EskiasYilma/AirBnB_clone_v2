#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/")
@app.route("/states/<id>")
def states_id(id=None):
    """
    Route to display a HTML page
     (inside the tag BODY)

    If a State object is found with this id:
        H1 tag: “State: ”
        H3 tag: “Cities:”
        UL tag: with the list of City objects linked to the State\
         sorted by name (A->Z)
            LI tag: description of one City: <city.id>: \
            <B><city.name></B>
    Otherwise:
        H1 tag: “Not found!”
    """
    table = "States"
    all_states = list(storage.all(State).values())
    id_stat = "States"
    state = None
    if id:
        if id in [x.id for x in all_states]:
            for x in all_states:
                if id == x.id:
                    id_stat = "State"
                    state = x
        else:
            id_stat = "Not found"

    return render_template("9-states.html", id_stat=id_stat,
                           all_states=all_states, state=state)


@app.teardown_appcontext
def teardown(exception):
    """
    Closes the session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
