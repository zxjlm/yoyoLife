'''
    @author: harumonia
    :@url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :@site: 
    :@datetime: 2020/6/21 14:08
    :@software: PyCharm
    :@description: None
'''
from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required

from application.extensions import db
from application.models import Bills
from datetime import datetime

from application.models.Bills import ConsumptionTypeDict

bill_bp = Blueprint('bill', __name__)


@bill_bp.route('/bill')
@login_required
def init():
    if len(current_user.bills) == 0:
        flag = False
    else:
        flag = True
    consumption_type = ConsumptionTypeDict.query.all()
    return render_template('bill.html', flag=flag, bills=[bill.to_json() for bill in current_user.bills],
                           consumption_type=[foo.consumption_type for foo in consumption_type])


@bill_bp.route('/bill/new', methods=['POST'])
@login_required
def new_bill():
    data = request.get_json()
    if data is None or data['body'].strip() == '':
        return jsonify(message='Invalid Bill body.'), 400
    try:
        payfor, money, type_, date = data['body'], data['money'], data['type'], data['date'].replace('T', ' ').replace(
            ".000Z", '')
        type_l = ConsumptionTypeDict.query.filter(ConsumptionTypeDict.consumption_type == type_).all()
        if ConsumptionTypeDict:
            bill = Bills(payfor=payfor, money=float(money), consumption_type_id=type_l[0].id, datetime=date,
                         author=current_user._get_current_object())
        else:
            bill = Bills(payfor=payfor, money=float(money), consumption_type_id=-1, datetime=date,
                         author=current_user._get_current_object(), mark=type_)
        db.session.add(bill)
        db.session.commit()
    except Exception:
        return jsonify(message='Invalid Bill body.'), 400
    return jsonify(html=render_template('_bill.html', bill=bill.to_json()), message='+1')


@bill_bp.route('/bill/edit', methods=['POST'])
@login_required
def edit_bill():
    data = request.get_json()

    bill = Bills.query.get_or_404(data['id'])
    if current_user != bill.author:
        return jsonify(message='Permission denied.'), 403

    if data is None or data['body'].strip() == '':
        return jsonify(message='Invalid bill body.'), 400
    try:
        payfor, money, type_, date = data['body'], data['money'], data['type'], data['date'].replace('T', ' ').replace(
            ".000Z", '')
        type_l = ConsumptionTypeDict.query.filter(ConsumptionTypeDict.consumption_type == type_).all()
        if type_l:
            bill.payfor, bill.money, bill.consumption_type_id, bill.date = payfor, money, type_l[0].id, date
        else:
            bill.payfor, bill.money, bill.consumption_type_id, bill.date = payfor, money, -1, date
        db.session.add(bill)
        db.session.commit()
    except Exception:
        return jsonify(message='Invalid bill body.'), 400
    return jsonify(message='Bill updated.')


@bill_bp.route('/bill/delete/<string:bill_id>', methods=['DELETE'])
@login_required
def delete_bill(bill_id):
    bill = Bills.query.get_or_404(bill_id)
    if current_user != bill.author:
        return jsonify(message='Permission denied.'), 403

    db.session.delete(bill)
    db.session.commit()
    return jsonify(message='Bill deleted.')
