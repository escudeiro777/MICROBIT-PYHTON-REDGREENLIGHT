#STATES
REDLIGHT = 0;
state = 0
GREENLIGHT = 0;
GREENLIGHT = 1;
REDLIGHT = 2;
radio.set_group(1);

#COMMUNICATION
state = 0;
def on_received_number(receivedNumber):
    global state
    state = receivedNumber
radio.on_received_number(on_received_number)

#DISPLAY
REDLIGHT = 0
state = 0
GREENLIGHT = 0

def on_forever():
    if state == GREENLIGHT:
        basic.show_icon(IconNames.YES)
    elif state == REDLIGHT:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever);

#MOVEMENT CHECK
REDLIGHT = 0
state = 0
GREENLIGHT = 0
movement = 0

def sempre():
    global movement
    if state == REDLIGHT:
        movement = abs(input.acceleration(Dimension.STRENGTH) - 1150)
        if movement > 100:
            game.game_over()
basic.forever(sempre)

#PLAYER CODE
movement = 0
REDLIGHT = 0
state = 0
GREENLIGHT = 0

def ao_receber_numero(receivedNumber):
    global state
    state = receivedNumber
    radio.on_received_number(ao_receber_numero)

GREENLIGHT = 1 
REDLIGHT = 2
radio.set_group(1)

def on_forever2():
    global movement
    if state == REDLIGHT:
        movement = abs(input.acceleration(Dimension.STRENGTH) - 1150)
        if movement != 0:
            game.game_over()
basic.forever(on_forever2)
