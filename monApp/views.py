from .app import app

@app.route('/')
def index():
    return "Hello world !"
    

@app.route("/about/")
def about():
    return app.config["ABOUT"]


@app.route("/contact/")
def contact():
    return app.config["CONTACT"]

if __name__== "__main__" :
    app.run()