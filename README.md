<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Rates Service & Extract Job</h3>

  <p align="center">
    Bootstrap curve extract job and rates service to return curve data
    <br />
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

As required, this project contains 2 main components to do the following tasks:
* Extract forward rates from designated website https://www.pensford.com/resources/forward-curve and save the results in local sqlite db file. For purpose of simplicity and requirement, I only extract Libor 1 Month and Sofr 1 Month rates along with their Reset Date. This is a separate executable job.
* A FastAPI service continuously running to listen to the request from clients, it returns date along with its corresponding rate based on ceiling/floor/spread provided by request sent from clients. The response payload is a json object and available to display in UI.
* It takes around 4-5 hours to complete the entire project. Including initial drafting, coding, testing and documenting.
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

In order to make things work, I am using libraries below. (We are not using any fancy libraries to do the job. Simplicity is beauty!)

* [FastAPI](https://fastapi.tiangolo.com/)
* [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [Sqlite](https://www.sqlite.org/index.html/)
* [Python 3.8.5](https://www.python.org/downloads/release/python-385/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can directly clone this project and copy to your local path (https://github.com/stevencao59/KKR.git)

### Prerequisites

* You will need to ensure Python 3.8 and above as well as pip are installed on your local machine.
* To install Python and pip, please follow the link below (https://www.python.org & https://pip.pypa.io/en/stable/installation/)

### Installation

You can simply run pip to install all required dependencies (Be sure to navigate to root directory of this project (KKR)):
```
pip install -r requirements.txt
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Extract Job
* To Run Extract job, simply navigate to project root folder and execute py file below:
```
python3 main_extract.py
```
 * The job extracts latest curve rate from website (https://www.pensford.com/resources/forward-curve), update existing rates and insert new ones based on dates (Check if exists, update if so, otherwise insert).

* All rates data is saved in forward_date sqllite db in project root folder. You can use any SQLite DB browser to open the db and check data.

![sqlite]

 ### Rest Service
 * To Run Rest Service, simply navigate to project root folder and execute py file below:
 ```
 python3 main_service.py
 ```
* You can open any web browser and type similar url (GET request) to check if service is running. Example:
http://127.0.0.1:8000/rates/?maturity_date=2022-11-23&reference_rate=SOFR&rate_floor=0.02&rate_ceiling=0.10&rate_spread=0.02

* To test POST response, go to http://127.0.0.1:8000/docs#/default. Open POST and click Try it out. You can pass following JSON object structure to test its response: {"maturity_date": "2022-11-23","reference_rate": "SOFR","rate_floor": 0.02,"rate_ceiling": 0.1,"rate_spread": 0.02}. Click Execute to see the results below.

![post]

* The service takes the maturity date and uses the closest day available in database against this maturity date in a month and display all curve rates up to this maturity date. For example, the url above yields below results:
```
[{"date":"2022-03-25","rate":0.0230404},{"date":"2022-04-25","rate":0.026483600000000003},{"date":"2022-05-25","rate":0.0291316},{"date":"2022-06-25","rate":0.0319899},{"date":"2022-07-25","rate":0.0354336},{"date":"2022-08-25","rate":0.036522200000000005},{"date":"2022-09-25","rate":0.0392427},{"date":"2022-10-25","rate":0.0414861}]
```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Switch to other database system to evaluate its performance. NoSQL systems can also be taken into account (DynamoDB, Mango DB, Cassandra and etc)
- [ ] Add load balancer to optimize REST requests when request volume continues to grow
- [ ] Dockerize REST Service to make it available to run in container
- [ ] Add UI to display current rate curves (LIBOR & SOFR) based on maturity dates along with other parameters

See the [open issues](https://github.com/stevencao59/KKR/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Lei Cao (Steven) - steven.cao.rider@gmail.com

Project Link: [https://github.com/stevencao59/KKR](https://github.com/stevencao59/KKR)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[post]: images/post.png
[sqlite]: images/sqlite.png