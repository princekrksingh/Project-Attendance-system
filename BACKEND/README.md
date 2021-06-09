# Face Recognition API

## Python environment

**Python version:** `Python 3.6.8`

For this project, we used `Conda environment` as environment.
You can find it in `API/env`.
You can **activate** it with: 
```bash
$ source env/bin/activate
```
and **disable** it with:
```bash
$ deactivate
```

## Python Conda Environments

You can install all the dependencies using conda.
How to create env in conda?
Here is the [link](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands).


## How to use it

There are two components in the backend: `app.ipynb` and `camerafeed.ipynb`.

* **app.ipynb:** This is the API itself, it handle routes. You can run it with jupyter notebook.


* **camerafeed.ipynb:** This is the algorithm that read the video feed and apply face recognition. You can run it 
with Jupyter notebook.

By default it will select the camera of your computer, but you can change it by any video feed, just change the value of `video_capture = VideoCapture(0)` 0 is the prinary webcam of your computer. You can also add multiple feeds.
