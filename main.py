def on_button_pressed_a():
    global people
    people += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global people
    people += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

people = 0

def on_forever():
    if people == 20:
        basic.show_string("Warning")
    else:
        basic.show_number(people)
basic.forever(on_forever)
