from flask import Flask, render_template, url_for
from flask_wtf.csrf import CSRFProtect



import datetime
app = Flask(__name__)

csrf=CSRFProtect(app)

csrf.init_app(app)


@app.route('/')
def weissnotary():
    return render_template("index.html")




@app.route("/liked")
def siteLiked():
  day=str(datetime.datetime.now().day)
  month=str(datetime.datetime.now().month)
  year=str(datetime.datetime.now().year)
  date=month+"/"+day+"/"+year

  filename="CustOpin.txt"
  outfile=open(filename, "a")
  outfile.write("YES\t"+date)
  outfile.write("\n")
  outfile.close()
  return render_template("thankyou.html")



@app.route("/disliked")
def siteDisliked():
  day=str(datetime.datetime.now().day)
  month=str(datetime.datetime.now().month)
  year=str(datetime.datetime.now().year)
  date=month+"/"+day+"/"+year

  filename="CustOpin.txt"
  outfile=open(filename, "a")
  outfile.write("NO\t"+date)
  outfile.write("\n")
  outfile.close()
  return render_template("thankyou.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
