every image should have a blurred version with the same filename in the /images-compressed directory. to do this, run `convert -blur 0x500 ./image.jpg ../images-compressed/image.jpg`

you can also bulk compress using the following command: `for FILE in *; do convert -blur 0x500 ./$FILE ../images-compressed/$FILE; done`