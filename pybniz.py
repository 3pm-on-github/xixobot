import pygame
import numpy as np
import math
t = 0
pygame.init()
canvas = pygame.display.set_mode((256, 256))
canvas.fill((0, 0, 0))


def func(x, y):
    # editable code:
    u = x - 128
    v = y - 128
    theta = math.atan2(v, u) / math.tau * 256
    radius = math.hypot(u, v)+1
    tr = (t % 8)*32
    r = int(theta*8 + tr) ^ int(65536/radius + tr)
    g = r
    b = g
    # end of editable code
    return 65536*(r%256) + 256*(g%256) + (b%256)


vfunc = np.vectorize(func)

run = True
while run:
    px = np.arange(256)
    py = np.arange(256)
    px, py = np.meshgrid(py, px)
    array = vfunc(px, py)
    pygame.surfarray.blit_array(canvas, array)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    t += 1
# by ztunedd