#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb():
    """
    Route to display a HTML page
     (inside the tag BODY)
    Use 6-index.html content as source code for the \
    template 10-hbnb_filters.html:
    Replace the content of the H4 tag under each \
    filter title (H3 States and H3 Amenities) by &nbsp;
    State, City and Amenity objects must be loaded from \
    DBStorage and sorted by name (A->Z)
    """
    table = "States"
    all_states = list(storage.all(State).values())
    all_amenities = list(storage.all(Amenity).values())
    all_places = list(storage.all(Place).values())

    return render_template("100-hbnb.html",
                           all_states=all_states, all_amenities=all_amenities, all_places=all_places)


@app.teardown_appcontext
def teardown(exception):
    """
    Closes the session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
