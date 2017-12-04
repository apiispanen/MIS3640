from flask import Flask, render_template, request

import write
#'write' writes the results into a .txt file
import artist
#this is the main artist searcher, through Spotify
import imagesearch
#this was an added extra, going into Pixabay and retrieving the top result to give an image of the artist or a related picture!


app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"

'''
App Processes popularity data through the Spotify API and updates data based on initial investment at a certain popularity value. 

'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        intad = request.form['artname']
        intinv= request.form['invamt']
        pop_score = artist.search(intad)
        result = write.store(intad, intinv)
        details = write.detail(result)
        picurl = imagesearch.get_image(intad)

        if result:
            return render_template('results.html',intad=intad, result=result, details = details, picurl=picurl, pop_score=pop_score, intinv = intinv)
        else:
            return render_template('hello.html', error=True)
    return render_template('hello.html', error=None)

'''
Beta Code for testing

'''

@app.route('/results/')
@app.route('/results/<name>')
def hello(name=None):
    if name:
        name = name.upper()
        pop_score = artist.search(name)
        result = write.store(name, intinv)
        details = write.detail(result)
        picurl = imagesearch.get_image(name)
        return render_template('results.html', name=name, pop_score = pop_score, intad=name, result=result, details = details, picurl=picurl, intinv = 0)
    else:
        return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()