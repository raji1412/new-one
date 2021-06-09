from flask import Flask,render_template,request
import smtplib
my_email = "rajithasample@gmail.com"
password="Sample*2000"
app=Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    message = "Contact Me!!"
    return render_template("contact.html",message=message)


@app.route("/contact",methods=["POST"])
def rec_data():
    message="Successfully sent!!"
    name=request.form["name"]
    email=request.form["email"]
    number=request.form["phone"]
    mess_age=request.form["mess"]
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs="rajithalakshmi2000@gmail.com",
            msg=f"Subject:Message form a customer!! \n\n Name: {name}"
                f"\n Email : {email}\n Phone number : {number}"
                f"\n Message : {mess_age}"
        )
    return render_template("contact.html",message=message)

if __name__ == "__main__":
    app.run(debug=True)
