from flask import Flask, render_template, request
from cleaning_data import data_kredit
from prediction import prediction
from plots import RevolvingUtilizationOfUnsecuredLines,NumberOfTimes90DaysLate

# Translate flask to python object
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['RevolvingUtilizationOfUnsecuredLines'] = float(data['RevolvingUtilizationOfUnsecuredLines'])
        data['age'] = int(data['age'])
        data['NumberOfTime3059DaysPastDueNotWorse'] = int(data['NumberOfTime3059DaysPastDueNotWorse'])
        data['DebtRatio'] = float(data['DebtRatio'])
        data['MonthlyIncome_AVG'] = float(data['MonthlyIncome_AVG'])
        data['NumberOfOpenCreditLinesAndLoans'] = int(data['NumberOfOpenCreditLinesAndLoans'])
        data['NumberOfTimes90DaysLate'] = int(data['NumberOfTimes90DaysLate'])
        data['NumberRealEstateLoansOrLines'] = int(data['NumberRealEstateLoansOrLines'])
        data['NumberOfTime60-89DaysPastDueNotWorse'] = int(data['NumberOfTime60-89DaysPastDueNotWorse'])
        data['NumberOfDependents_MV'] = int(data['NumberOfDependents_MV'])

        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=hasil)

    return render_template('prediction.html')

@app.route('/data')
def data():
    data = data_kredit()
    data = data.head(20)
    return render_template('tabel_data.html', data=data)

# Untuk proses panggil template dari masing-masing html 
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/plots')
def plots():
    data= RevolvingUtilizationOfUnsecuredLines()
    data2 = NumberOfTimes90DaysLate()
    return render_template('plots.html',data=data, data2=data2)


if __name__ =='__main__':
    app.run(debug=True, port=28105)