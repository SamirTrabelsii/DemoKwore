from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    # Vous pouvez traiter les données du formulaire ici si nécessaire
    return redirect(url_for('result'))


@app.route('/result')
def result():
    return render_template('generate.html')


@app.route('/trainproduct', methods=['POST'])
def trainproduct():
    # Process form data here
    return redirect(url_for('product'))


@app.route('/product')
def product():
    return render_template('trainproduct.html')


@app.route('/trainstyle', methods=['POST'])
def trainstyle():
    # Process form data here
    return redirect(url_for('style'))


@app.route('/style')
def style():
    return render_template('trainstyle.html')


@app.route('/progressgenerate', methods=['POST'])
def progressgenerate():
    # Process form data here
    return redirect(url_for('progress'))


@app.route('/progress')
def progress():
    return render_template('progressgenerate.html')


@app.route('/generatenew', methods=['POST'])
def generatenew():
    # Vous pouvez traiter les données du formulaire ici si nécessaire
    return redirect(url_for('resultnew'))


@app.route('/resultnew')
def resultnew():
    return render_template('generatebelproduct.html')


@app.route('/generatenewnew', methods=['POST'])
def generatenewnew():
    # Vous pouvez traiter les données du formulaire ici si nécessaire
    return redirect(url_for('resultnewnew'))


@app.route('/resultnewnew')
def resultnewnew():
    return render_template('generatebelstyle.html')


@app.route('/progressgeneratebelhsan', methods=['POST'])
def progressgeneratebelhsan():
    # Process form data here
    return redirect(url_for('progressbelhsan'))


@app.route('/progressbelhsan')
def progressbelhsan():
    return render_template('progressgeneratehsan.html')


@app.route('/indexx', methods=['POST'])
def indexx():
    # Process form data here
    return redirect(url_for('final'))


@app.route('/final')
def final():
    return render_template('indexfinal.html')


if __name__ == '__main__':
    app.run(debug=True)
