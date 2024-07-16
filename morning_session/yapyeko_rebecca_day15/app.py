
from flask import Flask, render_template, request, redirect, url_for

# Initialize the instance of the Flask class
app = Flask(__name__)

# Create wild conservation species list
species_list = [
    {"name": "Elephant", "habitat": "Africa"},
    {"name": "lion", "habitat": "Africa"},
    {"name": "Giraffe", "habitat": "Africa"},
    {"name": "Tiger", "habitat": "Africa"},
    {"name": "bat", "habitat": "Africa"},
    {"name": "penguin", "habitat": "Africa"},
    {"name": "seal", "habitat": "Africa"},
    {"name": "Eagle", "habitat": "Africa"},
    {"name": "Falcon", "habitat": "Africa"},
    {"name": "Ostrich", "habitat": "Africa"},
]

@app.route('/')
def index():
    return render_template('index.html', species_list=species_list)

@app.route('/add_species', methods=['GET', 'POST'])
def add_species():
    if request.method == 'POST':
        name = request.form['name']
        habitat = request.form['habitat']
        species_list.append({"name": name, "habitat": habitat})
        return redirect(url_for('index'))
    return render_template('add_species.html')

if __name__ == '__main__':
    app.run(debug=True)
  