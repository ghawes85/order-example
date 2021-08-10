"""Routes in the blueprint home. This controls all the server functionlaity and
template rendering for the home functionality in the site. ie. screening reveiw
screening.
"""
from datetime import datetime as dt
from datetime import date
from sqlalchemy import Date, cast, and_, exc
from flask import (
    session,
    render_template,
    Blueprint,
    flash,
    redirect,
    url_for,
    jsonify,
    request,
)
from flask_login import login_required
from flask_mail import Message
#from orders.extensions import secure_headers
from orders.views.home.forms import OrderForm
from orders.model import Item, db
from orders.views.home import main

#main = Blueprint("main",__name__)

"""@main.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response"""


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@main.route("/orders/items", methods=["Post"])
def order_items():
    item = request.get_json()
    try:
        new_item = Item(
            quantity=int(item["quantity"]),
            user_id=2,
            enduser=item["enduser"],
            extra_details=item["extra_details"],
            specs=item["specs"],
            part=item["part"],
            vendor=item["vendor"],
        )
        new_item.insert()
    except Exception as e:
        print(e)
        return jsonify({"msg": "failed to add item"}), 500
    return jsonify(new_item.serialize)


@main.route("/", methods=["Get", "Post"])
@main.route("/orders", methods=["Get", "Post"])
def orders():
    form = OrderForm()
    form.vendor.choices = ["Ven1", "Ven2"]

    if request.method == "POST":
        items = Item.query.all()
        print("Need the list of products added returned here")
        for item in items:
            print(item.serialize)

        # Clear Items after Order has been created
        try:
            deleted_rows = db.session.query(Item).delete()
            db.session.commit()
            print(deleted_rows)
        except Exception as e:
            db.session.rollback()

    # Get existing items to display on table
    _orders = db.session.query(Item).all()
    return render_template(
        "orders.html",
        form=form,
        orders_ =_orders,
        title="Orders",
    )

@main.route("/orders/items/<id>", methods=["GET", "PATCH"])
def update_items(id):
    item = request.get_json()
    existing_item = db.session.query(Item).filter_by(id=id).first()

    if request.method == "PATCH":
        existing_item.quantity = int(item["quantity"]),
        existing_item.user_id = 2,
        existing_item.enduser = item["enduser"],
        existing_item.extra_details= item["extra_details"],
        existing_item.specs = item["specs"],
        existing_item.part = item["part"],
        existing_item.vendor = item["vendor"]        
        db.session.commit()

        return jsonify(existing_item.serialize)    
    return jsonify(existing_item.serialize)


@main.route("/orders/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    try:
        db.session.query(Item).filter_by(id=item_id).delete()
        db.session.commit()
    except Exception as e: 
        print(e)
        raise "something went wrong"

    return jsonify({
        "msg": "Item deleted successfully",
        "success": True
    })