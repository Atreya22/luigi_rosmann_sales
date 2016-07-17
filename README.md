# Luigi-Sales Prediction

This project is an example of howto create a Machine Learning pipeline to build models.
It uses the data from the Rossman Sales Prediction Competition in Kaggle. 
The purpose of the project is not to create an accurate model for predicting Sales instead how to 
orchestrate the various tasks.

It uses [Luigi](https://github.com/spotify/luigi) to orchestrate the pipeline of the batch jobs.

### Videos 
* [PyCon Singapore, 2016](https://engineers.sg/video/machine-learning-pipeline-using-luigi-and-scikit-learn-pyconsg-2016--878)
* [PyData Singapore Meetup] (https://engineers.sg/video/a-machine-learning-data-pipeline-pydata-sg--723)

## Installation 
===============
### Python
---------------
It requires Python 2.7.*


### Installation
------------------------
```
$ sh build.sh
```

* Run the build.sh
* It will create a virtual environment in the root directory of the project with all the dependencies maintained in requirements.txt
* It will also setup the luigi Central Scheduler and run it as a daemon process.
* The Luigi Task Visualiser can be accessed by http://localhost:8082 which will give visualisation of all the running tasks.
* Historical Tasks can also be viewed by http://localhost:8082/history


### Known Issues
------------------------

* Using the SkLearn n_jobs > 1 for Scikit Learn Modules like GridSearchCV and others will cause an error.
* This may be due to the the Process Assignment ID of Luigi using the Central Scheduler.
* In case of --local-scheduler flag the error is not reproduced.



