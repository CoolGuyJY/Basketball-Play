from gamelib import*
#variables
game = Game(800,600,"Basketball play")#game variable
bk = Image("court.jpg",game)

bk.resizeTo(800,600)

bk.draw()
game.update()

james = Image("jamesharden.png",game)
james.resizeBy(-40)
james.setSpeed(8,60)

michael = Image("michaeljordan.png",game)
michael.resizeBy(-50)
michael.setSpeed(5,60)

basket = Image("basket.png",game)
basket.resizeBy(-70)
basket.setSpeed(3,60)

ball = Image("ball.png",game)
ball.resizeBy(-80)

#essential game loop
while not game.over:
    game.processInput()


    bk.draw()
    james.move(True)
    michael.move(True)
    basket.move(True)
    ball.draw()
    ball.moveTo(mouse.x,mouse.y)
    game.update(30)

game.quit()
