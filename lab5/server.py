from flask import Flask, render_template, request, redirect, url_for
from mongo import Mongo

app = Flask(__name__)

mongo = Mongo()

@app.route("/", methods=['post', 'get'])
def table_display():

    if request.method == 'POST':
        command = request.form.get('command')
        message = mongo.execute(command)
        if message:
            return render_template("response.html", command = command, message = message)
        else:
            return redirect(url_for('table_display'))

    table_list = mongo.get_tables()
    data = {}
    for table in table_list:

        table_data = mongo.get_table_data(table)
        data.update({table: table_data})

    return render_template("main.html", data=data)


app.run()
