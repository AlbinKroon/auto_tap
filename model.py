#!/usr/bin/env python3
import random

class Button():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def click(self, device):
        device.shell(f"input tap {self.x_pos} {self.y_pos}")

class Menu():
    close = Button(int("3ef", 16), int("4ed", 16))
    toggle = Button(int("deadbeef", 16), int("87c", 16))
    upgrades = []

    def open(self):
        self.close.click(self.device)
        self.toggle.click(self.device)
    
    def upgrade(self):
        self.open()
        for button in self.upgrades:
            button.click(self.device)

class AttackMenu(Menu):
    def __init__(self, device):
        self.device = device
        self.toggle.x_pos = int("7c", 16)
        self.upgrades.append(Button(int("39f", 16), int("618", 16)))

class HeroMenu(Menu):
    def __init__(self, device):
        self.device = device
        self.toggle.x_pos = int("125", 16)
        self.upgrades.append(Button(int("39f", 16), int("618", 16)))
        self.upgrades.append(Button(int("39f", 16), int("6c6", 16)))
        self.upgrades.append(Button(int("39f", 16), int("77d", 16)))
        self.upgrades.append(Button(int("39f", 16), int("814", 16)))
    

class Game():
    def __init__(self, device):
        self.device = device
        self.attack = Button(540, 475)
        self.attack_menu = AttackMenu(device)
        self.hero_menu = HeroMenu(device)
        self.fight_boss = Button(int("3d5", 16), int("b6", 16))

    def play(self):
        while True:
            for _ in range(40):
                self.attack.click(self.device)
            if random.uniform(0, 1) > 0.5:
                self.attack_menu.upgrade()
            else:
                self.hero_menu.upgrade()
            self.fight_boss.click(self.device)