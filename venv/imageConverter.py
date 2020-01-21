from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('userInterface.html')


@app.route('/', methods = ['GET', 'POST'])
def converter():
    if request.method == 'POST':
        image = request.files['fileupload']
        img1 = Image.open(image)
        img = np.array(img1)
        m = len(img)
        n = len(img[0])
        grayscale = np.zeros([m,n])

        for i in range(m):
            for j in range(n):
                grayscale[i][j] = (0.2126 * img[i][j][0] + 0.7152 * img[i][j][1] + 0.0722 * img[i][j][2])

        image1 = Image.fromarray(grayscale)
        final_image = image1.convert("L")
        final_image.save('grayscale.jpg')
        return 'Find the file at the same location where it was uploaded as grayscale.jpg'

if __name__ == '__main__':
    app.run(debug=True)





