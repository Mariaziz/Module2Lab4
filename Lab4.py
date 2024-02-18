if __name__ == "__main__":
    class SocSet:
        """Базовый класс для социальных сетей.
        Атрибуты:
            Name (str): Название социальной сети.
            Who (str): Имя основателя социальной сети.
            Year (int): Год основания социальной сети.
        Методы:
            __init__(self, Name: str, Who: str, Year: int) -> None:
                Конструктор класса СоциальнаяСеть.
            __str__(self) -> str:
                Возвращает строковое представление социальной сети.
        """

        def __init__(self, Name: str, Who: str, Year: int) -> None:
            self.Name = Name
            self.Who = Name
            self.Year = Year

        def __str__(self) -> str:
            return f"{self.Name} основана {self.Year} году, основатель: {self.Who}"


    class VK(SocSet):
        """
        Дочерний класс - социальная сеть VK.
        Атрибуты:
            Users (int): Количество пользователей в социальной сети VK.
        Методы:
            __init__(self, Name: str, Who: str, Year: int, Users: int) -> None:
                Конструктор класса VK.
            __str__(self) -> str:
                Возвращает строковое представление социальной сети VK.
        """

        def __init__(self, Name: str, Who: str, Year: int, Users: int) -> None:
            super().__init__(Name, Who, Year)
            self.Users = Users

        def __str__(self) -> str:
            return f"{super().__str__()} - Количество пользователей: {self.Users}"


    class Facebook(SocSet):
        """
        Дочерний класс - социальная сеть Facebook.
        Атрибуты:
            Active_Users (int): Количество активных пользователей в социальной сети Facebook.
        Методы:
            __init__(self, название: str, основатель: str, год_основания: int, активные_пользователи: int) -> None:
                Конструктор класса Facebook.
            __str__(self) -> str:
                Возвращает строковое представление социальной сети Facebook.
        """

        def __init__(self, Name: str, Who: str, Year: int, Active_Users: int) -> None:
            super().__init__(Name, Who, Year)
            self.Active_Users = Active_Users

        def __str__(self) -> str:
            return f"{super().__str__()} - Активные пользователи: {self.Active_Users}"

    # Пример использования классов
    vk = VK("VK", "Павел Дуров", 2006, 500000000)
    facebook = Facebook("Facebook", "Марк Цукерберг", 2004, 2500000000)

    print(vk)
    print(facebook)