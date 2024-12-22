import os

def clear_terminal() -> None:
    """
    Clear the terminal screen.

    :param None
    :type None
    :raises None: This function does not raise any exceptions.
    :return: None
    :rtype: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')