from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

books = [{"Author": "Orapin","Book_Name": "One-stop python", "ISBN": "978-616-204-772-5", "price": 225},
            {"Author": "Orapin","Book_Name": "Python for Data Science", "ISBN": "978-616-204-788-6", "price": 355},
            {"Author": "Orapin","Book_Name": "Java Programming", "ISBN": "978-616-204-734-3", "price": 255},
            {"Author": "Orapin","Book_Name": "C Programming", "ISBN": "978-616-204-725-1", "price": 255},
            {"Author": "Orapin","Book_Name": "Scratch 3", "ISBN": "978-616-204-720-6", "price": 185},
            {"Author": "Provision","Book_Name": "Introduction to computer", "ISBN": "978-616-204-766-4", "price": 225},
             {"Author": "Provision","Book_Name": "Computer Graphics", "ISBN": "978-616-204-787-9", "price": 325}]

@app.get("/MyBooks")
def my_books():
   return JSONResponse(status_code=201,content=books)

@app.get("/books/v1/{author}")
def findBookV1(author:str):
    results = findBookByAuthor(author)
    if len(results) > 0:
       return JSONResponse(status_code=200,content=results)
    else:
       return JSONResponse(status_code=404,content={"message": "Book not found"})

@app.get("/books/v1.1/{author}/{book_name}")
def findBookV11(author:str,book_name:str):
    results = findBookByAuthorAndBookName(author,book_name)
    if len(results) > 0:
       return JSONResponse(status_code=200,content=results)
    else:
       return JSONResponse(status_code=404,content={"message": "Book not found"})

@app.get("/books/v1.2/{author}")
#def findBookV12(author:str,book_name:str):
def findBookV12(author:str,book_name:str=None):
    results = []
    if book_name is None:
        results = findBookByAuthor(author)
    else:
        results = findBookByAuthorAndBookName(author,book_name)
    if len(results) > 0:
       return JSONResponse(status_code=200,content=results)
    else:
       return JSONResponse(status_code=404,content={"message": "Book not found"})

def findBookByAuthorAndBookName(author,name):
    search_result = []
    for book in books:
        if book.get("Author") == author and book.get("Book_Name") == name:
            search_result.append(book)
    return search_result
    
def findBookByAuthor(author):
    search_result = []
    for book in books:
        if book.get("Author") == author:
            search_result.append(book)
    return search_result