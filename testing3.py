from pdfminer.high_level import extract_text
import flask
import tabula
import pandas as pd
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def new():

    df1 = pd.read_excel(r'C:/Users/hp/Desktop/assign1/CANNA Product Item detail.xls')

    df2 = df1.iloc[2:, :]


    df2.rename(columns={'CANNA Continental': 'Product Reference', 'Unnamed: 1': 'Product Name',
                        'Unnamed: 2': 'Product Category',  'Unnamed: 3': 'UOM', 'Unnamed: 4': 'Type',
                        'Unnamed: 5': 'Weight by unit', 'Unnamed: 6': 'Weight by cs', 'Unnamed: 7': 'Unit per cs',
                        'Unnamed: 8': 'Pieces full pallet'}, inplace=True)
    html1 = df2.to_html()



    return render_template('xlsextract.html', df=df2, )


if __name__ == '__main__':
    app.run(debug=True)
