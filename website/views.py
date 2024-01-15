from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Order
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/newOrder', methods=['GET', 'POST'])
@login_required
def newOrder():
    if request.method == 'POST':
        cname = request.form.get('cName')
        corderId = request.form.get('cOrderId')
        orderDate = request.form.get('cOrderDate')
        deliveryDate = request.form.get('cDeliveryDate')
        pname = request.form.get('pName')
        material = request.form.get('material')
        size = request.form.get('size')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        # 白板纸
        surfaceId = request.form.get('surface-id')
        surfaceSize = request.form.get('surface-size')
        surfaceQuantity = request.form.get('surface-quantity')
        surfaceStage = request.form.get('surface-stage')
        # 坑纸
        backId = request.form.get('back-id')
        backSize = request.form.get('back-size')
        backQuantity = request.form.get('back-quantity')
        backStage = request.form.get('back-stage')
        # 啤板
        plateId = request.form.get('plate-id')
        plateStage = request.form.get('plate-stage')
        # 文件
        docId = request.form.get('doc-id')
        docStage = request.form.get('doc-stage')
        # 生产进度
        produceStage = request.form.get('produce-stage')
        # 送货进度
        deliveryStage = request.form.get('delivery-stage')
        # 订单进度
        orderStage = request.form.get('order-stage')

        new_Order = Order(cName=cname, cOrderId=corderId,
                          cOrderDate=datetime.strptime(orderDate, "%Y-%m-%d"),
                          cDeliveryDate=datetime.strptime(deliveryDate, "%Y-%m-%d"),
                          pName=pname, pMaterial=material, pSize=size, pQuantity=quantity, uPrice=price,
                          surfaceId=surfaceId, surfaceSize=surfaceSize, surfaceQuantity=surfaceQuantity,
                          surfaceStage=surfaceStage,
                          backId=backId, backSize=backSize, backQuantity=backQuantity, backStage=backStage,
                          plateId=plateId, plateStage=plateStage, docId=docId, docStage=docStage,
                          produceStage=produceStage, deliveryStage=deliveryStage, orderStage=orderStage,
                          user_id=current_user.id)

        db.session.add(new_Order)
        db.session.commit()

        flash('New Order added', category='success')
    return render_template('newOrder.html', user=current_user)


@views.route('/listOrder', methods=['GET', 'POST'])
@login_required
def listOrder():
    if request.method == 'GET':
       newOrder
    return render_template("listOrder.html", user=current_user,)


@views.errorhandler(404)
def page_not_found(error):
    return render_template('home.html')

@views.errorhandler(500)
def serverError(error):
    return render_template('home.html')
