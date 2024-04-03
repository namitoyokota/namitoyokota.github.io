![My API website preview](https://api.namitoyokota.com/assets/og-images/api.png)

# api.namitoyokota.com

-   **Deployment**: [GitHub](https://github.com)
-   **Format**: [JSON](https://www.json.org/json-en.html)
-   **Documentation**: [Markdown](https://commonmark.org/)

## Endpoints

-   [https://api.namitoyokota.com/images.json](./images.json) - List of images for the photography portfolio.
-   [https://api.namitoyokota.com/projects.json](./projects.json) - List of side projects.
-   [https://api.namitoyokota.com/socials.json](./socials.json) - List of social medias.
-   [https://api.namitoyokota.com/sounds.json](./sounds.json) - List of sound effects.
-   [https://api.namitoyokota.com/utils.json](./utils.json) - Utility object data like logos, meta images, and loading icons.

## Resources

-   Sounds: [Submit](https://opengameart.org/content/menu-selection-click), [Complete](https://opengameart.org/content/completion-sound)
-   Icons: [Vecteezy](https://www.vecteezy.com/)

## Contribution Guides

### Blug Images

```shell
$ convert -blur 0x500 ./image.jpg ../images-compressed/image.jpg
$ for FILE in *; do convert -blur 0x500 ./$FILE ../images-compressed/$FILE; done
```

### Compress Images

```shell
$ optimizt /path_to_image.jpg
```

### Convert JPG to WEBP

```$
$ cwebp -q 50 ./image.jpg -o ./image.webp
$ for FILE in *; do cwebp -q 50 ./$FILE -o ${FILE%%.*}.webp; done
```
