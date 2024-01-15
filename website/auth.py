from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        UserName = request.form.get('UserName')
        password = request.form.get('psw')

        user = User.query.filter_by(UserName=UserName).first()
        if user:
            if check_password_hash(user.Password, password):
                flash('登陆成功!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('密码错误请重试!', category='error')
        else:
            flash('用户名不存在！', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print(request.form)
        UserName = request.form.get('UserName ')
        psw1 = request.form.get('psw1')
        psw2 = request.form.get('psw2')
        user = User.query.filter_by(UserName=UserName).first()

        # 此处的更新要在模版html中写消息事务
        if user:
            flash('已存在该用户！', category='error')
        elif psw1 != psw2:
            flash('确认密码与新密码不对称', category='error')
        else:
            new_user = User(UserName=UserName, Password=generate_password_hash(psw1, method='pbkdf2:sha256:600000', salt_length=8))
            # db提交
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
