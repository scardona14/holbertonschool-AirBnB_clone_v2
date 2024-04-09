"""
A script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    Display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by name
    LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    states = storage.all(State).values()
    states=sorted(states, key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=states)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by name
    LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    states = storage.all(State).values()
    states=sorted(states, key=lambda k: k.name)
    sc = []
    for state in states:
        sc.append([state, sorted(states.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_states.html', states=sc, h1="States")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)