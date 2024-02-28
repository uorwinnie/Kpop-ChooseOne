from flask import Flask, request, render_template ,redirect
import re

app = Flask(__name__)

@app.route('/')
def main():
   return redirect("/login")

infos = {"winnie":"123456","logan":"111111"}

@app.route('/data', methods =["POST"])
def data():
   if request.method == "POST":
      username = request.form.get("userName")
      password = request.form.get("userPassword")
      return final_login(username,password)

def final_login(username,password):
   txt=None
   if login_valid(username,password) == 1:
      return redirect("/quiz")
   else:
      txt="Username or password is wrong"
      return render_template("login.html",txt=txt)

answers ={"oldest":"3","member":"3","youngest":"1","year":"2","debut":"1"}
@app.route('/quizdata', methods =["POST"])
def quiz():
   if request.method == "POST":
      ans=[]
      for i in answers:
         ans.append(request.form.get(i))
      score=check_ans(ans)
      return render_template("score.html",score=score)


@app.route('/signup-data',methods=["POST"])
def sdata():
   if request.method =="POST":
      email = request.form.get("email")
      password = request.form.get("userPassword")
      cpassword = request.form.get("cPassword")
      error = valid_email(email)
      return next_stage(password, cpassword,error)

def next_stage(password, cpassword,error):
   if valid_pw(password, cpassword) == None and error == None:
      return redirect('/quiz')
   else:
      msg=valid_pw(password, cpassword)
      return render_template("signup.html", msg=msg,error=error)


def login_valid(username,password):
   if (username in infos.keys()) and password==infos[username]:
      return 1
   else:
      return 2

def check_ans(ans : list) ->int:
   score = 0
   for i in answers:
      if ans.pop(0) ==answers[i]:
         score+=1
   return score

def valid_email(email):
   regex = r'^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
   if re.fullmatch(regex,email):
      return None
   return "Invalid email"

def valid_pw(password, cpassword):
   if len(password)>=6:
      if password == cpassword:
         return None
      else:
         return "Passwords didn't match"
   else:
      return "Password must have six characters at least"

@app.route('/login')
def login():
   return render_template("login.html")

@app.route('/quiz')
def run_quiz():
   return render_template("quiz.html")

@app.route('/register')
def register():
   return render_template("signup.html")

@app.route('/score')
def score():
   return redirect('/quiz')

if __name__=='__main__':
   app.run(debug=True)
