from UI.ui import ui_menu, ui_get_command, ui_run_command
from tests.tests import test_all
def main():
    """
    Functia principala a aplicatiei care ruleaza testele automate si porneste bucla meniului UI
    :return: None
    """
    test_all()
    numbers = []
    while True:
        ui_menu()
        command = ui_get_command()
        if command == "exit":
            exit()
        ui_run_command(command, numbers)

if __name__ == "__main__":
    main()