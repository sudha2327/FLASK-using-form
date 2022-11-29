from flask import *
from forms import Contactform

app=Flask(__name__)
app.secret_key="development key"

@app.route('/contact',methods=['POST','GET'])

def contact():
    form=Contactform()

    if request.method=='POST':
        if form.validate()==False:
            flash('ALL fields are required')
            return render_template('contact.html',form=form)
        else:
            return render_template('success.html')
    elif request.method=='GET':
        return render_template('contact.html',form=form)   
@app.route('/success',methods=['POST','GET'])

def success():
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)


