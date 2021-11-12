from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/MyBooks")
def my_books():
   books = [{"Book_Name": "One-stop python", "ISBN": "978-616-204-772-5", "price": 225},
            {"Book_Name": "Python for Data Science", "ISBN": "978-616-204-788-6", "price": 355},
            {"Book_Name": "Java Programming", "ISBN": "978-616-204-734-3", "price": 255},
            {"Book_Name": "C Programming", "ISBN": "978-616-204-725-1", "price": 255},
            {"Book_Name": "Scratch 3", "ISBN": "978-616-204-720-6", "price": 185}]
   return jsonify(books)

if __name__ == "__main__":
   app.run()