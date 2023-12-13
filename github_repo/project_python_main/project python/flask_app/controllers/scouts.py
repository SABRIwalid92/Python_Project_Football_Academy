from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models import Scout
from flask_app.models.user import User

@app.route('/scouts/new')
def scout_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('scouts_dashboard.html')



# @app.route('/scouts/create', methods=['post'])
# def create_recipe():
#     if (scout.validate_scout(request.form)):
#         data = {
#             **request.form, 'user_id':session['user_id']
#         }
#         scout.save_recipe(data)
#         return redirect('/scouts')
#     return redirect('/scouts')

@app.route('/scouts/show/<int:scout_id>')
def show_scout(scout_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    scout=scout.get_by_id_scout({'id':scout_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('show_offers.html',scout=scout,user=user)

# @app.route('/scouts/edit/<int:scouts_id>')
# def edit_scout(scout_id):
#     if 'user_id' not in session:
#         return redirect('/')
#     scout= scout.get_by_id_scout({'id': recipe_id})
#     session['recipe_id']= scout_id
#     return render_template('edit_scout.html',recipe=recipe)

# @app.route('/scouts/edit', methods=['post'])
# def edit():
#     scout_data= {
#         **request.form,
#         'id': session['scout_id']
#     }
#     scout.update_scout(scout_data)
#     return redirect('/scouts')

# @app.route('/scouts/delete/<int:scout_id>')
# def delete(scout_id):
#     scout.delete_scout({'id':scout_id})
#     return redirect('/scouts')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')