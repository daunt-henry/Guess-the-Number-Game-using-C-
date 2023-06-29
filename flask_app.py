from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        number = int(request.form["number"])
        guess = request.form["guess"]
        nguesses = int(request.form["nguesses"])

        if guess == '':
            return render_template("play.html", error="Please enter a valid guess.")

        guess = int(guess)

        if guess > number:
            message = "Lower number please!"
        elif guess < number:
            message = "Higher number please!"
        else:
            message = f"You guessed it in {nguesses} attempts"

        nguesses += 1

        # Compile and run the C program
        process = subprocess.Popen(["gcc", "game.c", "-o", "game"], stderr=subprocess.PIPE)
        error = process.stderr.read()
        if error:
            return render_template("play.html", error=error.decode("utf-8"))

        output = subprocess.check_output("./game", encoding="utf-8")

        return render_template("play.html", message=message, guess=guess, nguesses=nguesses, output=output)

    else:
        return render_template("play.html")

if __name__ == "__main__":
    app.run()
