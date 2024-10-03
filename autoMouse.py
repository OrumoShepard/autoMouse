import pyautogui
import time
import random
import keyboard

#Constants
LAPSE = 60
MOVE_SPEED = 0.5

def random_mouse_movement():
    # Desktop dimension
    wide, height = pyautogui.size()

    # Init the timer
    init_time = time.time()

    print("Press ESC to stop the program...")

    while True:
        # Verify if ESC is pressed
        if keyboard.is_pressed("esc"):
            print("Stopping the program...")
            break

        # We test the pass of time
        lapsed_time = time.time() - init_time
        if int(lapsed_time)>LAPSE:
            # We generate new random coordinates
            x = random.randint(10, wide - 11)
            y = random.randint(10, height - 11)

            # We move the cursor to the new coordinates
            pyautogui.moveTo(x, y, duration=MOVE_SPEED)  # Smooth movement

            # We wait the LAPSE in seconds to move it again
            init_time = time.time()


if __name__ == "__main__":
    random_mouse_movement()
