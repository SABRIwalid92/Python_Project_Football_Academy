from flask_app import app  # Import Flask to allow us to create our app

#! ALWAYS IMPORT THE CONTROLLERS HERE
# from flask_app.controllers import users_controller

from flask_app.controllers import users
from flask_app.controllers import players
from flask_app.controllers import offers

if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug= True)  # Run the app in debug mode.