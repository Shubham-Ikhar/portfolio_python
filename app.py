from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # print(data)
            write_data_csv(data)
            message = 'Thank you for submitting the form we will get in touch to you..!!'
            return render_template('thankyou.html', message= message)
        except:
            message = 'Did not save data to database..!'
            return render_template('thankyou.html', message= message)
    else:
        message = 'Form not submitted..!'
        return render_template('thankyou.html', message=message)

@app.route("/<string:page_name>")
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')


def write_data_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    # with open('database.txt', 'a') as f:
    #     f.write("email: {}, subject: {}, message: {}".format(email,subject,message))

    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])
#         start db.csv in terminal to show the file in excel format


if __name__ == "__main__":
    app.run(debug=True)



#to create the module txt file , just type
#pip freeze > filename.txt in console and press enter