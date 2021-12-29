# -*- coding:utf-8 -*-
# 日期：2021年12月24日


from flask import Flask, request, render_template, url_for, redirect, flash
user_name = ["ahu"]
user_pwd = ["1234"]


app = Flask(__name__)
app.secret_key = 'dklfsghls;d/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop')
def shop():
    return render_template('first.html')


@app.route('/login', methods=['POST', 'GET'])
# 登录界面
def login():
    return render_template('login.html')


@app.route('/', methods=['POST', 'GET'])
def goRegister():
    return redirect(url_for('register'))


@app.route('/register')
# 注册界面
def register():
    return render_template('register.html')


@app.route('/first', methods=['POST', 'GET'])
def getLogin():
    product_lists = [
        ("美式咖啡(冰)", "￥20.25"),
        ("浓缩咖啡(冰)", "￥22.50"),
        ("卡布奇诺(热)", "￥19.50"),
        ("拿铁(热)", "￥16.50"),
        ("红莓冰沙", "￥18.50"),
        ("菠萝冰沙", "￥16.50"),
        ("牛角包", "￥10.20"),
        ("双层安格斯MAX厚牛培根堡", "￥30.01")
    ]

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if (username not in user_name) or (password not in user_pwd):
            error = 'Invalid credentials'
            flash('username or password error')
        else:
            flash('You were successfully logged in')
            return render_template('first.html',
                                   username=username,
                                   product_lists=product_lists)
    return render_template('login.html', error=error)


@app.route('/register', methods=['POST', 'GET'])
def getRegister():
    username = request.form['username']
    password = request.form['password']
    user_name.append(username)
    user_pwd.append(password)
    return render_template('login.html')


@app.route('/list', methods=['POST', 'GET'])
def submit():
    name = request.form.get("name")
    tel = request.form.get('tel')
    add = request.form.get("add")
    lst = request.form.getlist('list')
    lst_str = "，".join(lst)
    return render_template('last.html',
                           name=name,
                           tel=tel,
                           add=add,
                           lst_name=lst_str)


@app.route('/name', methods=['POST', 'GET'])
def fullname():
    return render_template("fullname.html")


@app.route('/fullname', methods=['POST', 'GET'])
def result_name():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    full_name = firstname.title() + ' ' + lastname.title()
    return render_template("result_name.html", name=full_name)


@app.route('/word', methods=['POST', 'GET'])
def searchs():
    return render_template("search.html")


@app.route('/words', methods=['POST', 'GET'])
def result_word():
    word = request.form.get("word")
    vowels = request.form.get("vowels")
    found = {}
    for i in word:
        if i in vowels:
            found.setdefault(i, 0)
            found[i] += 1
    for j in found:
        k = j
        v = found[j]

    return render_template("result_words.html",
                           key=k,
                           value=v
                           )


@app.errorhandler(404)
# 404
def page_not_fount(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
# 500
def internal_server_error(error):
    return 'Datebase connection failed', 500


if __name__ == '__main__':
    app.run(debug=True)
