from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

class CreateAPI:
    names = [
        {'bookId': 1001, 'bookName': 'My Life My Rule', 'bookPrice': 120.11},
        {'bookId': 1002, 'bookName': 'Hello Alexa', 'bookPrice': 50.11},
        {'bookId': 1003, 'bookName': 'Role Model', 'bookPrice': 99.00}
    ]

    @app.route('/listAllBooks', methods=['GET'])
    def get_books():
        """
        Get all books
        ---
        responses:
          200:
            description: Successful operation
            schema:
              {    "type": "array",
                    "items": {
                        "$ref": "#/definitions/books"
                },
            "definitions": {
                "books": {
                    "type": "object",
                    "additionalProperties": false,
                    "properties": {
                        "bookId": {
                            "type": "integer"
                        },
                        "bookName": {
                            "type": "string"
                        },
                        "bookPrice": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "bookId",
                        "bookName",
                        "bookPrice"
                    ],
                    "title": "books"
                    }
                }
            }
        """
        return jsonify(CreateAPI.names)

# Swagger definition for the Book schema
app.config['SWAGGER'] = {
    'title': 'Book API',
    'uiversion': 3
}

@app.route('/apidocs')
def apidocs():
    return jsonify(swagger(app))

if __name__ == '__main__':
    app.run(debug=True)
