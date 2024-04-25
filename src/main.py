import pygame
import random 
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")
rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png") 
font = pygame.font.SysFont("Arial", 24)

number = 20 
rocks = []
for i in range(number):
    rocks.append([-100,height])

clock = pygame.time.Clock()

robot_x = (width/2)-(robot.get_width()/2)
robot_y = height-robot.get_height()

to_right = False
to_left = False

score = 0

robot_speed = 5
asteroid_speed = 1

game_state = "active"

while True:
    if game_state == "active":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False

        if to_right and robot_x+robot.get_width() < 640:
            robot_x += robot_speed
        if to_left and robot_x > 0:
            robot_x -= robot_speed

        for i in range(number):
            if rocks[i][1]+rock.get_height() < height: #robot falling
                rocks[i][1] += asteroid_speed
            elif rocks[i][0] < 0-rock.get_width() or rocks[i][0] > width: #robot start invalid
                rocks[i][0] = random.randint(0,width-rock.get_width())
                rocks[i][1] = random.randint(-1000,-100)
            
            if ((robot_x+10<=rocks[i][0]+rock.get_width() and robot_x+robot.get_width()-10>=rocks[i][0]) or (robot_x+10<=rocks[i][0]+rock.get_width() and robot_x+robot.get_width()-10>=rocks[i][0])) and (height > rocks[i][1] >= height-robot.get_height()-30):
                score += 1            
                rocks[i][0] = random.randint(0,width-rock.get_width())
                rocks[i][1] = random.randint(-1000,-100)
                
            if rocks[i][1] + rock.get_height() >= height:
                game_state = "failed"

        screen.fill((0, 0, 0))

        for i in range(number):
            screen.blit(rock,(rocks[i][0],rocks[i][1]))

        text = font.render("Points: " + str(score), True, (255, 0, 0))
        screen.blit(text, (width-150, 10))

        screen.blit(robot,(robot_x,robot_y))
        pygame.display.flip()

        clock.tick(60)
        
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 50)
        if score > 1:
            text = font.render(f"You scored {str(score)} points!",True, (0,0,0))
            screen.blit(text,(130,200))
        elif score == 1:
            text = font.render(f"You scored {str(score)} point!",True, (0,0,0))
            screen.blit(text,(130,200))                        
        elif score == 0:
            text = font.render(f"lol",True, (0,0,0))                        
            screen.blit(text,(290,200))  
        pygame.display.flip()
