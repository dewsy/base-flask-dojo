import utility
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/applicant')
def first_names_list():
    first_names = utility.get_first_names()
    return render_template('index.html', first_names=first_names)





if __name__ == '__main__':
    app.run(
        debug=True,
        host = '0.0.0.0',
        port = 5000
    )