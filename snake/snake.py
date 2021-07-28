import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))

def lvl(lvl1, lvl2, lvl3):
    if lvl1 == 1:
        x = open('lvl1.txt', 'r')
    if lvl2 == 1:
        x = open('lvl2.txt', 'r')
    if lvl3 == 1:
        x = open('lvl3.txt', 'r')

    a = x.readlines()
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "#":
                pygame.draw.rect(screen, (0, 0, 255), (i*10, j*10, 10, 10))


class Food:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

    def get(self, lvl1, lvl2, lvl3):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

        if lvl1 == 1:
            x = open('lvl1.txt', 'r')
        if lvl2 == 1:
            x = open('lvl2.txt', 'r')
        if lvl3 == 1:
            x = open('lvl3.txt', 'r')

        a = x.readlines()
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#":
                    if i*10 - 10 <= self.x <= i*10 + 10 and j*10 - 10 <= self.y <= j*10 + 10:
                        return False
        return True

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))

class Snake:
    def __init__(self, color, dx = 0, dy = 1, elements = [[random.randint(100, 690), random.randint(100, 490)]]):
        self.size = len(elements)
        self.elements = elements
        self.dx = dx
        self.dy = dy
        self.is_add = False
        self.speed = 20
        self.color = color
        self.radius = 10
        self.end = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, self.color, element, self.radius)

    def wall(self):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if 800 <= x <= 0 or 600 <= y <= 0:
            return False
        return True

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx - 10 <= x <= foodx + 20 and foody - 10 <= y <= foody + 20:
            return True
        return False

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.speed % 3 == 0:
            self.speed += 5

    def lose(self, lvl1, lvl2, lvl3):
        for i in range(1, self.size - 1):
            if self.elements[0][0] == self.elements[i][0] and self.elements[0][1] == self.elements[i][1]:
                return False

        if lvl1 == 1:
            x = open('lvl1.txt', 'r')
        if lvl2 == 1:
            x = open('lvl2.txt', 'r')
        if lvl3 == 1:
            x = open('lvl3.txt', 'r')

        a = x.readlines()
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "#" and i*10 - 10 <= self.elements[0][0] <= i*10 + 10 and j*10 - 10 <= self.elements[0][1] <= j*10 + 10:
                    return False

        return True

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx*10
        self.elements[0][1] += self.dy*10

        for i in range(1, len(self.elements)-1):
            if self.elements[i][0] == self.elements[0][0] and self.elements[i][1] == self.elements[0][1]:
                self.end = False

        if 800 <= self.elements[0][0] <= 0 or 600 <= self.elements[0][1] <= 0:
            self.end = False

def op(lvl1, lvl2, lvl3):
    font_small = pygame.font.SysFont("Verdana", 20)
    snake = Snake((0, 255, 0))
    food = Food()

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(snake.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0

        snake.move()
        if snake.eat(food.x, food.y):
            snake.is_add = True
            q = food.get(lvl1, lvl2, lvl3)
            while not q:
                q = food.get(lvl1, lvl2, lvl3)
        screen.fill((0, 0, 0))
        snake.draw()
        food.draw()
        lvl(lvl1, lvl2, lvl3)
        sc = font_small.render(str(snake.size), True, (0, 0, 255))
        screen.blit(sc, (760, 15))
        pygame.display.flip()
        if not snake.lose(lvl1, lvl2, lvl3):
            time.sleep(1)
            running = False

    return False

def tp(lvl1, lvl2, lvl3):
    font_small = pygame.font.SysFont("Verdana", 20)
    snake = Snake((0, 255, 0))
    snake2 = Snake((12, 200, 120))
    food = Food()

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(snake.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_w and snake2.dy != 1:
                    snake2.dx = 0
                    snake2.dy = -1
                if event.key == pygame.K_s and snake2.dy != -1:
                    snake2.dx = 0
                    snake2.dy = 1
                if event.key == pygame.K_d and snake2.dx != -1:
                    snake2.dx = 1
                    snake2.dy = 0
                if event.key == pygame.K_a and snake2.dx != 1:
                    snake2.dx = -1
                    snake2.dy = 0

        snake.move()
        snake2.move()
        if snake.eat(food.x, food.y):
            snake.is_add = True
            q = food.get(lvl1, lvl2, lvl3)
            while not q:
                q = food.get(lvl1, lvl2, lvl3)
        if snake2.eat(food.x, food.y):
            snake2.is_add = True
            q = food.get(lvl1, lvl2, lvl3)
            while not q:
                q = food.get(lvl1, lvl2, lvl3)
        screen.fill((0, 0, 0))
        snake.draw()
        snake2.draw()
        food.draw()
        lvl(lvl1, lvl2, lvl3)
        sc = font_small.render(str(snake.size), True, (0, 0, 255))
        sc2 = font_small.render(str(snake2.size), True, (0, 0, 255))
        screen.blit(sc, (755, 15))
        screen.blit(sc2, (15, 15))
        pygame.display.flip()
        if not snake.lose(lvl1, lvl2, lvl3):
            time.sleep(1)
            running = False
        if not snake2.lose(lvl1, lvl2, lvl3):
            time.sleep(1)
            running = False

    return False

def main():
    running = True
    start = False
    lvl1 = 1
    lvl2 = 0
    lvl3 = 0
    p1 = 1
    p2 = 0
    font = pygame.font.SysFont("Verdana", 60)
    while running:
        screen.fill((23, 45, 155))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= pos[0] <= 200 and 100 <= pos[1] <= 200:
                    lvl2 = 0
                    lvl1 = 1
                    lvl3 = 0
                if 300 <= pos[0] <= 400 and 100 <= pos[1] <= 200:
                    lvl2 = 1
                    lvl1 = 0
                    lvl3 = 0
                if 500 <= pos[0] <= 600 and 100 <= pos[1] <= 200:
                    lvl2 = 0
                    lvl1 = 0
                    lvl3 = 1
                if 200 <= pos[0] <= 300 and 300 <= pos[1] <= 400:
                    p1 = 1
                    p2 = 0
                if 400 <= pos[0] <= 500 and 300 <= pos[1] <= 400:
                    p1 = 0
                    p2 = 1
                if 300 <= pos[0] <= 500 and 450 <= pos[1] <= 550:
                    start = True

        pygame.draw.rect(screen, (255, 255, 255), (300, 450, 200, 100))
        lvl = font.render("START", True, (0, 0, 0))
        screen.blit(lvl, (305, 460))

        if lvl1 == 1:
            pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))
            lvl = font.render("lvl1", True, (0, 0, 0))
            screen.blit(lvl, (100, 110))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 100))
            lvl = font.render("lvl1", True, (255, 255, 255))
            screen.blit(lvl, (100, 110))

        if lvl2 == 1:
            pygame.draw.rect(screen, (255, 255, 255), (300, 100, 100, 100))
            lvl = font.render("lvl2", True, (0, 0, 0))
            screen.blit(lvl, (300, 110))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (300, 100, 100, 100))
            lvl = font.render("lvl2", True, (255, 255, 255))
            screen.blit(lvl, (300, 110))

        if lvl3 == 1:
            pygame.draw.rect(screen, (255, 255, 255), (500, 100, 100, 100))
            lvl = font.render("lvl3", True, (0, 0, 0))
            screen.blit(lvl, (500, 110))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (500, 100, 100, 100))
            lvl = font.render("lvl3", True, (255, 255, 255))
            screen.blit(lvl, (500, 110))

        #-------------------------------------
        if p1 == 1:
            pygame.draw.rect(screen, (255, 255, 255), (200, 300, 100, 100))
            lvl = font.render("1P", True, (0, 0, 0))
            screen.blit(lvl, (215, 310))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (200, 300, 100, 100))
            lvl = font.render("1P", True, (255, 255, 255))
            screen.blit(lvl, (215, 310))

        if p2 == 1:
            pygame.draw.rect(screen, (255, 255, 255), (400, 300, 100, 100))
            lvl = font.render("2P", True, (0, 0, 0))
            screen.blit(lvl, (415, 310))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (400, 300, 100, 100))
            lvl = font.render("2P", True, (255, 255, 255))
            screen.blit(lvl, (415, 310))

        #-------------------------------------
        if start and p1 == 1:
            start = op(lvl1, lvl2, lvl3)
        elif start and p2 == 1:
            start = tp(lvl1, lvl2, lvl3)

        pygame.display.flip()
    pygame.quit()

main()