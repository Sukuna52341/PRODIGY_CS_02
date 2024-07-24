from PIL import Image
import random
import os

def swap_pixels(image, key):
    pixels = list(image.getdata())
    width, height = image.size
    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    
    new_pixels = [None] * len(pixels)
    for i, idx in enumerate(indices):
        new_pixels[i] = pixels[idx]
    
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(new_pixels)
    return encrypted_image

def apply_math_operation(image, key, operation):
    pixels = list(image.getdata())
    new_pixels = []
    for pixel in pixels:
        if operation == 'add':
            new_pixel = tuple((channel + key) % 256 for channel in pixel)
        elif operation == 'subtract':
            new_pixel = tuple((channel - key) % 256 for channel in pixel)
        new_pixels.append(new_pixel)
    
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(new_pixels)
    return encrypted_image

def main():
    print()
    print('IMAGE ENCRYPTION TOOL')
    print()
    print('Do you want to encrypt or decrypt?')
    user_input = input('e/d: ').lower()

    if user_input not in ['e', 'd']:
        print('Invalid option')
        return

    file_path = input('Enter the path of the image file: ')
    if not os.path.isfile(file_path):
        print('The path provided is not a file.')
        return

    try:
        image = Image.open(file_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    print('Choose an operation:')
    print('1. Swap pixels')
    print('2. Apply mathematical operation')
    operation_input = input('1/2: ')

    if operation_input not in ['1', '2']:
        print('Invalid option')
        return

    try:
        key = int(input('Enter the key (integer): '))
    except ValueError:
        print('Invalid key. Please enter an integer.')
        return

    if operation_input == '1':
        result_image = swap_pixels(image, key)
    elif operation_input == '2':
        if user_input == 'e':
            result_image = apply_math_operation(image, key, 'add')
        else:
            result_image = apply_math_operation(image, key, 'subtract')

    output_path = input('Enter the output file path: ')
    try:
        result_image.save(output_path)
        print(f'Result saved to {output_path}')
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == '__main__':
    main()