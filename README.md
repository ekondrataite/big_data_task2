# Big Data Task 2

The goal of this task is to develop a Python code script and package it into a Docker container.

The python project is to train a linear regression model to predict housing prices in California. The data used for this project is accessed from sklearn library. The code:

## Project idea:

1. Does primary data analysis: 
   - Checks for NA's
   - Selects a subset of variables: MedInc, AveRooms, AveBedrms, Population, AveOccup.
   - Prints a correlation matrix for analysis.
2. Splits the data to train and test subsets with the ratio of 80:20.
3. Trains a Linear regression model on the train dataset.
4. Evaluates the result model:
   - Prints R-square score.
   - Prints MSE score.

## Docker:

Required files: (they can be found in this repository)
1. Python project code.
2. Requirements file.
3. Docker file.

Main docker commands used:

**To create docker image:**

- **Build an image:** docker build
- **Get the list of images:** docker image list
- **Run the docker:** docker run (image id)

**To push Docker image to DockerHub**

- **To tag my docker image:** docker tag 3676cc7b0d0a kondrataite/big_data_task2:newest
- **To push my tagged docker image to DockerHub:** docker push kondrataite/big_data_task2:newest

**To access the project through DockerHub**
- **To pull image from DockerHub:** docker pull kondrataite/big_data_task2:final
- **To run my project code:** docker run kondrataite/big_data_task2:final

The repository in DockerHub: https://hub.docker.com/repository/docker/kondrataite/big_data_task2/general
