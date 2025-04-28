from flask import Flask, render_template, request
from detection_model import analyze_account

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        account_url = request.form.get('account_url')
        result = analyze_account(account_url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
