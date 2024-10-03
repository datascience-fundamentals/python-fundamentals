"""
Este es el modulo que incluye la clase
de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor
    de musica
    """

    def play(self, song, by="radio"):
        """
        Reproduce la cancion que recibe como parametro

        Parameters:
          song (str): este es un string con el path de la cancion
          medio (str): parametro opcional

        Returns:
          int: devuelve 1 si reproduce con exito, caso contrario devuelve 0
        """
        print("reproduciendo musica", song, by)
        return 0

    def stop(self):
        """
        Deja de reproducir la musica
        """
        print("stopping")
