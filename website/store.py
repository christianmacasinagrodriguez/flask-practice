from flask import Flask, render_template, request, Blueprint

store = Blueprint('store', __name__)

Tinda = {
    'Milo': 10,
    'Pop-corn': 5,
}

@store.route('/')
def stor():
    return render_template("store.html", tinda=Tinda)

@store.route('/calculate')
def calcu():
    return render_template("calcu.html")
    return "10 + 12"