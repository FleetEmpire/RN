from flask import Flask, render_template, request, flash, redirect, url_for
import RnCore as rc

rn = Flask(__name__)

def get_results(start, end):
    RCore = rc.RandomNumberCore(start, end)
    results = RCore.random_number_fast()
    return results

@rn.route("/", methods=["GET", "POST"])
def index():
    
    """
    The index Page method

    Returns:
        Response
    """

    if request.method == "POST":
        global results, start1, end1
        start = request.form['start']
        end = request.form['end']
        
        try:
            start1 = int(str(start))
            end1 = int(str(end))
            
        except ValueError:
            flash("Invalid input.")
            return redirect(url_for("index"))
        
        else:
            results = get_results(start=start1, end=end1)
            return redirect(url_for("result"))
          
    return render_template("index.html")


@rn.route("/results", methods=["GET", "POST"])
def result():

    """
        The result Page

        Returns:
            Response
    """
    if request.method == "POST":
        if request.form.get('again') != None:
            global results
            results = get_results(start=start1, end=end1)
            return redirect(url_for("result"))
        
        elif request.form.get('return') != None:
            return redirect(url_for("index"))
    
    return render_template("results.html", results = results)

@rn.route("/fuck")
def fuck():
    return '<h1>傻逼政治！</h1>'

if __name__=="__main__":
    rn.run(port=5000,host="127.0.0.1",debug=False)