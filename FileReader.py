def read_text_file(file_path):
    """
    Reads and returns the contents of a text file.

    :param file_path: Path to the text file
    :return: Contents of the text file as a string
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except IOError as e:
        raise IOError(f"An I/O error occurred: {e}")