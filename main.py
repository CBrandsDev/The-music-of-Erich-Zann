import pyglet
from pyglet.window import key

window = pyglet.window.Window()

title_label = pyglet.text.Label('The music of Erich Zann',
                                font_name='Times New Roman',
                                font_size=36,
                                x=window.width//2, y=window.height//2,
                                anchor_x='center', anchor_y='center')

menu_label = pyglet.text.Label('Press enter to start',
                                font_name='Times New Roman',
                                font_size=24,
                                x=window.width//2, y=window.height//2-50,
                                anchor_x='center', anchor_y='center')

logo_image = pyglet.image.load('logo.jpg')
logo_sprite = pyglet.sprite.Sprite(logo_image, x=window.width/2, y=window.height/2)
logo_sprite.opacity = 0

warning_image = pyglet.image.load('warning.jpg')
warning_sprite = pyglet.sprite.Sprite(warning_image, x=window.width/2, y=window.height/2)
warning_sprite.opacity = 0

game_started = False

@window.event
def on_draw():
    window.clear()
    if not game_started:
        warning_sprite.draw()
        title_label.draw()
        menu_label.draw()
    else:
        logo_sprite.draw()


def fade_out(dt):
    global game_started
    warning_sprite.opacity = 10
    if warning_sprite.opacity <= 0:
        pyglet.clock.unschedule(fade_out)
        game_started = True
        pyglet.clock.schedule_once(fade_in, 1)
    

def fade_in(dt):
    logo_sprite.opacity += 10
    if logo_sprite.opacity >= 255:
        pyglet.clock.unschedule(fade_in)
        

def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        start_game()
    elif symbol == key.ESCAPE:
        end_game()

def start_game():
    global game_started
    game_started = True
    pyglet.clock.schedule_once(end_game, 5)
    pyglet.clock.schedule_once(fade_out, 1)
    print('Starting game...')
    

def end_game():
    pyglet.app.exit()

window.push_handlers(on_key_press)
pyglet.clock.schedule_interval(fade_out, 1/30.0)
pyglet.app.run()


