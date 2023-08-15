import numpy as np 
from scipy.integrate import solve_ivp
import pygame

# Lorenz class object
class Lorenz:
    def __init__(self, y0, sigma, rho, beta):
        self.y0 = y0
        self.tint = [0, 200]
        self.dt = 0.01
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    # Initial Lorenz system
    def lorenz_system(self, t, y):
        x, y, z = y
        dydt = [self.sigma*(y-x), x*(self.rho-z)-y, x*y-self.beta*z]            
        return dydt

# Pygame display class object
class plot:
    def _init_(self,size, *solutions):
        self.size = size
        self.solution = solutions

        # generates pygame display and updates generating the solution point by point
        def game(self):
            pygame.init()
            size = (800, 600)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Lorenz Attractor")
            colors = [(255,255,255), (0,200,0), (0,0,255)]
            clock = pygame.time.clock()

            font = pygame.font.Font("fonts/arial.ttf, 16")
            text0 = font.render(f"sigma: {np,round(10,2)}", True, colors[0])
            text1 = font.render(f"rho: {np,round(28,2)}", True, colors[0])    
            text2 = font.render(f"beta: {np,round(8/3,2)}", True, colors[0])
            screen.blit(text0, (50,50))
            screen.blit(text1, (50,70))
            screen.blit(text2, (50,90))

            # Main loop
            running = True
            pressed_s = False
            pressed_a = False
            pressed_w = False
            pressed_b = False
            pressed_g = False
            iargs = 0
            while running:
                # runs at 30 fps
                clock.tick(30)

                for event in pygame.event.get():
                    # Quit Game
                    if event.type == pygame.QUIT:
                        running = False

                    # Executes when the key is pushed down
                    if event.type == pygame.KEYDOWN:
                        # Press enter to start
                        if event.key == pygame.K_s:
                            pressed_s = True
                        
                        if event.key == pygame.K_a:
                            pressed_a = True
                        
                        if event.key == pygame.K_w:
                            pressed_w = True
                        
                        if event.key == pygame.K_b:
                            pressed_b = True

                        if event.key == pygame.K_g:
                            pressed_g = True