from model.incidencias_model import IncidenciaModel
from view.incidencias_view import IncidenciaView
from controller.incidencias_controller import IncidenciaController


def main():

    model = IncidenciaModel()
    view = IncidenciaView()

    IncidenciaController(model, view)

    view.iniciar()


if __name__ == "__main__":
    main()