# python
from flask import Flask, render_template, redirect, request
import random
import string

app = Flask(__name__)

#@app.route('/generate_password')
#def home():
    #return render_template('pass_test.html')



@app.route('/generate_password', methods=['GET', 'POST'])
def generate_password():
    if request.method == 'POST':
        length = request.form['lengthh']
        z = int(length)
        letters = ' '
        if request.form.get('upper'):
            letters += string.ascii_letters.upper()
        if request.form.get('lower'):
            letters += string.ascii_letters.lower()
        if request.form.get('nums'):
            letters += string.digits
        if request.form.get('sym'):
            letters += string.punctuation
        password = ''.join(random.choice(letters) for i in range(z))
        return render_template('pass_test.html', password=password)
    if request.method == 'GET':
        return render_template('pass_test.html')

    #if request.method == 'POST':
        #return render_template('pass_test.html', lengthh=length)








if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')