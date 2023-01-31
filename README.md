# sloom

UNDER DEVELOPMENT v 0.2.0

Sloom is a web scraping / crawling library

## Setup

to get use 
```
pip install sloom
```

to update use
```
 pip install sloom --upgrade
 ```

 ## Documentation

### Simple crawling function.
 
The `run()` function takes a parameter which is the root url. The crawler will start at this URL and go through links found at the root URL.

*WARNING*: `run()` is an infinte loop.

 ```python
 import sloom

 sloom.run("https://www.example.com")

 ```
