from flask import Flask, render_template, request, redirect
from classes.MemorPy import MemorPy

app = Flask(__name__)

memorpy = MemorPy()
memorpy.add("./test_text/test_1.txt")
memorpy.current_txt = memorpy.texts[-1]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "harder":
            memorpy.current_txt.inc_level()
        elif action == "easier":
            memorpy.current_txt.dec_level()

    output = memorpy.current_txt.out_txt()
    return render_template("index.html", text=output)


if __name__ == "__main__":
    app.run(debug=True)