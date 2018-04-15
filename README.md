# Data engineering exercise

### Instructions for use:

To run the code:

1. Clone the repo and cd into the directory
2. The input_data.gz file needs to be placed at the top level of the directory
3. Dependencies are all installed inside a virtual environment, to use it you
   need to have virtualenv installed as such: `pip install virtualenv`
4. Create virtual environment: `virtualenv my_env`
5. Activate the virtual environment: `source my_env/bin/activate`
6. Install dependencies inside it: `pip install -r requirements.txt`
7. Run the command: `python3 runner.py input_data.gz`
8. Watch your terminal for some magic
9. Deactivate the environment when the code exits: `deactivate`

---

Resources:

* [ip-address-lookups-in-python](http://tech.marksblogg.com/ip-address-lookups-in-python.html)
* [geoip -conflict with python 3.5](https://github.com/mirumee/saleor/issues/458)
