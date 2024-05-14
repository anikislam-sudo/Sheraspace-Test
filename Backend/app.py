from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/linkedin/form', methods=['GET'])
def get_linkedin_form():
    linkedin_form_link = "https://www.linkedin.com/home"
    return jsonify({'linkedin_form_link': linkedin_form_link})
