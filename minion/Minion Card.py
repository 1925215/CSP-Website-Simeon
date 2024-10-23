import turtle as trtl
wn=trtl.Screen()
card_minion = "minion/click here minion.gif"
card = "minion/Happy Birthday Card.gif"

wn.addshape(card_minion)
wn.addshape(card)

minion  = trtl.Turtle()
minion.shape(card_minion)
wn.update
minion.goto(0,0)


def click_the_card(x,y):
    minion.shape(card)


minion.onclick(click_the_card)
wn.listen()
wn.mainloop()
