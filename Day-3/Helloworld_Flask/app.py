# 1. Import Flask.
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return "Welcome to my API!"

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received a request for the 'about' page")
    return f"My name is Slim Shady ant I'm at Gotham City!"

@app.route("/contact")
def contact():
    print("Server received request for 'Contact' page")
    return f"You can contact me at SShardy@api.com"

if __name__ == "__main__":
    app.run(debug=True)
