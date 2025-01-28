# ==============================================
#   * 2D Sprite adventure game using pygame.
#   * The world is procedurally generated with
#   perlin noise and will keep generating.
# ==============================================
#   * Author: Mikey
#   * Date: 1/25/2025
# ==============================================

import pygame
import sys
import noise
import random

pygame.init()

# ====Constants====
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 32
FPS = 60
CHUNK_SIZE = 16

# ====Colors====
BLACK = (0, 0, 0)

# ====Screen====
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure")
clock = pygame.time.Clock()

# ====Textures====
textures = {
    # TODO: Add textures to project
}
