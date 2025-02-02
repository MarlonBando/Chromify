# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

Where you instead should add your answers. Any other changes may have unwanted consequences when your report is
auto-generated at the end of the course. For questions where you are asked to include images, start by adding the image
to the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

Will generate a `.html` page of your report. After the deadline for answering this template, we will auto-scrape
everything in this `reports` folder and then use this utility to generate a `.html` page that will be your serve
as your final hand-in.

Running

```bash
python report.py check
```

Will check your answers in this template against the constraints listed for each question e.g. is your answer too
short, too long, or have you included an image when asked. For both functions to work you mustn't rename anything.
The script has two dependencies that can be installed with

```bash
pip install typer markdown
```

## Overall project checklist

The checklist is *exhaustive* which means that it includes everything that you could do on the project included in the
curriculum in this course. Therefore, we do not expect at all that you have checked all boxes at the end of the project.
The parenthesis at the end indicates what module the bullet point is related to. Please be honest in your answers, we
will check the repositories and the code to verify your answers.

### Week 1

* [] Create a git repository (M5)
* [x] Make sure that all team members have write access to the GitHub repository (M5)
* [x] Create a dedicated environment for you project to keep track of your packages (M2)
* [x] Create the initial file structure using cookiecutter with an appropriate template (M6)
* [x] Fill out the `data.py` file such that it downloads whatever data you need and preprocesses it (if necessary) (M6)
* [x] Add a model to `model.py` and a training procedure to `train.py` and get that running (M6)
* [x] Remember to fill out the `requirements.txt` and `requirements_dev.txt` file with whatever dependencies that you
    are using (M2+M6)
* [x] Remember to comply with good coding practices (`pep8`) while doing the project (M7)
* [x] Do a bit of code typing and remember to document essential parts of your code (M7)
* [x] Setup version control for your data or part of your data (M8)
* [x] Add command line interfaces and project commands to your code where it makes sense (M9)
* [x] Construct one or multiple docker files for your code (M10)
* [x] Build the docker files locally and make sure they work as intended (M10)
* [ ] Write one or multiple configurations files for your experiments (M11)
* [ ] Used Hydra to load the configurations and manage your hyperparameters (M11)
* [ ] Use profiling to optimize your code (M12)
* [ ] Use logging to log important events in your code (M14)
* [ ] Use Weights & Biases to log training progress and other important metrics/artifacts in your code (M14)
* [ ] Consider running a hyperparameter optimization sweep (M14)
* [ ] Use PyTorch-lightning (if applicable) to reduce the amount of boilerplate in your code (M15)

### Week 2

* [x] Write unit tests related to the data part of your code (M16)
* [x] Write unit tests related to model construction and or model training (M16)
* [x] Calculate the code coverage (M16)
* [x] Get some continuous integration running on the GitHub repository (M17)
* [ ] Add caching and multi-os/python/pytorch testing to your continuous integration (M17)
* [ ] Add a linting step to your continuous integration (M17)
* [ ] Add pre-commit hooks to your version control setup (M18)
* [ ] Add a continues workflow that triggers when data changes (M19)
* [ ] Add a continues workflow that triggers when changes to the model registry is made (M19)
* [x] Create a data storage in GCP Bucket for your data and link this with your data version control setup (M21)
* [x] Create a trigger workflow for automatically building your docker images (M21)
* [x] Get your model training in GCP using either the Engine or Vertex AI (M21)
* [x] Create a FastAPI application that can do inference using your model (M22)
* [x] Deploy your model in GCP using either Functions or Run as the backend (M23)
* [ ] Write API tests for your application and setup continues integration for these (M24)
* [ ] Load test your application (M24)
* [ ] Create a more specialized ML-deployment API using either ONNX or BentoML, or both (M25)
* [x] Create a frontend for your API (M26)

### Week 3

* [ ] Check how robust your model is towards data drifting (M27)
* [ ] Deploy to the cloud a drift detection API (M27)
* [ ] Instrument your API with a couple of system metrics (M28)
* [ ] Setup cloud monitoring of your instrumented application (M28)
* [ ] Create one or more alert systems in GCP to alert you if your app is not behaving correctly (M28)
* [ ] If applicable, optimize the performance of your data loading using distributed data loading (M29)
* [ ] If applicable, optimize the performance of your training pipeline by using distributed training (M30)
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed (M31)

### Extra

* [ ] Write some documentation for your application (M32)
* [ ] Publish the documentation to GitHub Pages (M32)
* [x] Revisit your initial project description. Did the project turn out as you wanted?
* [ ] Create an architectural diagram over your MLOps pipeline
* [x] Make sure all group members have an understanding about all parts of the project
* [x] Uploaded all your code to GitHub

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

74

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

*s240033, s242943, s243121*

### Question 3
> **A requirement to the project is that you include a third-party package not covered in the course. What framework**
> **did you choose to work with and did it help you complete the project?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

We used the third-party framework **Pillow (PIL)** in our project, which is a powerful library for image processing in Python. Specifically, we used its functionality to load and manipulate images, such as converting uploaded images to grayscale using `.convert("L")` and saving the processed output as a PNG file. Pillow's integration made it easy to handle various image formats and perform operations like resizing, transformation, and conversion, which were essential for preprocessing inputs and postprocessing outputs of our model.

Additionally, we leveraged the **base64** module alongside Pillow to encode the processed images into a base64 string. This was crucial for transmitting the colorized images from our API to the frontend in a lightweight and efficient manner. The simplicity and flexibility of Pillow significantly streamlined the image-handling aspect of our project, enabling us to focus more on building and deploying the API.

## Coding environment

> In the following section we are interested in learning more about you local development environment. This includes
> how you managed dependencies, the structure of your code and how you managed code quality.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Recommended answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development environment, one would have to run the following commands*
>
> Answer:

We managed dependencies using Conda for our virtual environment.
A Conda YAML fileallows us to create the environment from scratch and install necessary packages from the `requirements.txt`.
To get an exact copy of our environment, a new team member would need to:
1. Clone the project repository.
2. Run `conda env create -f environment.yml` to create the Conda environment.
3. Activate the environment using `conda activate [environment_name]`.

For requirement management, we implemented a pre-commit hook that runs `pipreqs`.
However, `pipreqs` struggles to identify the `scikit-image` package, resulting in the erroneous entry `skimage==0.0` in `requirements.txt`,
which causes errors. To address this, we added a script in the pipeline called "fix requirements," which resolves any unresolved imports by `pipreqs`.
The updated `requirements.txt` is then staged and committed as part of the pre-commit hook. This process ensures that our requirements are always up-to-date.

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. What did you fill out? Did you deviate from the template in some way?**
>
> Recommended answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
>
> Answer:

From the cookiecutter template, we filled out everything except the
`notebooks` and `configs` folders. We added a `scripts` folder where
we saved the scripts for the pipelines, as they weren't directly
correlated to the main code of the project. Additionally, we created a
`gcp` folder to store the YAML files for building in the

### Question 6

> **Did you implement any rules for code quality and format? What about typing and documentation? Additionally,**
> **explain with your own words why these concepts matters in larger projects.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We used ... for linting and ... for formatting. We also used ... for typing and ... for documentation. These*
> *concepts are important in larger projects because ... . For example, typing ...*
>
> Answer:

We used Ruff for formatting to ensure our code is PEP8 compliant. PEP8 is the
standard for Python code, and is well-known and widely accepted. This means that
new team members are likely already familiar with it. Even if they aren't, PEP8 is
well-documented and easy to learn. We added Ruff to our pre-commit hook with the
`--fix` flag to automatically apply PEP8 standards.

Our project TOML file includes the following instructions for Ruff:

```toml
[tool.ruff]
line-length = 120
lint.select = ["I"]
```



## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Recommended answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

In total, We have implemented five tests. These tests verify the following functionalities:
- The `ColorizationDataset` class is properly initialized and handles datasets correctly.
- The dataloaders, ensuring they provide the expected batch size and shapes for both training and validation.
- The `PatchDiscriminator`, confirming its output shape is as expected.
- The utility function `get_project_root`, ensuring it correctly identifies the project directory.
- The utility function `lab_to_rgb`, ensuring it converts L*a*b* images to RGB format accurately.


### Question 8

> **What is the total code coverage (in percentage) of your code? If your code had a code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

The total code coverage of our code is as follows:
- 40% in `data`
- 60% in `model`
- 100% in `utils`

High code coverage is important but does not guarantee error-free code.
It shows the percentage of executed code but not the quality of the tests.
Edge cases, logical errors, and integration issues might still exist.


### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

We created a Kanban board with all the tasks in the project. For each task, the assigned person would create a branch and work on it.
When the feature or bug fix was ready, a pull request was created and approved by another team member (when possible).
For minor fixes, we pushed directly to the main branch.
This was really helpful to track all the changes and revert them in case something went wrong.
Additionally, with Git actions running tests on pull requests, we ensured the branch was functioning correctly.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

We integrated DVC with Google Cloud, linking it to a storage bucket that contains a zip file with all the data to streamline downloads. Although we primarily downloaded the dataset directly from Kaggle, we used DVC mainly to upload and manage the trained models. Looking ahead, if we incorporate data from additional sources, we plan to utilize DVC more extensively. For now, DVC is fully integrated into our project and ready for active use.

### Question 11

> **Discuss you continuous integration setup. What kind of continuous integration are you running (unittesting,**
> **linting, etc.)? Do you test multiple operating systems, Python  version etc. Do you make use of caching? Feel free**
> **to insert a link to one of your GitHub actions workflow.**
>
> Recommended answer length: 200-300 words.
>
> Example:
> *We have organized our continuous integration into 3 separate files: one for doing ..., one for running ... testing*
> *and one for running ... . In particular for our ..., we used ... .An example of a triggered workflow can be seen*
> *here: <weblink>*
>
> Answer:

[Here](https://github.com/MarlonBando/Chromify/actions/runs/12888763830) you can see one of our workflows. We have different unit tests that are run with pytest. These are run automatically when a push or a pull request to *main* has been done.
The tests are executed on Ubuntu, Windows, and MacOs, by two different python versions, python 3.11 and 3.12.


## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Recommended answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: Python  my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

We created a command in the *pyproject.toml* file and combined it with the functionality provided by the *typer* package.
Here it is an example: ``` chromify train --epochs 25 --batch-size 256 --use-checkpoint "0212215_12.pth" ```.
All the arguments of the train command are optional, since they have default values.

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

We haven't use config files and we didn't do any experiment

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Recommended answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

We have not implemented Weights and Biases into our code, thus we are not able to provide the asked screenshots.

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments/project? Include how you would run your docker images and include a link to one of your docker files.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

- Developed three Docker images:
  - **Training**: Used for training the ML model.
  - **API Backend**: Hosted the model for inference.
  - **Frontend**: Served the user interface.

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

We do not think that our code is perfect, but our model has been taken from someone else's work (see in [README.md](../../README.md)). Even though we have adapted the code to our necessities, we do not have the courage to do big modifications to the model in fear of just downgrading its performance.
To debug, we used the built-in debugger from Visual Studio Code. Sometimes we used the print function as an alternative to check some specific values of variables. It has also happened that there was not an obvious solution to our problem, so we turned to ChatGPT or GitHub Copilot to seek for possible reasons on why our code was wrong.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Recommended answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

We utilized the following GCP services in our project:

1. **Compute Engine**: Used to provision and manage virtual machine instances for training our machine learning models efficiently.
2. **Cloud Storage Bucket**: Used for storing a zip file containing the dataset, streamlining data access, and uploading trained models for secure and centralized storage.
3. **Artifact Registry**: Used as a secure repository to build and store Docker images, ensuring consistent and reliable containerized application deployments.

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

### Question 18

We used the Compute Engine to train our machine learning models.
Initially, we utilized a virtual machine instance equipped with a
**Tesla P100 GPU** in the **West Europe 1** zone.
This setup provided the computational power needed for
our training tasks but we soon run out of credit.
We also had problems with availability in this region and
therefore migrated to the **Central Europe** zone.
There, we used a virtual machine instance with an **NVIDIA T4 GPU**,
which offered excellent performance for deep learning
workloads while maintaining cost efficiency.
Both configurations enabled us to accelerate
the training process and effectively meet our computational requirements.


### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

![data archive](figures/bucket1.png)

![models archive](figures/bucket2.png)

### Question 20

> **Upload 1-2 images of your GCP artifact registry, such that we can see the different docker images that you have**
> **stored. You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

![models archive](figures/artifact.png)

### Question 21

> **Upload 1-2 images of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

![cloud build history](figures/cloud_history.png)

### Question 22

> **Did you manage to train your model in the cloud using either the Engine or Vertex AI? If yes, explain how you did**
> **it. If not, describe why.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We managed to train our model in the cloud using the Engine. We did this by ... . The reason we choose the Engine*
> *was because ...*
>
> Answer:

We managed to train our model in the cloud by starting a compute instance with a GPU on Google Cloud and accessing it
through SSH. Once connected, we cloned the GitHub repository onto the instance and trained the model there. After
training was completed, we sent the trained models to Google Cloud Storage using DVC for efficient version control
and storage management.
We chose this approach because it was the most straightforward and allowed direct access to an NVIDIA GPU, ensuring
optimal performance for our training process.

## Deployment

### Question 23

> **Did you manage to write an API for your model? If yes, explain how you did it and if you did anything special. If**
> **not, explain how you would do it.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We did manage to write an API for our model. We used FastAPI to do this. We did this by ... . We also added ...*
> *to the API to make it more ...*
>
> Answer:
We did manage to write an API for our model. We used FastAPI to do this. We created an endpoint /infer that accepts an image file upload. The image is processed by converting it to a grayscale image and then transforming it into a tensor. This tensor is then passed to our pre-trained model, which generates a colorized version of the image. The output tensor is converted back to an image and encoded in base64 format to be returned as a JSON response.

We also added CORS middleware to allow cross-origin requests from any origin, which is useful for frontend integration. This setup ensures that our API can be accessed from different domains, making it more flexible and easier to integrate with various frontend applications.

### Question 24

> **Did you manage to deploy your API, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer
> We successfully containerized our API using Docker and pushed the image to a container registry for deployment. The Dockerfile was designed to build a lightweight image, using `python:3.11-slim` as the base. The FastAPI application was configured to run with `uvicorn`, exposing the appropriate port as defined by the `$PORT` environment variable.

Initially, we tested the container locally by building and running it with a specific port (e.g., `docker run -e PORT=8080 -p 8080:8080`). This confirmed that the API was functional locally. However, when deploying to the cloud (using Google Cloud Run), the service failed to pass the health check. This issue stemmed from a misconfiguration related to the `$PORT` environment variable, which was not properly set or expanded within the container runtime.

Despite our efforts to debug and resolve the issue by modifying the Dockerfile and testing various configurations, the service was not able to start listening on the correct port. This has delayed the cloud deployment, but the image remains ready for redeployment once the issue is fully resolved.

### Question 25

> **Did you perform any unit testing and load testing of your API? If yes, explain how you did it and what results for**
> **the load testing did you get. If not, explain how you would do it.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *For unit testing we used ... and for load testing we used ... . The results of the load testing showed that ...*
> *before the service crashed.*
>
> Answer:

We didn't test our api.

### Question 26

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

We did not manage to implement monitoring.

If we had implemented monitoring, we would have used the **prometheus-client** library to expose metrics such as inference latency, API response times, and resource usage directly from the application.


## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 27

> **How many credits did you end up using during the project and what service was most expensive? In general what do**
> **you think about working in the cloud?**
>
> Recommended answer length: 100-200 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ... . Working in the cloud was ...*
>
> Answer:

Michele used all of his learning credits, and then we switched to Samer's credits, who spent the remaining balance.
The service that consumed the majority of our credits was the compute instance with the GPU. After running for two
full days, it consumed all $50 due to the high workload, including overnight usage, and because we used the NVIDIA
Tesla P100.

Getting started with the cloud was challenging, but once we understood the basic "rules," it became much easier and
more useful. Without cloud resources, we wouldn't have been able to train our model effectively.
When using Samer's credits we realized that other GPUs would give a much better performance for a very little increase in price.

### Question 28

> **Did you implement anything extra in your project that is not covered by other questions? Maybe you implemented**
> **a frontend for your API, use extra version control features, a drift detection service, a kubernetes cluster etc.**
> **If yes, explain what you did and why.**
>
> Recommended answer length: 0-200 words.
>
> Example:
> *We implemented a frontend for our API. We did this because we wanted to show the user ... . The frontend was*
> *implemented using ...*
>
> Answer:

We implemented a frontend for our API to provide an interactive interface for end-users. Since our model takes black-and-white images as input and colorizes them, the frontend allows users to upload their own images and view the colorized output. The frontend was built using Vite and TypeScript, with Mantine as the component library. Mantine's prebuilt components enabled us to quickly design a clean and responsive interface. To communicate with the backend API, we used Axios, which simplified the process of making HTTP requests and handling responses. This setup ensures a smooth user experience and seamless interaction between the frontend and backend services.

### Question 29

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally, in your own words, explain the**
> **overall steps in figure.**
>
> Recommended answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and push to GitHub, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

![architecture diagram](figures/scheme.png)


### Question 30

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Recommended answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

The biggest challenge we faced was deploying the Docker container with the API to the cloud. Unfortunately, we were unable to get it to work. We encountered issues with the port, and the solutions provided in the course material and online resources did not resolve the problem. Additionally, we experienced some difficulty training the model, as our cloud credits ran out mid-training.

### Question 31

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project. Additionally, state if/how you have used generative AI**
> **tools in your project.**
>
> Recommended answer length: 50-300 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
> *We have used ChatGPT to help debug our code. Additionally, we used GitHub Copilot to help write some of our code.*
> Answer:

Student s240033 was in charge of finding which were the different options of the models and which one could be the best fit for the task at hand. After finding which was it, he looked into how to implement it. Since it was a U-Net, and these networks are not directly found in huggingface he worked into trying to combine a decoder from huggingface and create an encoder from scratch. After many tries, this did not seem to work as expected, so he went back on to the research progress and read some articles. He found a GitHub repository that was accompanied by an article. We used the model of this repository but he adapted the code to our necessities and the format of our data. Combined with the adaptations of the code, some unit tests were created to ensure that some methods were working properly.
He also included the CLI commands to easily execute the training of the model and customize the parameters of execution. He partially worked on saving checkpoints for the model and the initialization of the training from a specific checkpoint.

Student s243121 managed the GitHub repository, pre-commit hooks, and GitHub Actions. He handled cloud resources (compute, storage, artifacts), implemented data version control, and created the training Docker image. Additionally, they assisted with the cloud-based training process.

Student s242943 handled both backend and frontend development, created the Docker image for both of them, and contributed to the deployment process and data handling.
