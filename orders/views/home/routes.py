"""Routes in the blueprint home. This controls all the server functionlaity and
template rendering for the home functionality in the site. ie. screening reveiw
screening.
"""
from datetime import datetime as dt
from datetime import date
from sqlalchemy import Date, cast, and_, exc
from flask import session, render_template, Blueprint, flash, redirect, url_for, jsonify, request
from flask_login import login_required
from flask_mail import Message
from orders.extensions import secure_headers
from orders.views.home.forms import OrderForm


main = Blueprint("main", __name__)

main = Blueprint(
    "main",
    __name__,
)


@main.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@main.route("/", methods=["Get", "Post"])
@main.route("/orders", methods=["Get", "Post"])
def orders():
    form = OrderForm()
    
    form.vendor.choices = ['Ven1', 'Ven2']

    print(request.method)
    if request.method == 'POST':
        print('Need the list of products added returned here')
        print('*'*100)
        print(form.vendor.data)
        print('*'*100)

    return render_template(
        "orders.html",
        form=form,
        title="Orders",
    )

