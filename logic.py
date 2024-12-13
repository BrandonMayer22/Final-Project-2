from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtCore import *
from PyQt6.QtGui import QMouseEvent, QStandardItem, QStandardItemModel, QPixmap
from gui import *
from typing import *
import csv, re


class Logic:
    """
    Handles the application logic, including page transitions, user interactions,
    and background functionality for login, signup, and user settings.
    """

    def __init__(
        self,
        ui_login: Ui_Form_Login,
        ui_main: Ui_MainWindow,
    ) -> None:
        """
        Initializes the Logic class with UI components and window objects.

        Args:
            ui_login (Ui_Form_Login): Login window UI.
            ui_main (Ui_MainWindow): Main page UI.
        """
        self.html_file_path = "Splash.html"
        self.app_version = "v1.0.0"
        
        self.ui_login = ui_login
        self.ui_main = ui_main
        self.current_window: QWidget | None = None
        self.window_login = QWidget()
        self.window_main = QMainWindow()

        self.current_filter = ""
        self.email = ""

        self.ui_login.setupUi(self.window_login)
        self.ui_main.setupUi(self.window_main)

        self.setup_connections()

        self.filter_proxy_model = QSortFilterProxyModel(self.ui_main.tableView)
        self.filter_proxy_model.setSourceModel(
            QStandardItemModel(self.ui_main.tableView)
        )
        self.filter_proxy_model.setFilterRole(Qt.ItemDataRole.DisplayRole)
        self.ui_main.tableView.setModel(self.filter_proxy_model)

        self.window_login.mousePressEvent = self.mousePressEvent
        self.window_login.mouseMoveEvent = self.mouseMoveEvent
        self.window_login.mouseReleaseEvent = self.mouseReleaseEvent

        self.ui_main.pushButton_Top_Menu_Carrot.setText("⏷")
        self.ui_main.pushButton_Side_Menu_Carrot.setText("⏴")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse press event for window dragging.

        Args:
            event (QMouseEvent): The mouse event that triggered this method.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = True
            if hasattr(self, "current_window") and self.current_window:
                self.drag_start_position = (
                    event.globalPosition().toPoint()
                    - self.current_window.frameGeometry().topLeft()
                )
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse move event for window dragging.

        Args:
            event (QMouseEvent): The mouse event that triggered this method.
        """
        if self.is_dragging and event.buttons() == Qt.MouseButton.LeftButton:
            # Ensure the current window is set, and perform the move operation
            if hasattr(self, "current_window") and self.current_window:
                self.current_window.move(
                    event.globalPosition().toPoint() - self.drag_start_position
                )
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handles the mouse release event for stopping window dragging.

        Args:
            event (QMouseEvent): The mouse event that triggered this method.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            event.accept()

    def setup_connections(self) -> None:
        """
        Connects all relevant signals and slots to their respective functions.
        """
        print("Setting up connections...")
        self.ui_login.pushButton_SU_Exit.clicked.connect(self.signup_exit)
        self.ui_login.pushButton_SU_Signup.clicked.connect(self.complete_signup)
        # self.ui_login.pushButton_SM1.clicked.connect(self.)
        # self.ui_login.pushButton_SM2.clicked.connect(self.)
        # self.ui_login.pushButton_SM3.clicked.connect(self.)
        # self.ui_login.pushButton_SM4.clicked.connect(self.)
        self.ui_login.pushButton_Login.clicked.connect(self.validate_login)
        self.ui_login.pushButton_Signup.clicked.connect(self.signup_clicked)

        self.ui_main.pushButton_Logo1.clicked.connect(self.logo1_clicked)
        # self.ui_main.pushButton_Logo2.clicked.connect(self.)
        # self.ui_main.pushButton_Logo3.clicked.connect(self.)
        # self.ui_main.pushButton_Logo4.clicked.connect(self.)
        self.ui_main.pushButton_Side_Menu_Carrot.clicked.connect(
            self.side_carrot_clicked
        )
        self.ui_main.pushButton_Top_Menu_Carrot.clicked.connect(self.top_carrot_clicked)
        self.ui_main.pushButton_Help.clicked.connect(self.display_help)
        self.ui_main.pushButton_Privacy.clicked.connect(self.display_privacy)
        self.ui_main.pushButton_Terms.clicked.connect(self.display_terms)
        self.ui_main.pushButton_Exit.clicked.connect(self.exit_app)
        self.ui_main.pushButton_Maximize.clicked.connect(self.maximize_app)
        self.ui_main.pushButton_Menu.clicked.connect(self.menu_app)
        self.ui_main.pushButton_Minimize.clicked.connect(self.minimize_app)
        self.ui_main.pushButton_Account.clicked.connect(self.display_account)
        self.ui_main.pushButton_Home.clicked.connect(self.display_home)
        self.ui_main.pushButton_Settings.clicked.connect(self.display_settings)
        self.ui_main.pushButton_clear.clicked.connect(self.clear_filter)
        self.ui_main.pushButton_chg_pass.clicked.connect(self.change_password)
        self.ui_main.pushButton_chg_submit.clicked.connect(self.submit_changes)
        self.ui_main.pushButton_prof_update.clicked.connect(self.update_profile)

        self.ui_main.checkBox_Legends.toggled.connect(self.cb_toggle_uni)
        self.ui_main.checkBox_Canon.toggled.connect(self.cb_toggle_uni)
        self.ui_main.checkBox_GB.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_JRA.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_NA.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_OJR.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_ON.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_S.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_YA.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_YR.toggled.connect(self.cb_toggle_novel)
        self.ui_main.checkBox_AOR.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_DOTJ.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_FOTJ.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_NJO.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_ROTE.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_ROTFO.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_THR.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_TNR.toggled.connect(self.cb_toggle_era)
        self.ui_main.checkBox_TOR.toggled.connect(self.cb_toggle_era)

    def show_login(self) -> None:
        """Displays the login page."""

        print("Setting up login page...")
        self.current_window = self.window_login
        self.window_login.show()

    def show_main(self) -> None:
        """
        Displays the main page and loads the splash page.

        Raises:
            FileNotFoundError: If the HTML file is not found.
            Exception: For any other errors loading the HTML file.
        """
        print("Setting up main page...")
        self.current_window = self.window_main
        print(
            f"Current window: {self.current_window.__class__.__name__ if self.current_window else 'None'}"
        )
        
        self.window_main.show()

        self.load_text_browser()
        print("Splash page loaded successfully.")
        print(f"Current html file: {self.html_file_path}")
        print(f"text browser visibility: {self.ui_main.textBrowser.isVisible()}")

    def read_csv(self, file_path: str) -> list[dict]:
        """
        Reads a CSV file and returns its rows as a list of dictionaries.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list[dict]: A list of dictionaries representing the rows in the CSV.

        Raises:
            FileNotFoundError: If the CSV file is not found.
            Exception: For any other errors reading the file.
        """
        try:
            with open(file_path, mode="r") as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' not found.")
        except Exception as e:
            raise Exception(f"Error reading file '{file_path}': {e}")

    def write_csv(self, file_path: str, data: list[str]) -> None:
        """
        Writes a row of data to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            data (list[str]): The data to write as a row in the CSV file.

        Raises:
            Exception: If there is an error writing to the file.
        """
        try:
            with open(file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
        except Exception as e:
            raise Exception(f"Error writing to file '{file_path}': {e}")

    def validate_login(self) -> None:
        """
        Validates user login credentials by checking them against a CSV file.

        Raises:
            FileNotFoundError: If the login credentials file is missing.
            Exception: For any other errors during the validation process.
        """
        self.email = self.ui_login.lineEdit_Email.text().strip()
        password = self.ui_login.lineEdit_Pass.text().strip()
        

        try:
            reader = self.read_csv("login_credentials.csv")
            for row in reader:
                if row["email"] == self.email:
                    if row["password"] == password:
                        print(
                            f"Current window: {self.current_window.__class__.__name__ if self.current_window else 'None'}"
                        )

                        first_name = row.get("first", "")  # Default to "Unknown" if not found
                        last_name = row.get("last", "") 
                        address = row.get("address", "")
                        state = row.get("state", "")
                        city = row.get("city", "")
                        zipcode = row.get("zip", "")
                        gender = row.get("gender", "")
                        dob = row.get("birthday", "") 
                        self.ui_main.label_Footer_Text_Center.setText(f"App Version: {self.app_version} | User: {first_name} {last_name}")
                        # Close the current window if it's the login window
                        if self.current_window == self.window_login:
                            print("Closing the login window...")
                            self.window_login.close()

                        # Update current window and show the main window
                        self.show_main()
                        self.ui_login.label_MainWarning.setVisible(False)
                        self.ui_login.lineEdit_Pass.clear()
                        self.ui_login.lineEdit_Email.clear()
                        self.ui_login.lineEdit_Email.setFocus()
                        self.ui_main.label_prof_first_name.setText(first_name)
                        self.ui_main.label_prof_last_name.setText(last_name)
                        self.ui_main.label_prof_email.setText(self.email)
                        self.ui_main.lineEdit_prof_address.setText(address)
                        self.ui_main.comboBox_state.setCurrentText(state)
                        self.ui_main.lineEdit_city.setText(city)
                        self.ui_main.lineEdit_prof_zip.setText(zipcode)
                        self.ui_main.comboBox_gender.setCurrentText(gender)
                        self.ui_main.dateEdit_dob.setDate(QDate.fromString(dob, "MMMM dd yyyy"))
                        
                        return
                    else:
                        self.ui_login.label_MainWarning.setText(
                            "Incorrect password entered"
                        )
                        self.ui_login.label_MainWarning.setVisible(True)
                        return

            self.ui_login.label_MainWarning.setText("Email not registered")
            self.ui_login.label_MainWarning.setVisible(True)
        except FileNotFoundError:
            self.ui_login.label_MainWarning.setText(
                "Login credentials file is missing."
            )
            self.ui_login.label_MainWarning.setVisible(True)
        except Exception as e:
            self.ui_login.label_MainWarning.setText(f"An error occurred: {e}")
            self.ui_login.label_MainWarning.setVisible(True)
            print(f"Error validating login: {e}")

    def signup_exit(self) -> None:
        """Exits the signup window and clears all form fields."""
        self.ui_login.frame_Signup.setVisible(False)
        self.ui_login.lineEdit_First.clear()
        self.ui_login.lineEdit_Last.clear()
        self.ui_login.lineEdit_SU_Email.clear()
        self.ui_login.lineEdit_SU_Pass.clear()
        self.ui_login.lineEdit_SU_Pass_Conf.clear()
        self.ui_login.comboBox_Day.setCurrentIndex(0)
        self.ui_login.comboBox_Month.setCurrentIndex(0)
        self.ui_login.comboBox_Year.setCurrentIndex(0)
        self.ui_login.radioButton_Female.setChecked(False)
        self.ui_login.radioButton_Male.setChecked(False)
        self.ui_login.radioButton_Custom.setChecked(False)
        self.ui_login.label_Warning.clear()

    def complete_signup(self) -> None:
        """Completes the signup process by validating and storing the user's credentials."""
        first_name = self.ui_login.lineEdit_First.text().strip()
        last_name = self.ui_login.lineEdit_Last.text().strip()
        email = self.ui_login.lineEdit_SU_Email.text().strip()
        password = self.ui_login.lineEdit_SU_Pass.text().strip()
        confirm_password = self.ui_login.lineEdit_SU_Pass_Conf.text().strip()
        day = self.ui_login.comboBox_Day.currentText()
        month = self.ui_login.comboBox_Month.currentText()
        year = self.ui_login.comboBox_Year.currentText()

        if self.ui_login.radioButton_Female.isChecked():  # Determine gender
            gender = "Female"
        elif self.ui_login.radioButton_Male.isChecked():
            gender = "Male"
        elif self.ui_login.radioButton_Custom.isChecked():
            gender = "Custom"
        else:
            gender = None

        birthday = f"{month} {day} {year}"  # Combine birthday into desired format

        # Check for duplicate email
        if not (
            first_name
            and last_name
            and email
            and password
            and confirm_password
            and gender
        ):
            self.ui_login.label_Warning.setText("All fields must be filled out.")
            self.ui_login.label_Warning.setVisible(True)
            return

        if password != confirm_password:
            self.ui_login.label_Warning.setText("Passwords do not match.")
            self.ui_login.label_Warning.setVisible(True)
            return

        valid_domains = [
            "@gmail.com",
            "@yahoo.com",
            "@outlook.com",
            "@hotmail.com",
            "@icloud.com",
            "@aol.com",
            "@msn.com",
            "@live.com",
            "@mail.com",
            "@protonmail.com",
            "@zoho.com",
            "@yandex.com",
            "@gmx.com",
            "@comcast.net",
            "@sbcglobal.net",
            "@verizon.net",
            "@bellsouth.net",
            "@charter.net",
            "@att.net",
            "@cox.net",
            "@fastmail.com",
            "@inbox.com",
            "@me.com",
            "@hushmail.com",
            "@tutanota.com",
            "@webmail.co.za",
            "@seznam.cz",
            "@mail.ru",
            "@outlook.co.uk",
            "@gmx.net",
            "@unomaha.edu",
        ]
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Basic email format validation

        if not re.match(email_regex, email):
            self.ui_login.label_Warning.setText("Invalid email format.")
            self.ui_login.label_Warning.setVisible(True)
            return

        if not any(email.endswith(domain) for domain in valid_domains):
            self.ui_login.label_Warning.setText(
                "Email must use a valid domain (e.g., @gmail.com)."
            )
            self.ui_login.label_Warning.setVisible(True)
            return

        try:
            existing_users = self.read_csv("login_credentials.csv")
            for user in existing_users:
                if user["email"] == email:
                    self.ui_login.label_Warning.setText("Email is already in use.")
                    self.ui_login.label_Warning.setVisible(True)
                    return
        except FileNotFoundError:
            existing_users = []

        try:
            self.write_csv(
                "login_credentials.csv",
                [email, password, first_name, last_name, birthday, gender],
            )
            self.ui_login.label_Warning.setText(
                "Signup successful! You can now log in."
            )
            self.ui_login.label_Warning.setStyleSheet("color: green;")
            self.ui_login.label_Warning.setVisible(True)

            self.ui_login.frame_Signup.setVisible(False)
            self.ui_login.lineEdit_First.clear()
            self.ui_login.lineEdit_Last.clear()
            self.ui_login.lineEdit_SU_Email.clear()
            self.ui_login.lineEdit_SU_Pass.clear()
            self.ui_login.lineEdit_SU_Pass_Conf.clear()
            self.ui_login.comboBox_Day.setCurrentIndex(0)
            self.ui_login.comboBox_Month.setCurrentIndex(0)
            self.ui_login.comboBox_Year.setCurrentIndex(0)
            self.ui_login.radioButton_Female.setChecked(False)
            self.ui_login.radioButton_Male.setChecked(False)
            self.ui_login.radioButton_Custom.setChecked(False)
            self.ui_login.label_Warning.clear()

        except Exception as e:
            self.ui_login.label_Warning.setText(f"An error occurred: {e}")
            self.ui_login.label_Warning.setVisible(True)

    def signup_clicked(self) -> None:
        """Displays the signup page."""
        self.ui_login.frame_Signup.setVisible(True)

    def load_table(self) -> None:
        """Loads the table with data from a CSV file and displays it."""
        if self.ui_main.textBrowser.isVisible():
            self.ui_main.tableView.setVisible(False)
        self.ui_main.tableView.setVisible(True)
        model = QStandardItemModel(self.ui_main.tableView)
        self.ui_main.tableView.setModel(model)

        try:
            data = self.read_csv("SWTable.csv")

            if not data:
                print("CSV file is empty.")
                return

            headers = list(data[0].keys())
            model.setHorizontalHeaderLabels(headers)

            thumbnail_paths = []

            for row_data in data:
                row_items = []
                for column, value in row_data.items():
                    if column.lower() == "thumbnail":
                        thumbnail_paths.append(value)
                        item = QStandardItem("Loading...")
                    else:
                        item = QStandardItem(str(value))
                    row_items.append(item)
                model.appendRow(row_items)

            self.filter_proxy_model.setSourceModel(model)
            self.ui_main.tableView.setModel(self.filter_proxy_model)

            self.ui_main.tableView.verticalHeader().setDefaultSectionSize(150)
            self.ui_main.tableView.hideColumn(1)
            self.ui_main.tableView.hideColumn(8)
            self.ui_main.tableView.setColumnWidth(2, 50)
            self.ui_main.tableView.setColumnWidth(4, 300)
            self.ui_main.tableView.setColumnWidth(7, 150)

            self.image_loader_thread = ImageLoaderThread(thumbnail_paths)
            self.image_loader_thread.image_loaded.connect(self.update_image)
            self.image_loader_thread.start()

        except Exception as e:
            print(f"Error loading table: {e}")

    def update_image(self, row_index: int, pixmap: QPixmap) -> None:
        """
        Updates the image in the specified row of the table view.

        Args:
            row_index (int): The row index where the image should be updated.
            pixmap (QPixmap): The QPixmap image to set in the table.
        """
        model = self.filter_proxy_model.sourceModel()

        if model:
            item = model.item(row_index, 9)
            if item:
                item.setData(pixmap, Qt.ItemDataRole.DecorationRole)

    def cb_toggle_uni(self) -> None:
        """Applies the selected universe filter to the table."""
        legends_checked = self.ui_main.checkBox_Legends.isChecked()
        canon_checked = self.ui_main.checkBox_Canon.isChecked()
        
        filter_condition = None

        if canon_checked:
            filter_condition = r"Canon"
        elif legends_checked:
            filter_condition = r"Legend"

        if filter_condition:
            self.uni_filter(filter_condition)


    def cb_toggle_novel(self) -> None:
        """Applies the selected novel filter to the table."""
        gb_checked = self.ui_main.checkBox_GB.isChecked()
        jra_checked = self.ui_main.checkBox_JRA.isChecked()
        na_checked = self.ui_main.checkBox_NA.isChecked()
        ojr_checked = self.ui_main.checkBox_OJR.isChecked()
        on_checked = self.ui_main.checkBox_ON.isChecked()
        s_checked = self.ui_main.checkBox_S.isChecked()
        ya_checked = self.ui_main.checkBox_YA.isChecked()
        yr_checked = self.ui_main.checkBox_YR.isChecked()

        filter_string = []

        if gb_checked:
            filter_string.append("GB")
        if jra_checked:
            filter_string.append("JRA")
        if na_checked:
            filter_string.append("NA")
        if ojr_checked:
            filter_string.append("OJR")
        if on_checked:
            filter_string.append("ON")
        if s_checked:
            filter_string.append("S")
        if ya_checked:
            filter_string.append("YA")
        if yr_checked:
            filter_string.append("YR")

        filter_expression = "|".join(filter_string)
        self.novel_filter(filter_expression)

    def cb_toggle_era(self) -> None:
        """Applies the selected era filter to the table."""
        aor_checked = self.ui_main.checkBox_AOR.isChecked()
        dotj_checked = self.ui_main.checkBox_DOTJ.isChecked()
        fotj_checked = self.ui_main.checkBox_FOTJ.isChecked()
        njo_checked = self.ui_main.checkBox_NJO.isChecked()
        rote_checked = self.ui_main.checkBox_ROTE.isChecked()
        rotfo_checked = self.ui_main.checkBox_ROTFO.isChecked()
        thr_checked = self.ui_main.checkBox_THR.isChecked()
        tnr_checked = self.ui_main.checkBox_TNR.isChecked()
        tor_checked = self.ui_main.checkBox_TOR.isChecked()

        filter_string = []

        if aor_checked:
            filter_string.append("AOR")
        if dotj_checked:
            filter_string.append("DOTJ")
        if fotj_checked:
            filter_string.append("FOTJ")
        if njo_checked:
            filter_string.append("NJO")
        if rote_checked:
            filter_string.append("ROTE")
        if rotfo_checked:
            filter_string.append("ROTFO")
        if thr_checked:
            filter_string.append("THR")
        if tnr_checked:
            filter_string.append("TNR")
        if tor_checked:
            filter_string.append("TOR")

        filter_expression = "|".join(filter_string)
        self.era_filter(filter_expression)

    def uni_filter(self, filter_condition: str) -> None:
        """
        Applies the selected universe filter condition to the table.

        Args:
            filter_condition (str): The regular expression to filter the data.
        """

        self.filter_proxy_model.setFilterKeyColumn(7)
        self.filter_proxy_model.setFilterRegularExpression(
            QRegularExpression(filter_condition)
        )

        self.filter_proxy_model.invalidateFilter()

    def novel_filter(self, filter_expression: str) -> None:
        """
        Applies the selected novel filter expression to the table.

        Args:
            filter_expression (str): The regular expression to filter the data.
        """
        self.filter_proxy_model.setFilterKeyColumn(3)
        self.filter_proxy_model.setFilterRegularExpression(
            QRegularExpression(filter_expression)
        )
        self.filter_proxy_model.invalidateFilter()

    def era_filter(self, filter_expression: str) -> None:
        """
        Applies a regular expression filter to the filter proxy model.

        Args:
            filter_expression (str): The regular expression to filter the data.
        """
        self.filter_proxy_model.setFilterKeyColumn(2)
        self.filter_proxy_model.setFilterRegularExpression(
            QRegularExpression(filter_expression)
        )
        self.filter_proxy_model.invalidateFilter()

    def clear_filter(self) -> None:
        """
        Clears any active filter on the filter proxy model and resets the filter options.
        Also resets checkbox selections in the UI and scrolls the table view to the top.
        """
        self.filter_proxy_model.setFilterRegularExpression(QRegularExpression(""))
        self.filter_proxy_model.setFilterKeyColumn(-1)
        self.filter_proxy_model.invalidateFilter()

        # self.ui_main.checkBox_Canon.setAutoExclusive(False)
        # self.ui_main.checkBox_Legends.setAutoExclusive(False)

        # self.ui_main.checkBox_Canon.setChecked(False)
        # self.ui_main.checkBox_Legends.setChecked(False)

        # self.ui_main.checkBox_Canon.setAutoExclusive(True)
        # self.ui_main.checkBox_Legends.setAutoExclusive(True)

        button_group = self.ui_main.buttonGroup_Universe

        button_group.setExclusive(False)

        # Uncheck the checkboxes
        self.ui_main.checkBox_Canon.setChecked(False)
        self.ui_main.checkBox_Legends.setChecked(False)

        # Re-enable the exclusive behavior
        button_group.setExclusive(True)
        
        self.ui_main.checkBox_GB.setChecked(False)
        self.ui_main.checkBox_JRA.setChecked(False)
        self.ui_main.checkBox_NA.setChecked(False)
        self.ui_main.checkBox_OJR.setChecked(False)
        self.ui_main.checkBox_ON.setChecked(False)
        self.ui_main.checkBox_S.setChecked(False)
        self.ui_main.checkBox_YA.setChecked(False)
        self.ui_main.checkBox_YR.setChecked(False)

        self.ui_main.checkBox_AOR.setChecked(False)
        self.ui_main.checkBox_DOTJ.setChecked(False)
        self.ui_main.checkBox_FOTJ.setChecked(False)
        self.ui_main.checkBox_NJO.setChecked(False)
        self.ui_main.checkBox_ROTE.setChecked(False)
        self.ui_main.checkBox_ROTFO.setChecked(False)
        self.ui_main.checkBox_THR.setChecked(False)
        self.ui_main.checkBox_TNR.setChecked(False)
        self.ui_main.checkBox_TOR.setChecked(False)

        self.ui_main.tableView.verticalScrollBar().setValue(0)

    def debug_model_data(self):
        """
        Prints the data from column 7 of the source model for each row in the filter proxy model.
        """
        for row in range(self.filter_proxy_model.sourceModel().rowCount()):
            data = self.filter_proxy_model.sourceModel().index(row, 7).data()
            print(f"Row {row}, Column 7: {data}")

    def logo1_clicked(self) -> None:
        """
        Handles the logo1 click event. Hides the text browser, loads the table, and clicks the top carrot button.
        """
        self.ui_main.textBrowser.setVisible(False)
        self.load_table()
        self.top_carrot_clicked()
        self.ui_main.pushButton_Side_Menu_Carrot.setVisible(True)
        

    def side_carrot_clicked(self) -> None:
        """
        Toggles the side menu's visibility. Expands or collapses the side menu based on its current state.
        """
        width = self.ui_main.frame_SW_Filter_Menu.width()

        if width == 0:
            new_width = 233
            new_button_geometry = QtCore.QRect(931, 300, 30, 30)
            new_button_text = "⏵"
        else:
            new_width = 0
            new_button_geometry = QtCore.QRect(1163, 300, 30, 30)
            new_button_text = "⏴"

        self.animate = QPropertyAnimation(
            self.ui_main.frame_SW_Filter_Menu, b"geometry"
        )
        self.animate.setDuration(250)
        self.animate.setStartValue(self.ui_main.frame_SW_Filter_Menu.geometry())
        if width == 0:
            self.animate.setEndValue(
                QRect(
                    self.ui_main.frame_SW_Filter_Menu.x(),
                    self.ui_main.frame_SW_Filter_Menu.y(),
                    new_width,
                    self.ui_main.frame_SW_Filter_Menu.height(),
                )
            )
        else:
            self.animate.setEndValue(
                QRect(
                    self.ui_main.frame_SW_Filter_Menu.x(),
                    self.ui_main.frame_SW_Filter_Menu.y(),
                    0,
                    self.ui_main.frame_SW_Filter_Menu.height(),
                )
            )
        self.animate.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animate.start()

        self.ui_main.pushButton_Side_Menu_Carrot.setGeometry(new_button_geometry)
        self.ui_main.pushButton_Side_Menu_Carrot.setText(new_button_text)
        
        if self.ui_main.frame_Logo.height() == 59:
            self.ui_main.frame_Logo.setGeometry(1, 1, 1194, 0)
            self.ui_main.pushButton_Top_Menu_Carrot.setGeometry(582, 0, 30, 30)
            self.ui_main.pushButton_Top_Menu_Carrot.setText("⏷")
            
        if self.ui_main.frame_Menu_Left.width() == 131:
            self.ui_main.frame_Menu_Left.setGeometry(0, 50, 41, 641)    

    def top_carrot_clicked(self) -> None:
        """
        Toggles the top menu's visibility. Expands or collapses the top menu based on its current state.
        """
        flheight = self.ui_main.frame_Logo.height()

        if flheight == 0:
            newflheight = 59
            new_button_geometry = QtCore.QRect(582, 59, 30, 30)
            new_button_text = "⏶"
        else:
            newflheight = 0
            new_button_geometry = QtCore.QRect(582, 0, 30, 30)
            new_button_text = "⏷"

        self.animate = QPropertyAnimation(self.ui_main.frame_Logo, b"geometry")
        self.animate.setDuration(250)
        self.animate.setStartValue(self.ui_main.frame_Logo.geometry())
        self.animate.setEndValue(
            QRect(
                self.ui_main.frame_Logo.x(),
                self.ui_main.frame_Logo.y(),
                self.ui_main.frame_Logo.width(),
                newflheight,
            )
        )
        self.animate.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animate.start()

        self.ui_main.pushButton_Top_Menu_Carrot.setGeometry(new_button_geometry)
        self.ui_main.pushButton_Top_Menu_Carrot.setText(new_button_text)
        
        if self.ui_main.frame_SW_Filter_Menu.width() == 233:
            self.ui_main.frame_SW_Filter_Menu.setGeometry(961, 2, 0, 639)
            self.ui_main.pushButton_Side_Menu_Carrot.setGeometry(1163, 300, 30, 30)
            self.ui_main.pushButton_Side_Menu_Carrot.setText("⏴")
            
        if self.ui_main.frame_Menu_Left.width() == 131:
            self.ui_main.frame_Menu_Left.setGeometry(0, 50, 41, 641)    

    def display_help(self) -> None:
        """
        Displays the help page or toggles the visibility of the help page and table view.

        This function:
        - Checks the current HTML file being displayed and determines whether to load the
        help page or show/hide the text browser and table view based on the current state.
        - When the help page is being shown for the first time, it updates the HTML file path
        to "Help.html" and loads it in the text browser.
        - When the help page is already visible, it hides the text browser and shows the table view.
        - If the table view is visible, it hides the table view and shows the help page.

        It handles visibility for both the text browser and the table view and ensures the correct
        HTML content is loaded.
        """
        print("Displaying help page...")

        if (
            self.html_file_path == "Splash.html"
            or self.html_file_path == "PrivacyPolicy.html"
            or self.html_file_path == "TermsOfService.html"
        ) and self.ui_main.textBrowser.isVisible():
            self.html_file_path = "Help.html"
            self.load_text_browser()
            self.ui_main.textBrowser.setVisible(True)
        elif (
            self.ui_main.textBrowser.isVisible() and self.html_file_path == "Help.html"
        ):
            self.ui_main.textBrowser.setVisible(False)
            if self.ui_main.pushButton_Side_Menu_Carrot.isVisible():
                self.ui_main.tableView.setVisible(True)
        else:
            self.html_file_path = "Help.html"
            self.ui_main.textBrowser.setVisible(True)
            self.load_text_browser()
            if self.ui_main.tableView.isVisible():
                self.ui_main.tableView.setVisible(False)

        print(f"Current HTML file: {self.html_file_path}")
        print(f"text browser visibility: {self.ui_main.textBrowser.isVisible()}")

    def display_privacy(self) -> None:
        """
        Displays the privacy page or toggles the visibility of the privacy page and table view.

        This function:
        - Checks the current HTML file being displayed and determines whether to load the
        privacy page or show/hide the text browser and table view based on the current state.
        - When the privacy page is being shown for the first time, it updates the HTML file path
        to "PrivacyPolicy.html" and loads it in the text browser.
        - When the privacy page is already visible, it hides the text browser and shows the table view.
        - If the table view is visible, it hides the table view and shows the privacy page.

        It handles visibility for both the text browser and the table view and ensures the correct
        HTML content is loaded.
        """
        print("Displaying privacy page...")
        self.ui_main.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ui_main.textBrowser.verticalScrollBar().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        if (
            self.html_file_path == "Splash.html"
            or self.html_file_path == "Help.html"
            or self.html_file_path == "TermsOfService.html"
        ) and self.ui_main.textBrowser.isVisible():
            self.html_file_path = "PrivacyPolicy.html"
            self.load_text_browser()
            self.ui_main.textBrowser.setVisible(True)
        elif (
            self.ui_main.textBrowser.isVisible()
            and self.html_file_path == "PrivacyPolicy.html"
        ):
            self.ui_main.textBrowser.setVisible(False)
            if self.ui_main.pushButton_Side_Menu_Carrot.isVisible():
                self.ui_main.tableView.setVisible(True)
        else:
            self.html_file_path = "PrivacyPolicy.html"
            self.ui_main.textBrowser.setVisible(True)
            self.load_text_browser()
            if self.ui_main.tableView.isVisible():
                self.ui_main.tableView.setVisible(False)

        print(f"Current HTML file: {self.html_file_path}")
        print(f"text browser visibility: {self.ui_main.textBrowser.isVisible()}")
        
        self.ui_main.textBrowser.update()
        self.ui_main.textBrowser.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.ui_main.textBrowser.setMinimumHeight(300)
        
        if self.ui_main.textBrowser.toPlainText().strip() == "":
            print("No content in textBrowser to scroll.")
        else:
            print("Content in textBrowser ready for scrolling.")

    def display_terms(self) -> None:
        """
        Displays the terms page or toggles the visibility of the terms page and table view.

        This function:
        - Checks the current HTML file being displayed and determines whether to load the
        terms page or show/hide the text browser and table view based on the current state.
        - When the terms page is being shown for the first time, it updates the HTML file path
        to "PrivacyPolicy.html" and loads it in the text browser.
        - When the terms page is already visible, it hides the text browser and shows the table view.
        - If the table view is visible, it hides the table view and shows the terms page.

        It handles visibility for both the text browser and the table view and ensures the correct
        HTML content is loaded.
        """
        print("Displaying terms page...")
        self.ui_main.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        if (
            self.html_file_path == "Splash.html"
            or self.html_file_path == "PrivacyPolicy.html"
            or self.html_file_path == "Help.html"
        ) and self.ui_main.textBrowser.isVisible():
            self.html_file_path = "TermsOfService.html"
            self.load_text_browser()
            self.ui_main.textBrowser.setVisible(True)
        elif (
            self.ui_main.textBrowser.isVisible()
            and self.html_file_path == "TermsOfService.html"
        ):
            self.ui_main.textBrowser.setVisible(False)
            if self.ui_main.pushButton_Side_Menu_Carrot.isVisible():
                self.ui_main.tableView.setVisible(True)
        else:
            self.html_file_path = "TermsOfService.html"
            self.ui_main.textBrowser.setVisible(True)
            self.load_text_browser()
            if self.ui_main.tableView.isVisible():
                self.ui_main.tableView.setVisible(False)

        print(f"Current HTML file: {self.html_file_path}")
        print(f"text browser visibility: {self.ui_main.textBrowser.isVisible()}")

    def load_text_browser(self) -> None:
        """
        Loads the text browser with the specified HTML file.
        """
        try:
            with open(self.html_file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            self.ui_main.textBrowser.setHtml(html_content)

        except FileNotFoundError:
            print(f"Error: File '{self.html_file_path}' not found.")
            self.ui_main.textBrowser.setHtml(
                "<h1>Error</h1><p>HTML file not found.</p>"
            )
        except Exception as e:
            print(f"Error loading HTML file: {e}")
            self.ui_main.textBrowser.setHtml(f"<h1>Error</h1><p>{e}</p>")

    def exit_app(self) -> None:
        """Exits the application."""
        self.window_login.close()
        self.window_main.close()
        QApplication.quit()

    def maximize_app(self) -> None:
        """Maximizes the application."""
        pass

    def minimize_app(self) -> None:
        """Minimizes the application."""
        if self.window_main:
            self.window_main.showMinimized()

    def menu_app(self) -> None:
        """
        Toggles the visibility of the left-side menu, expanding or collapsing it based on its current width.
        """
        width = self.ui_main.frame_Menu_Left.width()

        if width == 41:
            newWidth = 131
        else:
            newWidth = 41

        self.animate = QPropertyAnimation(self.ui_main.frame_Menu_Left, b"geometry")
        self.animate.setDuration(100)
        self.animate.setStartValue(self.ui_main.frame_Menu_Left.geometry())
        self.animate.setEndValue(
            QRect(
                self.ui_main.frame_Menu_Left.x(),
                self.ui_main.frame_Menu_Left.y(),
                newWidth,
                self.ui_main.frame_Menu_Left.height(),
            )
        )
        self.animate.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animate.start()
        
        if self.ui_main.frame_SW_Filter_Menu.width() == 233:
            self.ui_main.frame_SW_Filter_Menu.setGeometry(961, 2, 0, 639)
            self.ui_main.pushButton_Side_Menu_Carrot.setGeometry(1163, 300, 30, 30)
            self.ui_main.pushButton_Side_Menu_Carrot.setText("⏴")
            
        if self.ui_main.frame_Logo.height() == 59:
            self.ui_main.frame_Logo.setGeometry(1, 1, 1194, 0)
            self.ui_main.pushButton_Top_Menu_Carrot.setGeometry(582, 0, 30, 30)
            self.ui_main.pushButton_Top_Menu_Carrot.setText("⏷")    

    def display_account(self) -> None:
        """Displays the account settings page."""
        width = self.ui_main.frame_profile.width()

        if width == 0:
            newWidth = 491
        else:
            newWidth = 0

        self.animate = QPropertyAnimation(self.ui_main.frame_profile, b"geometry")
        self.animate.setDuration(250)
        self.animate.setStartValue(self.ui_main.frame_profile.geometry())
        self.animate.setEndValue(
            QRect(
                self.ui_main.frame_profile.x(),
                self.ui_main.frame_profile.y(),
                newWidth,
                self.ui_main.frame_profile.height(),
            )
        )
        self.animate.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animate.start()
        
        if self.ui_main.frame_Menu_Left.width() == 131:
            self.ui_main.frame_Menu_Left.setGeometry(0, 50, 41, 641)
    def update_profile(self) -> None:
        """Updates the profile information in the account settings page."""
        credentials: List[Dict[str, str]] = self.read_csv('login_credentials.csv')
        
        address = self.ui_main.lineEdit_prof_address.text()
        city = self.ui_main.lineEdit_city.text()
        state = self.ui_main.comboBox_state.currentText()
        zip = self.ui_main.lineEdit_prof_zip.text()
        country = self.ui_main.comboBox_country.currentText()
        gender = self.ui_main.comboBox_gender.currentText()
        
        
        user_found: bool = False
        for record in credentials:
            if record['email'] == self.email :
                user_found: bool = True
                record['address'] = address
                record['city'] = city
                record['state'] = state
                record['zip'] = zip
                record['country'] = country
                record['gender'] = gender
                break
            
        if user_found:
                if not credentials:
                    raise Exception("Data to write is empty")
                try:
                    with open('login_credentials.csv', mode='w', newline='', encoding='utf-8') as file:
                        fieldnames = credentials[0].keys()
                        writer = csv.DictWriter(file, fieldnames=fieldnames)

                        writer.writeheader()
                        writer.writerows(credentials)
                        self.ui_main.label_success.setVisible(True)
                        QTimer.singleShot(3000, lambda: self.ui_main.label_success.setVisible(False))

                except Exception as e:
                    raise Exception(f"Error writing to file 'login_credentials.csv': {e}")

        else:
            raise Exception("User not found in credentials.")
    def change_password(self) -> None:
        """Displays the change password page if the user enters the correct password.
    
        This function checks if the user has entered the correct password by comparing the
        entered password with the one associated with the email stored in the CSV file 
        ('login_credentials.csv'). If the entered password is correct:
            - The password change menu will be shown by expanding the menu frame.
            - The warning label (label_prof_warning_2) will be hidden.
        If the password is incorrect:
            - The warning label will be shown to notify the user of the failed attempt.
        
        It uses the email stored in `self.email` (set during login) to find the associated 
        password in the CSV file. The CSV file should contain two columns: 'email' and 'password'."""

        credentials: List[Dict[str, str]] = self.read_csv('login_credentials.csv')

        entered_password: str = self.ui_main.lineEdit_prof_pass.text()

        user_found: bool = False
        for record in credentials:
            if record['email'] == self.email and record['password'] == entered_password:
                user_found: bool = True
                break
        
        if user_found:
            width: int = self.ui_main.frame_chg_pass.width()

            newWidth: int = 291 if width == 0 else 0

            self.animate = QPropertyAnimation(self.ui_main.frame_chg_pass, b"geometry")
            self.animate.setDuration(250)
            self.animate.setStartValue(self.ui_main.frame_chg_pass.geometry())
            self.animate.setEndValue(
                QRect(
                    self.ui_main.frame_chg_pass.x(),
                    self.ui_main.frame_chg_pass.y(),
                    newWidth,
                    self.ui_main.frame_chg_pass.height(),
                )
            )
            self.animate.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animate.start()

            self.ui_main.label_prof_warning_2.setVisible(False)
        else:
            self.ui_main.label_prof_warning_2.setVisible(True)
    
    def submit_changes(self) -> None:
        """Submits the password changes. If the new passwords match, the password is updated 
        in the login_credentials.csv file. The new password is saved only if the user 
        enters the correct current password.
        
        This function also validates that the new passwords match, then updates the password 
        of the user identified by their email stored in `self.email` in the CSV file.

        Raises:
            Exception: If an error occurs while writing the CSV file.
        """
        new_pass1 = self.ui_main.lineEdit_prof_new_pass.text()
        new_pass2 = self.ui_main.lineEdit_prof_new_pass_2.text()
        
        if new_pass1 == new_pass2:
            credentials: List[Dict[str, str]] = self.read_csv('login_credentials.csv')

            user_found: bool = False
            for record in credentials:
                if record['email'] == self.email:
                    record['password'] = new_pass1
                    user_found = True
                    break

            if user_found:
                if not credentials:
                    raise Exception("Data to write is empty")
                try:
                    with open('login_credentials.csv', mode='w', newline='', encoding='utf-8') as file:
                        fieldnames = credentials[0].keys()
                        writer = csv.DictWriter(file, fieldnames=fieldnames)

                        writer.writeheader()
                        writer.writerows(credentials)

                except Exception as e:
                    raise Exception(f"Error writing to file 'login_credentials.csv': {e}")

                self.ui_main.label_prof_warning.setText("Password changed successfully!")
                self.ui_main.label_prof_warning.setStyleSheet("color: green;")
                self.ui_main.label_prof_warning.setVisible(True)
                self.ui_main.lineEdit_prof_new_pass.clear()
                self.ui_main.lineEdit_prof_new_pass_2.clear()
                QTimer.singleShot(2000, self.close_change_pass)
            else:
                self.ui_main.label_prof_warning.setText("User not found.")
                self.ui_main.label_prof_warning.setStyleSheet("color: red;")
                self.ui_main.label_prof_warning.setVisible(True)
        else:
            self.ui_main.label_prof_warning.setText("Passwords do not match.")
            self.ui_main.label_prof_warning.setStyleSheet("color: red;")
            self.ui_main.label_prof_warning.setVisible(True)
        
    def close_change_pass(self) -> None:
        self.ui_main.frame_chg_pass.setGeometry(491, 201, 0, 261)
    
        self.ui_main.label_prof_warning.setVisible(False)
    def display_home(self) -> None:
        """
        Displays the privacy page or toggles the visibility of the Splash page and table view.

        This function:
        - Checks the current HTML file being displayed and determines whether to load the
        Splash page or show/hide the text browser and table view based on the current state.
        - When the Splash page is being shown for the first time, it updates the HTML file path
        to "PrivacyPolicy.html" and loads it in the text browser.
        - When the Splash page is already visible, it hides the text browser and shows the table view.
        - If the table view is visible, it hides the table view and shows the Splash page.

        It handles visibility for both the text browser and the table view and ensures the correct
        HTML content is loaded.
        """
        if self.ui_main.frame_profile.width() == 491:
            self.ui_main.frame_profile.setGeometry(0, 0, 0, 641)
            
        if (
            self.html_file_path == "PrivacyPolicy.html"
            or self.html_file_path == "Help.html"
            or self.html_file_path == "TermsOfService.html"
        ) and self.ui_main.textBrowser.isVisible():
            self.html_file_path = "Splash.html"
            self.load_text_browser()
            self.ui_main.textBrowser.setVisible(True)
        elif (
            self.ui_main.textBrowser.isVisible()
            and self.html_file_path == "Splash.html"
        ):
            self.ui_main.textBrowser.setVisible(True)
            if self.ui_main.pushButton_Side_Menu_Carrot.isVisible():
                self.ui_main.tableView.setVisible(True)
        else:
            self.html_file_path = "Splash.html"
            self.ui_main.textBrowser.setVisible(True)
            self.load_text_browser()
            if self.ui_main.tableView.isVisible():
                self.ui_main.tableView.setVisible(False)

        print(f"Current HTML file: {self.html_file_path}")
        print(f"text browser visibility: {self.ui_main.textBrowser.isVisible()}")
        
        self.ui_main.textBrowser.update()
        self.ui_main.textBrowser.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.ui_main.textBrowser.setMinimumHeight(300)
        
        if self.ui_main.textBrowser.toPlainText().strip() == "":
            print("No content in textBrowser to scroll.")
        else:
            print("Content in textBrowser ready for scrolling.")
            
        if self.ui_main.frame_Menu_Left.width() == 131:
            self.ui_main.frame_Menu_Left.setGeometry(0, 50, 41, 641)
        

    def display_settings(self) -> None:
        """Displays the settings page."""
        pass


class ImageLoaderThread(QThread):
    image_loaded = pyqtSignal(int, QPixmap)

    def __init__(
        self, thumbnail_paths: List[str], parent: Optional[QThread] = None
    ) -> None:
        """
        Initializes the image loader thread with the provided list of thumbnail paths.

        Args:
            thumbnail_paths (List[str]): List of file paths to the images.
            parent (Optional[QThread], optional): The parent thread, defaults to None.
        """
        super().__init__(parent)
        self.thumbnail_paths = thumbnail_paths

    def run(self) -> None:
        """
        Loads images in the background and emits a signal when each image is loaded.
        """
        for row_index, image_path in enumerate(self.thumbnail_paths):
            # print(f"Loading image for row {row_index}: {image_path}... (Thread)")

            if image_path:

                pixmap = QPixmap(image_path)

                if not pixmap.isNull():

                    pixmap = pixmap.scaled(100, 200, Qt.AspectRatioMode.KeepAspectRatio)
                    self.image_loaded.emit(row_index, pixmap)
                else:
                    print(f"Image not found for row {row_index}: {image_path}")
                    self.image_loaded.emit(row_index, QPixmap())
            else:
                print(f"No image path provided for row {row_index}")
                self.image_loaded.emit(row_index, QPixmap())
