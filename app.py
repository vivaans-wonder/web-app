from flask import Flask,render_template,request,session,redirect
app=Flask(__name__)
app.config["SECRET_KEY"]="Hi"

@app.route("/") 
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/validate_register', methods=['POST'])
def validate_register():
    username=request.form.get('username')
    password=request.form.get('password')
    confirm_password=request.form.get('confirm_password')
    email=request.form.get('email')

    if password==confirm_password:
        print('registration success')
        message='registered sussessfully'
        session['registered']=True
        session['email']=email
        session['username']=username
        session['password']=password
        registered = session.get('registered',False)
        return render_template('login.html',message=message,registered=registered)
    else:
        print('Unsuccessful')
        return redirect('/register')

@app.route('/login')    
def login():
    return render_template("login.html")

@app.route('/validate_user',methods=['POST'])
def validate_user():
   username=request.form.get("username")
   password=request.form.get("password")
   message=""
   session_un=session.get('username','No User')
   session_pwd=session.get('password','No Password')
   if session_pwd==password and session_un==username:
       message="login successful:)"
       session['authenticated'] =True
       return render_template('home.html',message=message,score=0) 
   else:
       message="login failed:( "   
       session['authenticated']=False
       return render_template('login.html',message=message)

#question 1--------quiz 
def validate_quiz(correct_choice):
    user_choice=request.form.get("select")
    message=""
    score=session.get("score",0)
    if user_choice==correct_choice:
        message="Your answer is correct!"
        score+=10
    else:
        message="Your answer is incorrect!"   
    session["score"]=score 
    return message

@app.route('/q1',methods=['POST','GET'])
def q1():
    if request.method=='GET':
        return render_template('question1.html')
    session['attempted_questions']=[]
    if session['authenticated']:
        return render_template("question1.html",score=0)
    else:
        return render_template('login.html',message='please login first to view the quiz content')

@app.route('/validateq1',methods=['POST'])
def validateq1():
    # attempted_questions=session.get('attempted_questions',[])
    # print(attempted_questions)
    # if 'q1' in attempted_questions:
    #     return render_template('error.html',message="question attempted already")
    # attempted_questions.append('q1')
    # session['attempted_questions']=attempted_questions
    message=validate_quiz('1')
    score=session.get('score',0)
    return render_template("question2.html",message=message,score=score)  
        

@app.route('/validateq2',methods=['POST'])
def validateq2():
    message=validate_quiz('1')
    score=session.get('score',0)
    return render_template("question3.html",message=message,score=score)    

@app.route('/validateq3',methods=['POST'])
def validateq3():
    message=validate_quiz('4')
    score=session.get('score',0) 
    return render_template("question4.html",message=message,score=score)    

@app.route('/validateq4',methods=['POST'])
def validateq4():
    message=validate_quiz('4')
    score=session.get('score',0)        
    return render_template("question5.html",message=message,score=score)     

@app.route('/validateq5',methods=['POST'])
def validateq5():
    message=validate_quiz('1')
    score=session.get('score',0)     
    return render_template("question6.html",message=message,score=score)  

@app.route('/validateq6',methods=['POST'])
def validateq6():
    message=validate_quiz('2')
    score=session.get('score',0)      
    return render_template("question7.html",message=message,score=score)     

@app.route('/validateq7',methods=['POST'])
def validateq7():
    message=validate_quiz('3')
    score=session.get('score',0)     
    return render_template("question8.html",message=message,score=score)     

@app.route('/validateq8',methods=['POST'])
def validateq8():
    message=validate_quiz('3')
    score=session.get('score',0)     
    return render_template("question9.html",message=message,score=score)

@app.route('/validateq9',methods=['POST'])
def validateq9():
    message=validate_quiz('1')
    score=session.get('score',0)    
    return render_template("question10.html",message=message,score=score)

@app.route('/validateq10',methods=['POST'])
def validateq10():
    message=validate_quiz('4')
    score=session.get('score',0)     
    return render_template("thanku.html",message=message,score=score)

@app.route('/thanku')
def thanku():
    score=session.get("score",0)
    return render_template("thanku.html",score=score)    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/home')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/feedback')
def feedback():
     return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)