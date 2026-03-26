from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    date = request.form['date']
    start = request.form['start']
    end = request.form['end']

    return f"Booked for {date} from {start} to {end}"


if __name__ == "__main__":
    app.run(debug=True)