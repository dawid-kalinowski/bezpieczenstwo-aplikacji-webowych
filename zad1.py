from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return username == 'dawid' and password == '1234'

@app.route('/api/secure')
@auth.login_required
def secure_resource():
    return 'siema!'

if __name__ == '__main__':
    app.run(debug=True)
