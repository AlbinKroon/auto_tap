#!/usr/bin/env python3
import random

from ppadb.device import Device

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Button():
    def __init__(self, position: Point):
        self.position = position

    def click(self, device: Device) -> None:
        device.shell(f"input tap {self.position.x} {self.position.y}")
        return None

class MenuInterface():
    def get_upgrades(self) -> list:
        pass

    def get_close(self) -> Button:
        pass

    def get_open(self) -> Button:
        pass
    
    def upgrade(self) -> None:
        pass

    def scroll_up(self) -> None:
        pass

class AttackMenu(MenuInterface):
    def __init__(self, device: Device):
        self.device = device
        self.open = Button(Point(int("7c", 16), int("87c", 16)))
        self.close = Button(Point(int("3ef", 16), int("4ed", 16)))
        self.upgrades = [Button(Point(int("39f", 16), int("618", 16)))]

    def get_upgrades(self) -> list:
        return self.upgrades

    def get_close(self) -> Button:
        return self.close

    def get_open(self) -> Button:
        return self.open
    
    def upgrade(self) -> None:
        self.get_open().click(self.device)
        self.scroll_up()
        for button in self.get_upgrades():
            button.click(self.device)
        self.get_close().click(self.device)
        return None

    def scroll_up(self) -> None:
        x = int('1fa', 16)
        y_from = int('622', 16)
        y_to = int('802', 16)
        self.device.shell(f"input swipe {x} {y_from} {x} {y_to}")
        return None

class HeroMenu(MenuInterface):
    def __init__(self, device: Device):
        self.device = device
        self.open = Button(Point(int("125", 16), int("87c", 16)))
        self.close = Button(Point(int("3ef", 16), int("4ed", 16)))
        self.upgrades = [Button(Point(int("39f", 16), int("618", 16))),
                         Button(Point(int("39f", 16), int("6c6", 16))), 
                         Button(Point(int("39f", 16), int("77d", 16))), 
                         Button(Point(int("39f", 16), int("814", 16)))]

    def get_upgrades(self) -> list:
        return self.upgrades

    def get_close(self) -> Button:
        return self.close

    def get_open(self) -> Button:
        return self.open

    def upgrade(self) -> None:
        self.get_open().click(self.device)
        self.scroll_up()
        for button in self.get_upgrades():
            button.click(self.device)
        self.get_close().click(self.device)
        return None
    
    def scroll_up(self) -> None:
        x = int('1fa', 16)
        y_from = int('600', 16)
        y_to = int('900', 16)
        self.device.shell(f"input swipe {x} {y_from} {x} {y_to}")
        return None

class Game():
    def __init__(self, device: Device):
        self.attacks_before_upgrade = 30
        self.device = device
        self.attack = Button(Point(int("297", 16), int("682", 16)))
        self.attack_menu = AttackMenu(device)
        self.hero_menu = HeroMenu(device)
        self.fight_boss = Button(Point(int("3d5", 16), int("b6", 16)))

    def setup(self) -> None:
        pass

    def play(self) -> None:
        self.setup()
        while True:
            for _ in range(self.attacks_before_upgrade):
                self.attack.click(self.device)
            if bool(random.randint(0,5)):
                self.hero_menu.upgrade()
            else:
                self.attack_menu.upgrade()
            self.fight_boss.click(self.device)
