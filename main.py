from logic import *


def main() -> None:
    """
    Initializes the PyQt application, sets up the UI windows, and starts the main event loop.

    This function creates instances of the login and main window UI components,
    and initializes the application logic that controls the transitions between different pages.
    It then displays the login page and starts the event loop to wait for user interaction.

    The logic class is responsible for handling the functionality and interactions between the UI components.
    """
    app = QApplication([])

    ui_login = Ui_Form_Login()
    ui_main = Ui_MainWindow()

    logic = Logic(ui_login, ui_main)

    logic.show_login()

    app.exec()


if __name__ == "__main__":
    main()
