# Simplified Asteroids (Python + Pygame)

This project is a classic arcade-style game inspired by the original **Asteroids** computer game released in 1979.  
It was built using **Python** and **Pygame** as part of the course  
[Build Asteroids using Python and Pygame](https://boot.dev) by *boot.dev*.

---

## License

- **Code, images, and most sounds**: [MIT License](./LICENSE)  
- **Song "LateNight1"**:  
  LateNight1 © 2023 by Sebastian Lein is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).  
  This license applies only to the file `/sounds/LateNight1.ogg`.  

---

## 📌 Versions

- **v1.0.0**  
  Initial version completed after finishing the Boot.dev course.

- **v2.0.0**  
  Extended with new features:
  - Added main menu and background images  
  - Game improvements:    
    - Game no longer closes after the first hit
    - Multiple lives + life bar 
    – After losing the round, the player is sent to the new respawn menu  
  - Respawn menu with round statistics  
  - Scoring system:
    - **+10 points** for destroying a large asteroid  
    - **+20 points** for destroying a medium asteroid  
    - **+30 points** for destroying a small asteroid  

- **v2.1.0**  
  Audio update:
  - Added background music (*LateNight1*, licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)) 
  - Added sound effects for gameplay events      

---

## 🚀 How to Run
1. Clone this repository:

   ```bash
   git clone https://github.com/sebasukodo/asteroids_game.git
   cd asteroids_game
   ```

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the game:

   ```bash
   python main.py
   ```

### Alternative: Run with Virtual Environment (venv)

If you prefer to use a virtual environment:

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows (PowerShell)
   ```

2. Install dependencies inside the environment:

   ```bash
   pip install pygame
   ```

3. Run the game:

   ```bash
   python main.py
   ```


---

## 🎮 Controls

* **W** – Move forward
* **A / D** – Rotate left / right
* **S** – Slow down
* **Space** – Fire bullets