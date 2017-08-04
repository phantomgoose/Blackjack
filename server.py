from flask import Flask, render_template, request, redirect
import blackjack

app = Flask(__name__)

@app.route("/")

def root(dealer_card="", player_cards="", output=""):
    return render_template("index.html", dealer_card=blackjack.getDealerCard(), player_cards=blackjack.getPlayerCards(), output=blackjack.getGameState())

@app.route("/decide", methods=["POST"])

def decide():
    option = request.form["choice"]
    if option == "reset":
        reload(blackjack)
        return redirect("/")
    else:
        blackjack.play(option)
        return redirect("/")

app.run(debug=True)
