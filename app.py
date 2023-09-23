from flask import Flask,render_template, request, redirect , url_for

app = Flask(__name__)

@app.route('/')

def home():
    return "This is home page"

@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/prof')

def prof():
    return render_template('profile.html')

@app.route('/profile')

def profile():
    return "<h1>This Is Profile Page </h1>"



@app.route('/heart')

def heart():
    return render_template('heart.html')




#### score profile

@app.route('/success/<int:score>')

def success(score):
    return " Person has passed the exam with marks of " + str(score)

@app.route('/fail/<int:score>')

def fail(score):
    return "Person has failed in exam with avg marks of " +str(score) 






 ### Get post methods   
    
    
@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')  
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        average_marks= (maths+science+history)//3
        
        result= " "
        if average_marks> 33:
            result = 'success'
        else:
            result= 'fail'    
            
        return redirect(url_for(result,score = average_marks))    
            
        #return render_template('calculate.html',marks= average_marks)
        #return render_template('result.html', marks= average_marks, maths= maths , science=science, history=history)


if __name__=="__main__":
    app.run(debug=True)