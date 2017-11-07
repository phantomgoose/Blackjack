from flask import Flask, render_template, request, redirect
import blackjack

app = Flask(__name__)

@app.route("/")

def root():
    if blackjack.getPlayerState() == "playing":
        continue_btn_state = "hidden"
        hit_stand_state = ""
    else:
        continue_btn_state = ""
        hit_stand_state = "hidden"
    return render_template("index.html", dealer_cards=cardsToImg(blackjack.getDealerCards()), player_cards=cardsToImg(blackjack.getPlayerCards()), output=blackjack.getGameState(), continue_btn_state=continue_btn_state, hit_stand_state=hit_stand_state)

# helper method for mapping the card object to the corresponding image
def cardToImg(card):
    return "<img src='static/svg/" + card.getShortValue() + card.getShortSuit() + ".svg'>"

# helper method that takes an array of cards and converts it to html markup that consists of corresponding card images
def cardsToImg(cards):
    res = ""
    for card in cards:
        res += cardToImg(card)
    return res

@app.route("/decide", methods=["POST"])

def decide():
    choice = request.form["choice"]
    if choice == "reset":
        # game is meant to support only a single client, so resetting just reloads the blackjack module
        reload(blackjack)
    else:
        blackjack.play(choice)
    return redirect("/")

app.run()
