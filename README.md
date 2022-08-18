## Snow problem: Find the cost effective path to clear the snow in the city of Montreal, Canada.


## Real:
The pratical part of the solution using osmnx, networkx, pandas and numpy, plotly

First set up a virtual environment
```
pip install -r requirements.txt
```

To launch the solution please run script.py with --city and --country as --weight_name arguments
weight_name could be 'length' or 'travel_time'
```
Example: python script.py --city Pesaro --country Italy --weight_name length
```

Or for Montreal use the different borough
For instance:
python script.py --city borough --country Canada --weight_name length

It should open an **interactive map** and print the **statistics** for this city
and country
