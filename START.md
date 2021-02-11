# How to start the project

1. Create the virtual enviroment and install packages:
> ``` 
> $ bash build.sh
> ``` 
2. Start the database with:
> ``` 
> $ bash start.sh
> ``` 
3. Generate some fake data:
> ``` 
> $ bash data_gen.sh
> ```
4. Check the metrics:
> ``` 
> $ ./venv/bin/python src/mypack/metrics.py
> ```
5. Run tests(need to install the package in dev mode):
> ``` 
> $  pytest src
> ```
