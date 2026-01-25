from ui.app import App
from database.db import init_db

if __name__ == "__main__":
    init_db()
    app = App()
    app.mainloop()
