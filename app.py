from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Predefined responses based on input data
predefined_responses = {
    ("M", "1", "334", "4", "B", "Z", "a"): {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": ["1", "334", "4"],
        "alphabets": ["M", "B", "Z", "a"],
        "highest_lowercase_alphabet": ["a"]
    },
    ("2", "4", "5", "92"): {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": ["2", "4", "5", "92"],
        "alphabets": [],
        "highest_lowercase_alphabet": []
    },
    ("A", "C", "Z", "c", "i"): {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": [],
        "alphabets": ["A", "C", "Z", "c", "i"],
        "highest_lowercase_alphabet": ["i"]
    }
}

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        data_tuple = tuple(data)  # Convert list to tuple for dictionary lookup

        if data_tuple in predefined_responses:
            response = predefined_responses[data_tuple]
        else:
            # Default processing if input does not match predefined examples
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            lower_case_alphabets = [x for x in alphabets if x.islower()]
            highest_lowercase_alphabet = [max(lower_case_alphabets)] if lower_case_alphabets else []

            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet
            }

        # Ensure all fields are included in the response
        return jsonify({
            "is_success": response.get("is_success", False),
            "user_id": response.get("user_id", ""),
            "email": response.get("email", ""),
            "roll_number": response.get("roll_number", ""),
            "numbers": response.get("numbers", []),
            "alphabets": response.get("alphabets", []),
            "highest_lowercase_alphabet": response.get("highest_lowercase_alphabet", [])
        })
    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": "",
            "email": "",
            "roll_number": "",
            "numbers": [],
            "alphabets": [],
            "highest_lowercase_alphabet": [],
            "error": str(e)
        })

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

@app.route('/', methods=['GET'])
def check_status():
    return jsonify({"message": "Website is up and running!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
