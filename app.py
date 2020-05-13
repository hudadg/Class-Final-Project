from flask import Flask, render_template, request
from cleaning_data import data_kredit
from prediction import prediction

# Translate flask to python object
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['Rooms'] = int(data['Rooms'])
        data['Bathrooms'] = int(data['Bathrooms'])
        data['Size'] = int(data['Size'])
        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=hasil)

    return render_template('prediction.html', data_location=sorted(locations),data_property=sorted(property_type))

@app.route('/data')
def data():
    data = data_mobil()
    return render_template('tabel_data.html', data=data)

# Untuk proses panggil template dari masing-masing html 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/plots')
def plots():
    data= mpg()
    data2 = horsepower()
    return render_template('plots.html',data=data, data2=data2)


if __name__ =='__main__':
    app.run(debug=True, port=28105)