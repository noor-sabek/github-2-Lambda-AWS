#import pandas as pd

# def lambda_handler(event, context):
    #d = {'col1': [1,2], 'col2': [3,4], 'col3':[5,6]}
  #  df = pd.DataFrame(data=d)
   # print(df)
   # print('Done x1.2')
 
 
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
