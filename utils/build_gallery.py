from argparse import ArgumentParser
from pathlib import Path


# background image
# bg_image = "assets/images/6-sparkling-lights-overlay-effects-real-particles_vjmlvqhqe__F0000.png
# bg_image2 = f"{bg_image}"
bg_image = ""
bg_image2 = ""
image_formats = (".jpg", ".JPG", ".png", ".PNG", ".jpeg", ".JPEG")


def get_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--images', help='Image folder name. Has to be located in /assets/images/', default="img_gallery", type=str)
    parser.add_argument('-g', '--gallery', help='Gallery file name', default="pgallery.md", type=str)
    parser.add_argument('-t', '--title', help='Page title for the gallery', default="Gallery", type=str)
    parser.add_argument('-e', '--excerpt', help='Page description', default="Image Gallery", type=str)
    return parser.parse_args()


def built_md(gallery_name, images_folder, title, excerpt):
    # writes a markdown file
    with open(Path(".") / ".." / "_photo_gallery" / gallery_name, "w") as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'excerpt: {excerpt}\n')
        f.write('header:\n')
        f.write(f'   image: {bg_image2}\n')
        f.write(f'   teaser: {bg_image}\n')
        f.write('sidebar:\n')
        f.write('   - title:\n')
        f.write('     image:\n')
        f.write('     image_alt:\n')
        f.write('     text:\n')
        f.write('   - title:\n')
        f.write('     text:\n')
        f.write('gallery:\n')
        urls, imgs = get_imgs(images_folder)
        i = 1
        for u, t in zip(urls, imgs):
            f.write(f'   - url: {u}\n')
            f.write(f'     image_path: {t}\n')
            f.write(f'     alt: "placeholder image {i}"\n')
            i += 1
        f.write('---\n')
        f.write('{% include gallery caption="" %}')


def get_imgs(images_folder):
    # returns image file informations
    path = Path(".") / ".." / "assets" / "images" / images_folder
    img_str = f'assets/images/{images_folder}/'
    url_str = f'/{img_str}'
    urls, imgs = [], []
    for img in path.iterdir():
        if img.name.endswith(image_formats):
            urls.append(url_str + img.name)
            imgs.append(img_str + img.name)
    return urls, imgs    


if __name__ == "__main__":
    args = get_args()
    built_md(args.gallery, args.images, args.title, args.excerpt)
