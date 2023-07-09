
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def the_result():
    name_from_form = request.form['name']
    Dojo_Location_form = request.form['Dojo_Location']
    Favorite_Language_form = request.form['Favorite_Language']
    comment_form = request.form['comment']
    return render_template("result.html", name_on_template=name_from_form, location_on_template=Dojo_Location_form, language_on_template=Favorite_Language_form, comment_on_template=comment_form)
if __name__ == '__main__':
   app.run(debug = True)

if __name__ == '__main__':
   app.run(debug = True)











@app.route('/,addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')


app.run(debug=True)