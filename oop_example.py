class WeatherPhenomenon:
    """
    Класс - погодное явление
    """
    def __init__(self, condition):
        self.condition  = condition


class Wind(WeatherPhenomenon):
    """
    Класс - ветер
    """
    def __init__(self, condition):
        super().__init__(condition)
        self.force = True
        self.squall = True

    def __repr__(self):
        return 'Сильный шквалистый ветер'


class Rain(WeatherPhenomenon):
    """
    Класс - дождь
    """
    def __init__(self, condition):
        super().__init__(condition)
        self.force = True
        self.squall = False

    def _scale_saffir_simpson(self):
        if self.force == True and self.squall == True:
            return 'Тропический шторм'
        elif self.force == False and self.squall == True:
            return 'Тропическая депрессия'
        elif self.force == False and self.squall == False:
            return 'Солнечный :)'
        else:
            return 'Погода с gismeteo'


class Hurricane(Wind,Rain):
    """
    Класс - ураган
    """
    def __init__(self, condition, name, category):
        super().__init__(condition)
        self.force = True
        self.squall = True
        self.name = name
        self.category = category

    def new(self):
        if self._scale_saffir_simpson():
            return f'{self.name} был {self.category}'
        else:
            return f'{self.name} остался в море'

    def __repr__(self):
        return f'Ураган {self.name} был разрушительным его амплитуда достигла {self.category}'
