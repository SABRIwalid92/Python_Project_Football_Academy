from flask_app import app
from flask import request ,render_template, session, redirect
from flask_app.models.offer import Offer

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/offers/new')
def new():
    if 'trainer_id' in session:
        return render_template('new.html')
    return redirect('/')

@app.route('/offers/create', methods=['post'])
def create():
    # if not Offer.validation(request.form):
    #     return redirect('/offers/new')

    data = {**request.form, "trainer_id": int(session["trainer_id"])}
    db_return = Offer.create(data)
    print(db_return)
    return redirect('/dashboard')

@app.route('/offers/<int:id>')
def one(id):
    if 'trainer_id' in session:
        offer = Offer.get_by_id({'id' : id})
        # trainer = Trainer.get_by_id({'id':session['trainer_id']})
        return render_template('/view.html', offer=offer)
    return redirect('/')

@app.route('/offers/edit/<int:id>')
def edit(id):
    session["offer_id"]=id
    offer = Offer.get_by_id({'id' : id})
    return render_template('/edit.html', offer=offer)

@app.route('/offers/update', methods=['post'])
def update():
    # if not Offer.validation(request.form):
    #     return redirect(f'/offers/edit/{ session["offer_id"]}')
    data ={
        **request.form, 'id':session["offer_id"]
    }
    Offer.edit(data)
    return redirect('/dashboard')
    

@app.route('/offers/<int:id>/destroy')
def delete(id):
    if 'trainer_id' in session:
        Offer.delete({'id' : id})
        return redirect('/dashboard')
    return redirect('/')