from flask import Flask, render_template, request
from classes.MemorPy import MemorPy
import os

app = Flask("MemorPy")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

memorpy = MemorPy()
memorpy.add("./test_text/test_1.txt")
memorpy.add("./test_text/test_2.txt")
memorpy.set_curr_txt("./test_text/test_1.txt")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "inc":
            output = memorpy.c_inc_level()
        elif action == "dec":
            output = memorpy.c_dec_level()
        elif action == "upload":
            file = request.files.get("file")

            if file and file.filename != "":
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)

                memorpy.add(filepath)
                memorpy.set_curr_txt(filepath)

                output = memorpy.current_txt.out_txt()
            else:
                output = memorpy.current_txt.out_txt()
        else:
            level = int(request.form.get("level"))
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