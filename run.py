import arcade
from soul_stars.game.views.dev_room import DevRoomView, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    window.show_view(DevRoomView())
    arcade.run()

if __name__ == "__main__":
    main()