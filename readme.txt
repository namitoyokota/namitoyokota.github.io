## blur images

`convert -blur 0x500 ./image.jpg ../images-compressed/image.jpg`
`for FILE in *; do convert -blur 0x500 ./$FILE ../images-compressed/$FILE; done`

## compress images
`optimizt /path_to_image.jpg`