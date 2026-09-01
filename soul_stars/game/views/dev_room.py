import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Dev Room"

class DevRoomView(arcade.View):
    """
    Dev Room view application
        - Demonstrates basic game mechanics and sprites
    """
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON
        # Sprite lists should be created here and set to none

        # Creates the sprite list for dev room
        self.sprites = arcade.TextureAnimationSprite(
            path = "soul_stars/assets/sprites/Ghost.gif", 
            center_x = 0.0, 
            center_y = 0.0, 
            scale = 1.0,
            animation: TextureAnimation | None = None )

        self.sprite = arcade.load_animated_gif("soul_stars/assets/sprites/Ghost.gif")
        self.sprite.position = self.center
        

    def reset(self):
        """Reset game to its initial state"""
        pass

    def on_draw(self):
        """Render the screen"""
        self.clear()

        # Call draw() on all sprite lists below

    def on_update(self, delta_time):
        """All logic to move + Game logic"""
        self.clear()


        self.sprites.update_animation(delta_time = 0.1)

    def on_key_press(self, key, key_modifiers):
        """Called whenever a key is pressed"""
        pass

    def on_key_release(self, key, key_modifiers):
        """Called whenever the user releases a previously pressed key"""
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves"""
        pass

    def on_mouse_press(self, x, y, button, key_modifers):
        """Called whenever the user presses a mouse button"""
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """Called whenever the user releases a mouse button"""
        pass
