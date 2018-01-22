# Assignment 0: Probability/Calculus Review and Environment Setup

## Probability/Calculus Review

There is nothing to complete in this section. Use the following information as a reference during lecture and assignments.

TODO. Include the following: Logarithm Rules, Exponential Rules, Useful Derivatives, Bayes Rule, perhaps some more.

## Environment Setup

For this course we'll rely heavily on Python 3, jupyter notebook, and pytorch for programming assignments. Jupyter is a nifty interactive programming environment and pytorch is useful for building and training deep neural networks. There are a handful of other python frameworks that will come in handy including: numpy, pandas, scikit-learn, and matplotlib.

To make it easier to install and use these tools we will provide a Dockerfile that can be built with Docker. This can done following these instructions:

- Navigate to the directory with the appropriate Dockerfile. `cd /path/to/dockerfile-directory`
- Run the Docker command for building Dockerfiles. `docker build -t cs5304 .`
- Now we can start our Docker image with the following command:

```
docker run -i -t --name cs5304 \
    -p 3003:3003 \
    -v `pwd`:/code \
    cs5304 \
    /bin/bash
```

***Programming*** For this assignment, all that is required is to run Docker as instructed above, then to run the notebook that we've provided, and print the output to a pdf (this can be done with File -> Print Preview).

## FAQ

### Questions related to Docker or other programming tools.

Please email one of the TAs or post on the forum if you run into any programming related issues, and please feel free to help out one another. Do not spend too much time debugging on your own if it can be helped.

### How can I run Docker without `sudo`?

We recommend avoiding the use of `sudo` whenever possible. To run Docker with `sudo` please follow the instructions here: https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
