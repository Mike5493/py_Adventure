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
MINIMAP_SCALE = 0.1

# ====Colors====
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# ====Screen====
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure")
clock = pygame.time.Clock()

# ====Textures====
textures = {
    # TODO: Add textures to project
}

# Load player texture
player_texture = pygame.image.load("player.png").convert()
player_rect = player_texture.get_rect()
player_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


def generate_chunk(chunk_x, chunk_y, scale):
    chunk = []
    for y in range(CHUNK_SIZE):
        row = []
        for x in range(CHUNK_SIZE):
            world_x = chunk_x * CHUNK_SIZE + x
            world_y = chunk_y * CHUNK_SIZE + y
            height_value = noise.pnoise2(world_x / scale, world_y / scale,
                                         octaves=6, persistence=0.5, lacunarity=2.0,
                                         repeatx=1024, repeaty=1024, base=42)
            if height_value < -0.05:
                row.append(BLUE)    # Water
            elif height_value < 0.2:
                row.append(GREEN)   # Grass
            else:
                row.append(BROWN)   # Mountain
        chunk.append(row)
    return chunk


def draw_chunk(screen, chunk, chunk_x, chunk_y, camera_offset):
    for y in range(CHUNK_SIZE):
        for x in range(CHUNK_SIZE):
            color = chunk[y][x]
            screen_x = (chunk_x * CHUNK_SIZE + x) * \
                TILE_SIZE - camera_offset[0]
            screen_y = (chunk_y * CHUNK_SIZE + y) * \
                TILE_SIZE - camera_offset[1]
            pygame.draw.rect(
                screen, color, (screen_x, screen_y, TILE_SIZE, TILE_SIZE,))


def draw_minimap(screen, loaded_chunks, player_rect, minimap_size):
    minimap_surface = pygame.Surface(minimap_size)
    minimap_surface.fill(BLACK)

    for (chunk_x, chunk_y), chunk in loaded_chunks.items():
        for y in range(CHUNK_SIZE):
            for x in range(CHUNK_SIZE):
                color = chunk[y][x]
                minimap_x = (chunk_x * CHUNK_SIZE + x) * MINIMAP_SCALE
                minimap_y = (chunk_y * CHUNK_SIZE + y) * MINIMAP_SCALE
                pygame.draw.rect(
                    minimap_surface, color, (minimap_x, minimap_y, MINIMAP_SCALE, MINIMAP_SCALE))

    # ==== Draw Player on minimap ====
    player_minimap_x = player_rect.x * MINIMAP_SCALE / TILE_SIZE
    player_minimap_y = player_rect.y * MINIMAP_SCALE / TILE_SIZE
    pygame.draw.rect(minimap_surface, WHITE, (player_minimap_x, player_minimap_y,
                                              MINIMAP_SCALE, MINIMAP_SCALE))

    screen.blit(minimap_surface, (SCREEN_WIDTH - minimap_size[0] - 10, 10))


def main():
    scale = 100
    loaded_chunks = {}
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_rect.y -= 5
        if keys[pygame.K_s]:
            player_rect.y += 5
        if keys[pygame.K_a]:
            player_rect.x -= 5
        if keys[pygame.K_d]:
            player_rect.x += 5

        # ===== Calculate camera offset ====
        camera_offset = (player_rect.x - SCREEN_WIDTH // 2,
                         player_rect.y - SCREEN_HEIGHT // 2)

        # ==== Determine chunk loading ====
        player_chunk_x = player_rect.x // (CHUNK_SIZE * TILE_SIZE)
        player_chunk_y = player_rect.y // (CHUNK_SIZE * TILE_SIZE)

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                chunk_x = player_chunk_x + dx
                chunk_y = player_chunk_y + dy
                if (chunk_x, chunk_y) not in loaded_chunks:
                    loaded_chunks[(chunk_x, chunk_y)] = generate_chunk(
                        chunk_x, chunk_y, scale)

        screen.fill(BLACK)
        for (chunk_x, chunk_y), chunk in loaded_chunks.items():
            draw_chunk(screen, chunk, chunk_x, chunk_y, camera_offset)
        screen.blit(player_texture, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # ==== Draw Minimap ====
        minimap_size = (int(SCREEN_WIDTH * MINIMAP_SCALE),
                        int(SCREEN_HEIGHT * MINIMAP_SCALE))
        draw_minimap(screen, loaded_chunks, player_rect, minimap_size)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
