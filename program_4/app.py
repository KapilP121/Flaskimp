from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dynamic content')
def dynamic(content):
    return render_template('dynamic.html', dynamic_content=content)

if __name__ == '__main__':
    app.run(host='0.0.0',port=4000)
