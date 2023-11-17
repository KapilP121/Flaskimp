from flask import Flask, session
app = Flask(__name__)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        
        for key, value in request.form.items():
            print(f'{key}: {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)

        
            session['stock_symbol'] = stock_data.stock_symbol          
            session['number_of_shares'] = stock_data.number_of_shares  
            session['purchase_price'] = stock_data.purchase_price      
        except ValidationError as e:
            print(e)

    return render_template('add_stock.html')

    @app.route('/stocks/')
    def list_stocks():
    return render_template('stocks.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000)