from flask import Flask, render_template, request

import write
import artist

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        intad = request.form['artname']
        intinv= request.form['invamt']
        pop_score = artist.search(intad)
        result = write.store(intad)
        details = write.detail(result)
        picurl = 'https://www.accessrx.com/blog/wp-content/uploads/2015/10/skeptical-man.jpg'

        if result:
            return render_template('results.html',intad=intad, result=result, details = details, picurl=picurl, pop_score=pop_score, intinv = intinv)
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=None)



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = name.upper()
    return render_template('hello.html', name=name)



if __name__ == '__main__':
    app.run()