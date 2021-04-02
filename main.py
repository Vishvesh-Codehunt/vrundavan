from flask import Flask, render_template, request, url_for, redirect
import smtplib
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resumes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    resume = db.Column(db.LargeBinary, nullable=False)

# db.create_all()
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/career", methods=["GET", "POST"])
def career():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        contact = request.form["contact"]
        position = request.form["position"]
        experience = request.form["experience"]
        date = request.form["date"]
        file1 = request.files["file1"]

        newFile = Resume(name = firstname, resume = file1.read())
        db.session.add(newFile)
        db.session.commit()
    

        # s = smtplib.SMTP('smtp.gmail.com', 587) 
        # s.starttls() 
        # s.login("", "") 
        # message = f"\n\nFirst Name:{firstname}\n\nLast Name:{lastname}\n\nEmail:{email}\n\nContact:{contact}\n\nPosition:{position}\n\nExperience:{experience}\n\ndate:{date}"
        # s.sendmail("", "", message) 
        # s.quit()
        return redirect(url_for('career'))
    return render_template("career.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        call = request.form['call']
        message = request.form['message']

        # s = smtplib.SMTP('smtp.gmail.com', 587) 
        # s.starttls() 
        # s.login("", "") 
        # message = f"\n\nName:{name}\n\nEmail:{email}\n\nContact:{phone}\n\nSubject:{subject}\n\nMessage:{message}\n\nAddress:{address}\n\nBest Time to Call:{call}"
        # s.sendmail("", "", message) 
        # s.quit()
        return redirect(url_for('contact'))
    return render_template("contact.html")

@app.route("/ongoing-projects")
def projects():
    return render_template("onprojects.html")

@app.route("/completed-projects")
def complete():
    return render_template("completedprojects.html")


if __name__ == "__main__":
    app.run(debug=True)


    