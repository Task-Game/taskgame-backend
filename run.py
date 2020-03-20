from app import create_app

config = {
    "development":"config.Development"
}
app = create_app()
if __name__ == "__main__":
    app.run()