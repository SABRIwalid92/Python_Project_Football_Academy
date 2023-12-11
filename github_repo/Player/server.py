from flask_app import app

#                ================ ADD CONTROLLERS ===========================
# >>>>>>>>>>>>>>        from flask_app.controllers import controller.py     <<<<<<<<<<<<<<<<<


from flask_app.controllers import players


if __name__ == "__main__":
    app.run(debug=True,port=5002)
