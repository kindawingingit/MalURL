![malurl_2](https://user-images.githubusercontent.com/54901460/140620830-4330f7e6-94ce-4278-8e59-9af1bbbc1bb1.gif)


![test](https://img.shields.io/github/workflow/status/BastaAditya/MalURL/Requirements%20Test)
![dependencies](https://img.shields.io/github/pipenv/locked/dependency-version/BastaAditya/MalURL/flask)
![repo](https://img.shields.io/github/repo-size/BastaAditya/MalURL)
![count](https://img.shields.io/tokei/lines/github/BastaAditya/MalURL)
![license](https://img.shields.io/github/license/BastaAditya/MalURL)
![last](https://img.shields.io/github/last-commit/BastaAditya/MalURL)

# MalURL
MalURL detects whether website links are malicious or not by applying various machine learning algorithms. MalURL uses  machine learning algorithms - Decision Tree and XGBoost on detecting whether a link is malicious or benign or phishing.

# Prerequisites :
  Docker

# Installation Steps:
1) Clone the repository. 
   `git clone https://github.com/BastaAditya/MalURL.git`
2) Change into the directory.
   `cd MalURL`
3) Build the docker image using the Dockerfile.
   `docker build -t malurl . `
4) After the mage is built, run the docker by giving the port mappings.
   `docker run -p 5000:5000 malurl`
5) Open up the browser and headover to `http://localhost:5000` to get the home page.
