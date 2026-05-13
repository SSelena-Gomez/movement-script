# Premium Movement Suite - CS 1.6 (V7)

An advanced external movement optimizer for Counter-Strike 1.6 that implements **Priority Snap-Tap (SOCD)** logic. This tool is designed to enhance strafe precision by managing simultaneous key presses (A and D) through an external Python-based engine.

## ✨ Features
- **Smart SOCD Engine**: Automatically manages conflicting cardinal directions (A/D).
- **Trigger-Based Activation**: Snap-Tap logic only activates when `SPACE` or `CTRL` is held, allowing for natural movement during normal walking.
- **Steam Verification**: Built-in security check to ensure compatibility with the official Steam version of the game.
- **Encrypted Config**: Loads configuration from an encrypted `null.txt` file for integrity.
- **Zero Console Injection**: Works externally without modifying game files or sending visible console commands.

## 🚀 How it Works
The script uses a high-frequency input listener to monitor keyboard states. When a "Trigger Key" (Space or Ctrl) is active, the engine ensures that if both `A` and `D` are pressed, the **latest** input takes priority by virtually releasing the previous one. This results in perfect strafes and improved Bhop synchronization.

## 🛠️ Installation
1. Install [Python 3.x](https://www.python.org/).
2. Install dependencies:
   ```bash
   pip install psutil pygetwindow pynput

More updates will be soon
Made by love and boring
If it works for you send me a gift on steam
[![Steam Profile](https://img.shields.io/badge/STEAM-PROFILE-blue?style=for-the-badge&logo=steam)](https://steamcommunity.com/id/valvesucksmydick)
