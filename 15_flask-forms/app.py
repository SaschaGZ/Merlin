# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/" , methods=['GET'])#, 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )



@app.route('/resp', methods=['GET', 'POST'])
def respond():
    username = request.form['username']


    return render_template('response.html', username=username, request="POST")

if __name__ == '__main__':
    app.debug = True
    app.run()
