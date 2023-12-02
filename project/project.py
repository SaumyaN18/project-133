from flask import Flask
app = Flask(__name__)
@app.route('/Mother')    #creationg an OPI
def first_flask():
    return 'Name: Manisha Narang , Age: 55'

@app.route('/Me')
def second_flask():
    return 'Name: Saumya , Age: 15'

@app.route('/Father')
def third_flask():
    return 'Name: Sanjay Narang , Age: 55'
app.run()