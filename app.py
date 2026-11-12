from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "wordwise-local-demo-key"

WORDS = {
    "apple": {"telugu": "ఆపిల్", "hindi": "सेब", "meaning": "A round fruit that can be red, green, or yellow."},
    "beautiful": {"telugu": "అందమైన", "hindi": "सुंदर", "meaning": "Pleasant to look at."},
    "brave": {"telugu": "ధైర్యవంతుడు", "hindi": "बहादुर", "meaning": "Ready to face danger or difficulty."},
    "book": {"telugu": "పుస్తకం", "hindi": "किताब", "meaning": "A set of pages with words or pictures."},
    "friend": {"telugu": "స్నేహితుడు", "hindi": "दोस्त", "meaning": "A person you know and like."},
    "happy": {"telugu": "సంతోషంగా", "hindi": "खुश", "meaning": "Feeling pleased or joyful."},
    "learn": {"telugu": "నేర్చుకో", "hindi": "सीखना", "meaning": "To gain knowledge or a skill."},
    "water": {"telugu": "నీరు", "hindi": "पानी", "meaning": "The clear liquid that people drink."},
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    searched = ""
    if request.method == "POST":
        searched = request.form.get("word", "").strip().lower()
        result = WORDS.get(searched)
    favorites = session.get("favorites", [])
    return render_template("index.html", result=result, searched=searched,
                           words=WORDS, favorites=favorites)

@app.route("/favorite/<word>", methods=["POST"])
def favorite(word):
    favorites = session.get("favorites", [])
    if word in favorites:
        favorites.remove(word)
    elif word in WORDS:
        favorites.append(word)
    session["favorites"] = favorites
    return redirect(url_for("home"))

if __name__ == "__main__":
    print("\\nWordWise is ready! Open http://127.0.0.1:5000 in your browser.\\n")
    app.run(debug=True)
