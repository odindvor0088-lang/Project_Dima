from abc import ABC, abstractmethod

class MediaDevice(ABC):

    MAX_VOLUME = 100
    MIN_VOLUME = 0
    BATTERY_WARNING_LEVEL = 20
    manufacturer_country = "Russia"

    def init(self, brand, model, battery_level, is_on, current_volume):
        self.brand = brand
        self.model = model
        self.is_on = is_on
        self.battery_level = battery_level
        self.current_volume = current_volume

    @abstractmethod
    def play(self):
        """начать воспроизведение"""
        pass

    @abstractmethod
    def stop(self):
        """остановить воспроизведение"""
        pass

    @abstractmethod
    def get_device_type(self):
        """возвращает тип устройства"""
        pass