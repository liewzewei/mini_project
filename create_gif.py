import imageio
import glob

images = glob.glob("./images/*.jpg")
images = sorted(images,key= lambda x : float((x[17:])[:-4]))[:3000]
# images = list(map(lambda x : float((x[17:])[:-4]),images))
# print(images[:20])

with imageio.get_writer('movie.gif', mode='I') as writer:
    print("Creating gif")
    for filename in images:
        print(f"Adding {filename}")
        image = imageio.imread(filename)
        writer.append_data(image)
    print("Gif created")