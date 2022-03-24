from flask import Flask, render_template, request

ttt = Flask(__name__)

@ttt.route("/" ,methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('game.html')

    return render_template('home.html')

@ttt.route("/home" ,methods = ['GET', 'POST'])
def home2():
    if request.method == 'POST':
        return render_template('game.html')

    return render_template('home.html')

@ttt.route("/game")
def game():
    return render_template('game.html')
    

@ttt.route("/stats")
def stats():
    n = 0
    return render_template('stats.html', n = n)


if __name__ == "__main__":
    ttt.run()