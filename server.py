from flask import Flask, render_template, request
from pokemon import get_pokemon
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/pokemon")
def get_pokemon_by_name():
    pokemon_name = request.args.get("pokemon_name")
    pokemon_data = get_pokemon(pokemon_name)
    return render_template("pokemon.html",
                           name=pokemon_data["name"],
                           order=pokemon_data["order"],
                           sprite=pokemon_data["sprites"]["front_default"])


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)