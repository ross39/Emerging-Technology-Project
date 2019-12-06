# Table of Contents
* [Description](#description)
* [Sections](#sections)
* [Getting Started](#getting-started)
* [Built With](#built-with)
* [License](#license)

## Description

Welcome to my project for Emerging Technologies. The goal of this project is to create a web app that recognises hand drawn digits. I have also done some data analysis and exploration in the jupter notebooks so be sure to check those out. For the purposes of making this easy to understand the project will be broken into various parts and I will explain them below

## Sections

### Part 1. 
This is the web app. All code for the web app is in the folder labelled 'MNISTCode'. Everything is there to run the project locally. Also I hope to host this on heroku. ===> Link

### Part 2. 

This is the IRIS dataset. Not necessarily part of the project but it's pretty cool so included it in

### Part 3. 

Initial exploration of the MNIST dataset and training the model

### Part 4. 

Further exploration and explaining how neural networks work and exploring the model in more depth. I didn't want to create a god notebook. 

### Part 5. 

This is a notebook dedicated to the numpy package for python

## Getting Started

To get started just clone this repo or you can use gitpod to load the project in an online virtual enviroment</br>
LINK TO GITPOD =====> https://www.gitpod.io/.

gitpod is really neat and I'd recommne checking this out.

### Prerequisites

Jupyter notebooks =====> https://jupyter.org/ </br>
Anaconda ======> https://www.anaconda.com/ </br>
:warning: You can install jupyter notebooks through anaconda so check out anaconda first!

### How to Run Notebooks
You should have jupyter notebooks installed. Easiest way to do this is to download and run anaconda on your machine that way you can get jupyter notebooks plus a ton of other goodies! Alternatively you can use gitpod and just install the requirments from the command line using

    conda install --yes --file requirements.txt

This will install the dependencies to your conda enviroment. </br>

:bangbang: If one dependency fails then all will fail. This can happen very rarely. To get around this problem please try =>

    while read requirement; do conda install --yes $requirement; done < requirements.txt
  
For further information please refer to =====> https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4 


### How to Run Scripts

To run the MNIST webapp you must run the app.py file which is the entry point for the webapp. To run please follow the instructions below 

    export FLASK_APP=app.py
    
    flask run

Please note that I personally use a Unix system(Mac) and this is the command I use. This will work on any Unix system(Linux, Mac). For Windows users please refer to the flask documentation.

#### Running the jupyter notebooks
For anyone reading this not familiar with jupyter notebooks, jupyter notebooks will not run like regular python files/scripts. You will need jupyter notebooks installed on your system. To run the notebooks you can just type the command below in the directory of your files or type the command anywhere and just use the gui to move to the files.
        
        jupyter notebook 
        
You can then view and run the notebooks in the browser. </br>
For a beginner tutorial on jupyter notebooks ====> https://www.youtube.com/watch?v=HW29067qVWk


## Built With
Python </br>
Student sweat and tears </br>
Insiration from kaggle, r/datascience, r/machinelearning
Enviroment: MacOs(10.14.6), python 3.7(anaconda), jupyter notebooks, Vim(spacevim, I'd highly recommend). The exact configuration of jupyter notebooks I'm using is. This output of jupyter --version is below


        jupyter core     : 4.5.0
        jupyter-notebook : 6.0.0
        qtconsole        : 4.5.1
        ipython          : 7.6.1
        ipykernel        : 5.1.1
        jupyter client   : 5.3.1
        jupyter lab      : 1.0.2
        nbconvert        : 5.5.0
        ipywidgets       : 7.5.0
        nbformat         : 4.4.0
        traitlets        : 4.3.2



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE) file for details
