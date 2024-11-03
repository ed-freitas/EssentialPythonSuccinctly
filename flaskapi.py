from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Sample data for the API
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

# Define routes below
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = books[-1]["id"] + 1 if books else 1  # Auto-increment ID
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book), 200
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)