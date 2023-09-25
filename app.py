# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "ufo" # write your name
    age = "10" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father_webpage():
    #Create a variable
    name = 'xyz'
    # Pass the variable in the template
    return render_template('father.html', father_name = name)


# define the route to mother webpage
@app.route("/mother")
def mother_webpage():
    #Create a variable
    name = 'mno'
    # Pass the variable in the template
    return render_template('mother.html', mother_name = name)


# define the route to friends webpage
@app.route("/friend")
def friend_webpage():
    #Create a variable
    name = 'asdf'
    # Pass the variable in the template
    return render_template('friend.html', friend_name = name)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
