from controllers.menu_controller import MenuController
from utils.clear import clear_terminal
from views.menu_view import MenuView

def main() -> None:
    """
    Main entry point of the application.

    :param None
    :type None
    :raises KeyboardInterrupt: If the user interrupts the script with Ctrl+C
    :return: None
    :rtype: None
    """
    menu_controller = MenuController()
    menu_controller.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_terminal()
        print("\nScript interrompu par l'utilisateur.")
