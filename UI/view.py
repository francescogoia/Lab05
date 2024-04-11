import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_iscritti = None
        self.dd_corsi = None
        self.txt_matricola = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscriviti = None

        self.txt_output = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )
        """
        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()
        """
        ## mio codice
        self.dd_corsi = ft.Dropdown(label="corso", width=750)
        self._fill_selettore_corso()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._cerca_iscritti)
        ## row1
        row1 = ft.Row([self.dd_corsi, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)

        ## row2
        self.txt_matricola = ft.TextField(label="matricola")
        self.txt_nome = ft.TextField(label="nome", read_only=True)
        self.txt_cognome = ft.TextField(label="cognome", read_only=True)
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        ## row3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente")
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi")
        self.btn_iscriviti = ft.ElevatedButton(text="Iscriviti")
        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscriviti], alignment=ft.MainAxisAlignment.CENTER)

        self.txt_output = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, row3, self.txt_output)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def _fill_selettore_corso(self):
        for i in self._controller._model._corsi.items():
            self.dd_corsi.options.append(ft.dropdown.Option(key=i[0], text=i[1]))

    def _cerca_iscritti(self, e):
        corso = self.dd_corsi.value
        lista_studenti = self._controller._cerca_iscritti(corso)
        for i in lista_studenti:
            self.txt_output.controls.append(ft.Text(value=i.__str__()))

        self.update_page()