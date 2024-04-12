import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def _cerca_iscritti(self, cod_corso):
        return self._model._cerca_iscritti(cod_corso)

    def _cerca_corsi(self, matr_studente):
        return self._model._cerca_corsi(matr_studente)

    def _cerca_studente(self, matr_studente):
        return self._model._cerca_studente(matr_studente)

    def _return_corso(self, cod_corso):
        return self._model._return_corso(cod_corso)
    def _return_studente(self, matricola):
        return self._model._return_studente(matricola)

    def _nuova_iscrizione(self, matricola, cod_corso):
        return self._model._nuova_iscrizione(matricola, cod_corso)