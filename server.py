from flask import Flask, render_template, request, redirect
import blackjack

app = Flask(__name__)

@app.route("/")

def root():
    if blackjack.getPlayerState() == "playing":
        skip_state = "hidden"
        hit_stand_state = ""
    else:
        skip_state = ""
        hit_stand_state = "hidden"
    return render_template("index.html", dealer_card=blackjack.getDealerCard(), player_cards=blackjack.getPlayerCards(), output=blackjack.getGameState(), skip_state=skip_state, hit_stand_state=hit_stand_state)

@app.route("/decide", methods=["POST"])

def decide():
    option = request.form["choice"]
    if option == "reset":
        reload(blackjack)
        return redirect("/")
    elif option == "skip":
        blackjack.play("stand")
        return redirect("/")
    else:
        blackjack.play(option)
        return redirect("/")

app.run(debug=True)
