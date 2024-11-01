import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Python vs Snake II')

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True