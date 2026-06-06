import random
import turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FINISH_LINE_X = 420
START_LINE_X = -420
NUM_RACERS = 10
PLAYER_SPEED = 14
AI_MIN_SPEED = 2.0
AI_MAX_SPEED = 4.0
LEVEL_SPEED_BOOST = 0.8
LANE_HEIGHT = 55

RACER_COLORS = [
    "blue",
    "red",
    "yellow",
    "orange",
    "purple",
    "lime",
    "cyan",
    "magenta",
    "white",
    "gold",
]


class Racer:
    def __init__(self, color, lane_y, name, is_player=False):
        self.name = name
        self.color = color
        self.is_player = is_player
        self.speed = 0
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setheading(0)
        self.turtle.goto(START_LINE_X, lane_y)
        self.label = turtle.Turtle(visible=False)
        self.label.penup()
        self.label.hideturtle()

    def reset(self, start_x, lane_y, speed):
        self.turtle.goto(start_x, lane_y)
        self.speed = speed
        self.turtle.setheading(0)
        self.draw_label()

    def move_forward(self):
        self.turtle.forward(PLAYER_SPEED)

    def move_backward(self):
        self.turtle.backward(PLAYER_SPEED)

    def move_auto(self):
        self.turtle.forward(self.speed)

    def is_finished(self):
        return self.turtle.xcor() >= FINISH_LINE_X

    def draw_label(self):
        self.label.clear()
        self.label.goto(self.turtle.xcor(), self.turtle.ycor() + 25)
        self.label.write(self.name, align="center", font=("Arial", 9, "bold"))


class RacingGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor("#0b1220")
        self.screen.title("Turtle Grand Prix")
        self.screen.tracer(0)

        self.level = 1
        self.winner = None
        self.running = False

        self.status = turtle.Turtle(visible=False)
        self.status.penup()
        self.status.color("white")
        self.status.hideturtle()

        self.message = turtle.Turtle(visible=False)
        self.message.penup()
        self.message.hideturtle()

        self.racers = []
        self.player = None
        self.ai_racers = []

        self.create_racers()
        self.draw_track()
        self.bind_keys()

    def create_racers(self):
        lane_start = (NUM_RACERS - 1) * LANE_HEIGHT / 2
        for index in range(NUM_RACERS):
            y = lane_start - index * LANE_HEIGHT
            color = RACER_COLORS[index % len(RACER_COLORS)]
            name = "You" if index == 0 else f"Bot {index}"
            racer = Racer(color, y, name, is_player=(index == 0))
            self.racers.append(racer)
            if index == 0:
                self.player = racer
            else:
                self.ai_racers.append(racer)

    def draw_track(self):
        border = turtle.Turtle(visible=False)
        border.penup()
        border.color("white")
        border.pensize(4)
        border.goto(-SCREEN_WIDTH / 2 + 20, -SCREEN_HEIGHT / 2 + 40)
        border.pendown()
        for _ in range(2):
            border.forward(SCREEN_WIDTH - 40)
            border.left(90)
            border.forward(SCREEN_HEIGHT - 80)
            border.left(90)

        for lane in range(1, NUM_RACERS):
            line = turtle.Turtle(visible=False)
            line.penup()
            line.color("#4b5563")
            line.goto(START_LINE_X, (NUM_RACERS - 1) * LANE_HEIGHT / 2 - lane * LANE_HEIGHT)
            line.setheading(0)
            line.pendown()
            line.forward(FINISH_LINE_X - START_LINE_X + 20)

        finish = turtle.Turtle(visible=False)
        finish.penup()
        finish.color("lime")
        finish.goto(FINISH_LINE_X, -SCREEN_HEIGHT / 2 + 40)
        finish.setheading(90)
        finish.pendown()
        finish.pensize(6)
        finish.forward(SCREEN_HEIGHT - 80)

        start = turtle.Turtle(visible=False)
        start.penup()
        start.color("white")
        start.goto(START_LINE_X, -SCREEN_HEIGHT / 2 + 40)
        start.setheading(90)
        start.pendown()
        start.pensize(3)
        start.forward(SCREEN_HEIGHT - 80)

        title = turtle.Turtle(visible=False)
        title.penup()
        title.color("white")
        title.goto(0, SCREEN_HEIGHT / 2 - 60)
        title.write("Turtle Grand Prix", align="center", font=("Verdana", 24, "bold"))

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.player.move_forward, "w")
        self.screen.onkey(self.player.move_backward, "s")
        self.screen.onkey(self.reset_game, "r")
        self.screen.onkey(self.quit_game, "q")

    def reset_game(self):
        self.running = True
        self.winner = None
        self.message.clear()
        self.generate_ai_speeds()
        for racer in self.racers:
            racer.reset(START_LINE_X, racer.turtle.ycor(), racer.speed)
        self.update_status()
        self.screen.update()
        if not hasattr(self, "started"):
            self.started = True
            self.update()

    def generate_ai_speeds(self):
        for ai in self.ai_racers:
            base_speed = random.uniform(AI_MIN_SPEED, AI_MAX_SPEED)
            ai.speed = base_speed + (self.level - 1) * LEVEL_SPEED_BOOST
        self.player.speed = PLAYER_SPEED

    def update_status(self):
        self.status.clear()
        self.status.goto(-SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 - 80)
        self.status.write(
            f"Level {self.level}  |  Player speed: {PLAYER_SPEED}  |  AI base range: {AI_MIN_SPEED:.1f}-{AI_MAX_SPEED:.1f}",
            align="left",
            font=("Arial", 12, "normal"),
        )
        self.status.goto(-SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 - 105)
        self.status.write("W/S to move your turtle. R to restart. Q to quit.", align="left", font=("Arial", 12, "normal"))

    def display_message(self, text, delay=1500):
        self.message.clear()
        self.message.goto(0, -SCREEN_HEIGHT / 2 + 40)
        self.message.color("white")
        self.message.write(text, align="center", font=("Arial", 14, "bold"))
        if delay:
            self.screen.ontimer(self.message.clear, delay)

    def display_winner(self, text):
        self.message.clear()
        self.message.goto(0, 0)
        self.message.color("yellow")
        self.message.write(text + " Press R to play again.", align="center", font=("Arial", 18, "bold"))

    def update(self):
        if self.running and not self.winner:
            for ai in self.ai_racers:
                if not ai.is_finished():
                    ai.move_auto()
                    ai.draw_label()
            self.player.draw_label()
            self.check_finish_line()
            self.screen.update()
            self.screen.ontimer(self.update, 50)

    def check_finish_line(self):
        finished = [r for r in self.racers if r.is_finished()]
        if finished:
            self.winner = max(finished, key=lambda racer: racer.turtle.xcor())
            self.running = False
            if self.winner.is_player:
                self.display_winner(f"You won Level {self.level}!")
                self.level += 1
                self.screen.ontimer(self.reset_game, 2500)
            else:
                self.display_winner(f"{self.winner.name} won the race.")

    def quit_game(self):
        self.running = False
        self.screen.bye()

    def start(self):
        self.reset_game()
        self.screen.mainloop()


if __name__ == "__main__":
    game = RacingGame()
    game.start()
