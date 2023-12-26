import subprocess
import os

def add_border_to_image(image, output, left, right, top, bottom, border_color):
    command = [
        'ffmpeg', '-y', '-i', image,
        '-vf', f'pad=width=in_w+{left}+{right}:height=in_h+{top}+{bottom}:x={left}:y={top}:color={border_color}',
        output
    ]
    subprocess.run(command)

def cleanup(images_with_borders):
    for image in images_with_borders:
        os.remove(image)

def combine_images_2x2(images, output, border_color):
    borders=[(20, 10, 20, 10), (10, 20, 20, 10), (20, 10, 10, 20), (10, 20, 10, 20)]
    #images = [image1, image2, image3, image4]
    images_with_borders = []

    for i, image in enumerate(images):
        output_image = f"border_{i}.jpg"
        left, right, top, bottom = borders[i]
        add_border_to_image(image, output_image, left, right, top, bottom, border_color)
        images_with_borders.append(output_image)

    command = ['ffmpeg', '-y', '-i', images_with_borders[0], '-i', images_with_borders[1], '-i', images_with_borders[2], '-i', images_with_borders[3], '-filter_complex', "[0:v][1:v]hstack[top];[2:v][3:v]hstack[bottom];[top][bottom]vstack", output]
    subprocess.run(command)

    #cleanup(images_with_borders)

def combine_images_1x4(images, output, border_color):
    borders=[(20, 20, 20, 10), (20, 20, 10, 10), (20, 20, 10, 10), (20, 20, 10, 20)]
    #images = [image1, image2, image3, image4]
    images_with_borders = []

    for i, image in enumerate(images):
        output_image = f"border_{i}.jpg"
        left, right, top, bottom = borders[i]
        add_border_to_image(image, output_image, left, right, top, bottom, border_color)
        images_with_borders.append(output_image)

    command = ['ffmpeg', '-y', '-i', images_with_borders[0], '-i', images_with_borders[1], '-i', images_with_borders[2], '-i', images_with_borders[3], '-filter_complex', "[0:v][1:v][2:v][3:v]vstack=inputs=4", output]
    subprocess.run(command)

    cleanup(images_with_borders)

def combine_images_4x1(images, output, border_color):
    
    borders=[(20, 10, 20, 20), (10, 10, 20, 20), (10, 10, 20, 20), (10, 20, 20, 20)]
    #images = [image1, image2, image3, image4]
    images_with_borders = []

    for i, image in enumerate(images):
        output_image = f"border_{i}.jpg"
        left, right, top, bottom = borders[i]
        add_border_to_image(image, output_image, left, right, top, bottom, border_color)
        images_with_borders.append(output_image)

    command = ['ffmpeg', '-y', '-i', images_with_borders[0], '-i', images_with_borders[1], '-i', images_with_borders[2], '-i', images_with_borders[3], '-filter_complex', "[0:v][1:v][2:v][3:v]hstack=inputs=4", output]
    subprocess.run(command)

    cleanup(images_with_borders)
