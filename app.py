from flask import Flask

app = Flask("software_house_chatbot")

@app.route("/")
def home():
    return "Software House Chatbot API is running"

if __name__ == "__main__":
    app.run(port=5000)
