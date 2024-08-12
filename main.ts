input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        `)
})
basic.forever(function () {
    led.plotBarGraph(
    input.soundLevel(),
    225
    )
})
