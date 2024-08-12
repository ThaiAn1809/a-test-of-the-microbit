def on_gesture_shake():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    led.plot_bar_graph(input.sound_level(), 225)
basic.forever(on_forever)
