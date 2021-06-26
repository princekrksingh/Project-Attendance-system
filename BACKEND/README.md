# Face Recognition API

## Python environment

**Python version:** `Python 3.6.8`

For this project, we used `Conda environment` as environment.



## Python Conda Environments

You can install all the dependencies using conda.
How to create env in conda?

# Step 1: [Download Anaconda](https://www.anaconda.com/products/individual) and [create an environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) by using my [environment.yml](https://drive.google.com/file/d/1ONgvHnECZ1pH66tMleVz0BUCh4nUH0Ev/view?usp=sharing) file.

Note:Download yml file first.

# Step2: Now activate environment using conda activate env_name

Here is the [link](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) for other helpful commands.



## How to use it

There are two components in the backend: `app.ipynb` and `camerafeed.ipynb`.

* **app.ipynb:** This is the API itself, it handle routes. You can run it with jupyter notebook.


* **camerafeed.ipynb:** This is the algorithm that read the video feed and apply face recognition. You can run it 
with Jupyter notebook.

By default it will select the camera of your computer, but you can change it by any video feed, just change the value of `video_capture = VideoCapture(0)` 0 is the prinary webcam of your computer. You can also add multiple feeds.
