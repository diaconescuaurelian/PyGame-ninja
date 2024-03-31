import pygame
import os

BASE_IMG_PATH = 'PyGame-ninja/data/images/'

def load_image(path):
    #We add the path of a specific image to the base path
    #We use .convert() on the image to convert the internal representation of the image in pygame and make it more efficient for rendering
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    #the black color becomes transparent
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images