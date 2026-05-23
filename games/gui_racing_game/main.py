import turtle
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FINISH_LINE_X = 350

PLAYER_SPEED = 15
ATTACK_RANGE = 40
ATTACK_DAMAGE = 1
MAX_HEALTH = 10


class Racer:
    def __init__(self, color, start_x, start_y, up_key, down_key, attack_key):
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setheading(0)
        self.turtle.goto(start_x, start_y)
        self.health = MAX_HEALTH
        self.up_key = up_key
        self.down_key = down_key
        self.attack_key = attack_key
        self.score_display = turtle.Turtle(visible=False)
        self.score_display.penup()
        self.score_display.hideturtle()

    def move_forward(self):
        self.turtle.forward(PLAYER_SPEED)

    def move_backward(self):
        self.turtle.backward(PLAYER_SPEED)

    def attack(self, other):
        if self.is_close(other):
            other.health = max(0, other.health - ATTACK_DAMAGE)
            self.flash_attack()
            return True
        return False

    def is_close(self, other):
        return abs(self.turtle.xcor() - other.turtle.xcor()) < ATTACK_RANGE

    def flash_attack(self):
        original_color = self.turtle.pencolor()
        self.turtle.color("yellow")
        turtle.ontimer(lambda: self.turtle.color(original_color), 100)

    def is_finished(self):
        return self.turtle.xcor() >= FINISH_LINE_X

    def reset(self, x, y):
        self.turtle.goto(x, y)
        self.health = MAX_HEALTH

    def draw_health(self):
        x, y = self.turtle.xcor(), self.turtle.ycor() - 30
        self.score_display.clear()
        self.score_display.goto(x, y)
        self.score_display.write(f"HP: {self.health}", align="center", font=("Arial", 10, "bold"))


class RacingGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Turtle Racing Fight")
        self.screen.tracer(0)

        self.draw_track()

        self.player1 = Racer("blue", -350, 80, "w", "s", "d")
        self.player2 = Racer("red", -350, -80, "Up", "Down", "Right")

        self.message = turtle.Turtle(visible=False)
        self.message.penup()
        self.message.hideturtle()

        self.winner = None

        self.bind_keys()
        self.running = True

    def draw_track(self):
        border = turtle.Turtle(visible=False)
        border.penup()
        border.goto(-SCREEN_WIDTH / 2 + 20, -SCREEN_HEIGHT / 2 + 20)
        border.pendown()
        border.pensize(3)
        for _ in range(2):
            border.forward(SCREEN_WIDTH - 40)
            border.left(90)
            border.forward(SCREEN_HEIGHT - 40)
            border.left(90)

        finish = turtle.Turtle(visible=False)
        finish.penup()
        finish.color("green")
        finish.goto(FINISH_LINE_X, -SCREEN_HEIGHT / 2 + 20)
        finish.setheading(90)
        finish.pendown()
        finish.pensize(5)
        finish.forward(SCREEN_HEIGHT - 40)

        start = turtle.Turtle(visible=False)
        start.penup()
        start.color("black")
        start.goto(-SCREEN_WIDTH / 2 + 40, -SCREEN_HEIGHT / 2 + 20)
        start.setheading(90)
        start.pendown()
        start.pensize(3)
        start.forward(SCREEN_HEIGHT - 40)

        self.draw_labels()

    def draw_labels(self):
        label = turtle.Turtle(visible=False)
        label.penup()
        label.goto(0, SCREEN_HEIGHT / 2 - 40)
        label.write("Autonomous Turtle Race: first to the finish or knockout wins. Press R to restart.", align="center", font=("Arial", 14, "normal"))

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.reset_game, "r")
        self.screen.onkey(self.quit_game, "q")

    def autopilot(self, racer, opponent):
        if not self.running or self.winner:
            return
        if racer.is_close(opponent):
            if racer.attack(opponent):
                self.display_feedback(f"{racer.turtle.color()[0].capitalize()} hit {opponent.turtle.color()[0].capitalize()}!")
                if opponent.health <= 0:
                    self.winner = racer
                    self.running = False
                    self.display_winner(f"{racer.turtle.color()[0].capitalize()} wins by knockout!")
        else:
            racer.move_forward()

    def do_attack(self, attacker, defender):
        if attacker.attack(defender):
            self.display_feedback(f"{attacker.turtle.color()[0].capitalize()} attacked {defender.turtle.color()[0].capitalize()}!")
            if defender.health <= 0:
                self.winner = attacker
                self.running = False
                self.display_winner(f"{attacker.turtle.color()[0].capitalize()} wins by knockout!")

    def display_feedback(self, text):
        self.message.clear()
        self.message.goto(0, SCREEN_HEIGHT / 2 - 70)
        self.message.write(text, align="center", font=("Arial", 14, "bold"))
        self.screen.ontimer(self.message.clear, 1200)

    def display_winner(self, text):
        self.message.clear()
        self.message.goto(0, 0)
        self.message.write(text + " Press R to restart.", align="center", font=("Arial", 18, "bold"))

    def reset_game(self):
        self.running = True
        self.winner = None
        self.message.clear()
        self.player1.reset(-350, 80)
        self.player2.reset(-350, -80)
        self.player1.draw_health()
        self.player2.draw_health()

    def quit_game(self):
        self.running = False
        self.screen.bye()

    def update(self):
        if self.running and not self.winner:
            self.autopilot(self.player1, self.player2)
            self.autopilot(self.player2, self.player1)
            self.player1.draw_health()
            self.player2.draw_health()
            self.check_finish_line()
            self.screen.update()
            self.screen.ontimer(self.update, 50)

    def check_finish_line(self):
        if self.player1.is_finished() and self.player2.is_finished():
            self.winner = self.player1 if self.player1.turtle.xcor() > self.player2.turtle.xcor() else self.player2
            self.running = False
            self.display_winner(f"{self.winner.turtle.color()[0].capitalize()} wins by crossing first!")
        elif self.player1.is_finished():
            self.winner = self.player1
            self.running = False
            self.display_winner("Blue wins by crossing first!")
        elif self.player2.is_finished():
            self.winner = self.player2
            self.running = False
            self.display_winner("Red wins by crossing first!")

    def start(self):
        self.reset_game()
        self.update()
        self.screen.mainloop()


if __name__ == "__main__":
    game = RacingGame()
    game.start()
