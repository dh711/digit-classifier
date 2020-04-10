# digit-classifier.

Handwritten Digit Recognition using the MNIST dataset.

Dataset from: https://www.kaggle.com/oddrationale/mnist-in-csv

### prerequisites.

* python v3.7.7
* scikit-learn v0.22.1
* numpy v1.18.1
* pandas v1.0.3
* pillow v7.0.0
* django v3.0.3

### setup and deployment.
1. Setup an environment with the above mentioned libraries.
2. Clone the repository.
3. To launch the server, navigate to `django-server/`
4. In terminal, run `python manage.py runserver` to start the server.
5. Open your browser and go to `localhost:8000/digits/` or `http://127.0.0.1:8000/digits/`
6. Draw desired digit and click `PREDICT` to get an answer.
