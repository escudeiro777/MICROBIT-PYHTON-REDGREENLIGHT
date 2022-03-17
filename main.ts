// STATES
let REDLIGHT = 0
let state = 0
let GREENLIGHT = 0
GREENLIGHT = 1
REDLIGHT = 2
radio.setGroup(1)
// COMMUNICATION
state = 0
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    state = receivedNumber
})
// DISPLAY
REDLIGHT = 0
state = 0
GREENLIGHT = 0
basic.forever(function on_forever() {
    if (state == GREENLIGHT) {
        basic.showIcon(IconNames.Yes)
    } else if (state == REDLIGHT) {
        basic.showIcon(IconNames.No)
    }
    
})
// MOVEMENT CHECK
REDLIGHT = 0
state = 0
GREENLIGHT = 0
let movement = 0
basic.forever(function sempre() {
    
    if (state == REDLIGHT) {
        movement = Math.abs(input.acceleration(Dimension.Strength) - 1150)
        if (movement > 100) {
            game.gameOver()
        }
        
    }
    
})
// PLAYER CODE
movement = 0
REDLIGHT = 0
state = 0
GREENLIGHT = 0
GREENLIGHT = 1
REDLIGHT = 2
radio.setGroup(1)
basic.forever(function on_forever2() {
    
    if (state == REDLIGHT) {
        movement = Math.abs(input.acceleration(Dimension.Strength) - 1150)
        if (movement != 0) {
            game.gameOver()
        }
        
    }
    
})
