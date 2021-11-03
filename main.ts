input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    people += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    people += -1
})
let people = 0
basic.forever(function on_forever() {
    if (people == 20) {
        basic.showString("Warning")
    } else {
        basic.showNumber(people)
    }
    
})
