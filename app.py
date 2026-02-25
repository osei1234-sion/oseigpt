1from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "OseiGPT is running successfully on Render!"

if __name__ == "__main__":
    app.run()