from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="pages",
    static_folder="style",
    static_url_path="/style",
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/table")
def table():
    return render_template("table.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)