from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import String,Column, Integer
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(150))
    Password = db.Column(db.String(150))
    notes = db.relationship('Note')



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cName = db.Column(db.String(150))     # 客户名
    cOrderId = db.Column(db.String(150))  # 客户订单号
    cOrderDate = db.Column(db.DateTime(timezone=True))
    cDeliveryDate = db.Column(db.DateTime(timezone=True))
    pName = db.Column(db.String(150))
    pMaterial = db.Column(db.String(150))
    pSize = db.Column(db.String(150))
    pQuantity = db.Column(db.Integer)
    uPrice = db.Column(db.Integer)       # 单价
    # 白板纸
    surfaceId = db.Column(db.String(150))
    surfaceSize = db.Column(db.String(150))
    surfaceQuantity = db.Column(db.Integer)
    surfaceStage = db.Column(db.String(150))
    # 坑纸
    backId = db.Column(db.String(150))
    backSize = db.Column(db.String(150))
    backQuantity = db.Column(db.Integer)
    backStage = db.Column(db.String(150))
    # 啤板
    plateId = db.Column(db.String(150))
    plateStage = db.Column(db.String(150))
    # 文件
    docId = db.Column(db.String(150))
    docStage = db.Column(db.String(150))
    # 生产进度
    produceStage = db.Column(db.String(150))
    # 送货进度
    deliveryStage = db.Column(db.String(150))
    # 订单进度
    orderStage = db.Column(db.String(150))


    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))