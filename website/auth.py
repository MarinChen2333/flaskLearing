from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # 请求表单(控制台可看)
    data = request.form
    print(data)
    # 注意此处变量使用
    return render_template("login.html", text="hi!", user="CH")


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/sign-in')
def sign_in():
    return "<h1>sign in</h1>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method=='post':
        UserName = request.form.get('UserName')
        Password1 = request.form.get('psw1')
        Password2 = request.form.get('psw2')

        # 此处的更新要在模版html中写消息事务
        if Password1 != Password2:
            flash('Password don\'t match.',category='error')
        else:
            flash('Account created', category='success')

    return render_template("sign_up.html")
