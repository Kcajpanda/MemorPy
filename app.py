from flask import Flask, render_template, request
from classes.MemorPy import MemorPy

app = Flask("MemorPy")

memorpy = MemorPy()
memorpy.add("./test_text/test_1.txt")
memorpy.add("./test_text/test_2.txt")
memorpy.set_curr_txt("./test_text/test_1.txt")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # 1. get slider value
        level = int(request.form.get("level"))

        # 2. store previous level (CRITICAL for your system)
        # memorpy.save_level()

        # 3. update level using your backend command
        output = memorpy.c_set_level(level)
    else:
        output = memorpy.current_txt.out_txt()

    return render_template(
        "index.html",
        text=output,
        level=memorpy.current_txt.get_level(),
        max_level=memorpy.current_txt.get_max_level()
    )


if __name__ == "__main__":
    app.run(debug=True)