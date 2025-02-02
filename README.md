# chromify

Chromify is a deep learning project that takes a grayscale image as input and generates a colorized version as output.

## How to run the project locally
Run this commands in the root folder to build the docker image
```sh
docker build -f docker/frontend.dockerfile . -t frontend:latest
docker build -f docker/api.dockerfile . -t api:latest
```
After building the image you can run the container with these commands in two different terminal
```sh
docker run -p 8080:8080 --rm -it api:latest
```
```sh
docker run -p 5137:5137 --rm -it frontend:latest
```
After running the containers access this page to try out: http://localhost:5137/
## Description

Many times, when we check history, the information and documentation available comes accompanied by images. Even though it is true that these images are capable of giving us a better perception of how things were in that specific moment in time there is a very important thing missing the further back in history we look: color.
With our project our purpose is to take black and white images and bring them back to life colorizing them.
The frameworks we expect to use are PyTorch, some pretrained model fit for the task that we might find in hugging face.
Our initial dataset is this one named [Image Colorization](https://www.kaggle.com/datasets/seungjunleeofficial/image-colorization). It has a size of 3.13GB and it is composed of two folders with the 118k original images and their correspondent grayscaled versions.
There are multiple models that can be fit for this task, but all of them have their pros and cons. Our main options are:
1. Encoder-decoder: Simple and effective with a simple implementation. It is not computationally heavy but struggles producing realistic high-quality outputs.
1. U-Net: Takes advantage of the skip connections and combines low- and high-level features with them. Its outputs are sharper than those of an encoder-decoder. Nonetheless, it's more complex, computationally heavy, and its results could still be improved.
1. Generative Adversarial Network (GAN): gives the best results due the use of the adversarial loss and the accuracy provided by the use of the discriminator. It is more difficult to train and computationally heavy. It also requires big datasets.
In case of choosing GAN we would use one of two specialized frameworks for them: Pix2Pix or CycleGAN.

Out of the three, we have chosen U-Net due being the most balanced option. It gives the best results when compared to the computational cost and implementation cost.

Update: the implementation of a U-Net from scratch, or using existing models from huggingface, is not straightforward. After many unsuccessful tries, we ended up finding ourselves delvening on the research process, and we found the [following implementation](https://github.com/mberkay0/image-colorization) by the user mberkay0. His work consists of the combination of a U-Net with a GAN. He also wrote an article that can be read [here](https://towardsdatascience.com/colorizing-black-white-images-with-u-net-and-conditional-gan-a-tutorial-81b2df111cd8).  
His code was adapted to our data and our necessities.

## Project structure

The directory structure of the project looks like this:
```txt
├── .github/                  # Github actions and dependabot
│   ├── dependabot.yaml
│   └── workflows/
│       └── tests.yaml
├── configs/                  # Configuration files
├── data/                     # Data directory
│   ├── processed
│   └── raw
├── dockerfiles/              # Dockerfiles
│   ├── api.Dockerfile
│   └── train.Dockerfile
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── models/                   # Trained models
├── notebooks/                # Jupyter notebooks
├── reports/                  # Reports
│   └── figures/
├── src/                      # Source code
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── data.py
│   │   ├── evaluate.py
│   │   ├── models.py
│   │   ├── train.py
│   │   └── visualize.py
└── tests/                    # Tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_data.py
│   └── test_model.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── pyproject.toml            # Python project file
├── README.md                 # Project README
├── requirements.txt          # Project requirements
├── requirements_dev.txt      # Development requirements
└── tasks.py                  # Project tasks
```


Created using [mlops_template](https://github.com/SkafteNicki/mlops_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting
started with Machine Learning Operations (MLOps).
