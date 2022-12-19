from flask import Flask, request, render_template, redirect
import pandas as pd
import crawler

app = Flask(__name__)


@app.route("/")
def hello():
    item = request.args.get('item')

    if not item:
        return render_template("none.html",
                               item='',
                               d=[],
                               )

    print(f'item => {item}')

    d1 = crawler.yahoo(item)
    d2 = crawler.momo(item)
    d3 = crawler.pchome(item)

    df = pd.concat([d1, d2, d3])

    return render_template("test_1.html",
                           item=item,
                           d=df.to_dict(orient='records'),
                           )



if __name__ == "__main__":
    app.run()