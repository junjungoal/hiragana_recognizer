import cStringIO
import argparse
import commands
from PIL import Image


def load_data(args):
    image_list = commands.getoutput("ls %s/* | xargs -n 1 basename" %args.data_dir).split("\n")
    images = []
    for image_path in image_list:
        image_file = cStringIO.StringIO(open("%s/1900_753325_0060.png" % args.data_dir, "rb").read())
        image = Image.open(image_file)
        images.append(image)
    return images

parser = argparse.ArgumentParser()
parser.add_argument("--data_dir", type=str, default="data/U3042")
parser.add_argument("--gpu", type=int, default=-1)

args = parser.parse_args()

images = load_data(args)

