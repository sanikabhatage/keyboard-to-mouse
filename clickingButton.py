import pyautogui
import keyboard
import time

class VirtualMouse:
    def __init__(self):
        # Set failsafe to False with caution
        pyautogui.FAILSAFE = True
        self.speed = 10

    def move_relative(self, x, y):
        current_x, current_y = pyautogui.position()
        pyautogui.moveRel(x * self.speed, y * self.speed)

    def click(self, button='left'):
        pyautogui.click(button=button)

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def run(self):
        print("Virtual Mouse Control Started")
        print("Use arrow keys to move")
        print("Space to left click")
        print("Right Ctrl to right click")
        print("Q/E to scroll up/down")
        print("Esc to exit")

        while True:
            if keyboard.is_pressed('esc'):
                break
            
            # Movement
            if keyboard.is_pressed('up'):
                self.move_relative(0, -1)
            if keyboard.is_pressed('down'):
                self.move_relative(0, 1)
            if keyboard.is_pressed('left'):
                self.move_relative(-1, 0)
            if keyboard.is_pressed('right'):
                self.move_relative(1, 0)
                
            # Clicks
            if keyboard.is_pressed('space'):
                self.click('left')
            if keyboard.is_pressed('right ctrl'):
                self.click('right')
                
            # Scrolling
            if keyboard.is_pressed('q'):
                self.scroll(1)
            if keyboard.is_pressed('e'):
                self.scroll(-1)
                
            time.sleep(0.01)  # Prevent high CPU usage

if __name__ == "__main__":
    mouse = VirtualMouse()
    mouse.run()