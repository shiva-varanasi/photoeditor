import streamlit as st
from PIL import Image
from io import BytesIO


st.header(":blue[Convert Image to Black and White]")
st.caption(':blue[Convert your color photo to black and white and give it a retro look]')

image_to_process = st.file_uploader('Upload image')


if image_to_process:
    # create a pillow image instance
    img = Image.open(image_to_process)

    # convert the pillow image into gray scale
    gray_img = img.convert("L")

    # show the gray scale image on the screen
    st.image(gray_img)
    # converting a pillow image instance to bytes
    buf = BytesIO()
    gray_img.save(buf, format='JPEG')
    byte_gray_img = buf.getvalue()

    # Render the download image button to download the gray scale image
    button = st.download_button(label='Download image', data=byte_gray_img,
                                file_name='grayscale.jpeg', mime='image/jpeg')



