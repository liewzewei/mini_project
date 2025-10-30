import imageio
import glob

images = glob.glob("./images/*.jpg")

with imageio.get_writer('movie.gif', mode='I') as writer:
    for filename in glob:
        image = imageio.imread(filename)
        writer.append_data(image)