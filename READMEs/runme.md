# Running this program

## Install dependencies

You need to run these commands:

```bash
sudo <package_manager> install nmap
sudo <package_manager> install ansible

pip install dash --user
pip install dash-core-components --user
pip install dash-html-components --user
pip install plotly --user
pip install pandas --user
    
pip3 install speedtest-cli
```

## Adjustments

Adjust how often you want to run the data collection in seconds. This needs to be edited in ```continuous.sh``` and in ```visualize.py```. These numbers need to be equal.

The line number is indicated like so: &nbsp; ```1|``` 

in ```/controllers/continuous.sh```:
```bash

3| interval=600 #time interval between scans in seconds
```

in ```visualization/visualize.py```:
```python
17| interval = 600
```

