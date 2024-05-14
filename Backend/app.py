from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/linkedin/form', methods=['GET'])
def get_linkedin_form():
    linkedin_form_link = "https://www.linkedin.com/home"
    return jsonify({'linkedin_form_link': linkedin_form_link})

if __name__ == '__main__':
    app.run(debug=True)
