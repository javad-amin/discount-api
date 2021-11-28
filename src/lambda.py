from api.app import create_app
from database.some_database.some_database import SomeDatabase

database_layer = SomeDatabase()

app = create_app(database_layer)

# We can imagine this is a lambda function and the app is injected to it
if __name__ == "__main__":
    app.run(debug=True)
