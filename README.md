# Simple-API
Simple API to query data from an online MongoDB database.

The MongoDB datbase uses data from the `individuals.json.gz` file cointaned in the SummerOfCodeImages [repository](https://github.com/FreeUKGen/SummerOfCodeImages/tree/master/freecen_subset/data). 

Create a free databse at [MLab](www.mla.com) and import the JSON data.

Create a virtual environment

Install all libraries in requirements by running `pip install -r requirements.txt`

Run `main.py` and open [127.0.0.1/5000](127.0.0.1/5000)

An example of an endpoint is [127.0.0.1/5000/individuals/Richard](127.0.0.1/5000/individuals/Richard).
