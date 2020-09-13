# Tap Titans 2 auto battler

Play tap titans 2 without actually having to play the game

### Instructions
First connect your phone to your computer. **Only works with 2240x1080 phones, maybe...**
You need to have pipenv, the adb cli tool, and the adb server running.

```
adb start-server
```

Then install the dependencies with pipenv

```
pipenv install
```

Then run the script inside the virtual environment

```
pipenv run python taptitans.py
```

### Observe
You should not leave your device unattended since there are all kinds of things that can happen which might lead to the script running touch input in another app. Use with caution as this is just a fun little project that i threw together in a couple of hours. Don't expect me to fix any issues.

Only a few things are automated and these are:
1. Attack upgrades (or whatever they are called)
2. Hero upgrades
3. Actual attacks

This means prestige, equipment, artifacts and whatever else will have to be done manually as of right now.