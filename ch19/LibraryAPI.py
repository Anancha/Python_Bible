from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

books = [{"Author": "Orapin","Book_Name": "One-stop python", "ISBN": "978-616-204-772-5", "price": 225},
            {"Author": "Orapin","Book_Name": "Python for Data Science", "ISBN": "978-616-204-788-6", "price": 355},
            {"Author": "Orapin","Book_Name": "Java Programming", "ISBN": "978-616-204-734-3", "price": 255},
            {"Author": "Orapin","Book_Name": "C Programming", "ISBN": "978-616-204-725-1", "price": 255},
            {"Author": "Orapin","Book_Name": "Scratch 3", "ISBN": "978-616-204-720-6", "price": 185},
            {"Author": "Provision","Book_Name": "Introduction to computer", "ISBN": "978-616-204-766-4", "price": 225},
             {"Author": "Provision","Book_Name": "Computer Graphics", "ISBN": "978-616-204-787-9", "price": 325}]

@app.route("/books/v1/<author>")
def findBookV1(author):
    return jsonify(findBookByAuthor(author))
    
@app.route("/books/v1.1/<author>")
def findBookV11(author):
    book_name = request.args.get("book_name")
    if book_name is None:
        return jsonify(findBookByAuthor(author))
    else:
        return jsonify(findBookByAuthorAndBookName(author,book_name))

def findBookByAuthor(author):
    search_result = []
    for book in books:
        if book.get("Author") == author:
            search_result.append(book)
    if len(search_result) > 0:
       return search_result
    else:
       return { "Search result":"Not found" }

def findBookByAuthorAndBookName(author,name):
    search_result = []
    for book in books:
        if book.get("Author") == author and book.get("Book_Name") == name:
            search_result.append(book)
    if len(search_result) > 0:
       return search_result
    else:
       return { "Search result":"Not found" }

if __name__ == '__main__':
   app.run()