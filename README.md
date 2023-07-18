
===
## Project Information
- Title:  `questions and answers`


## Install & Dependence
- python 3.10
- Docker


## Use
- using python
  ```
  python3 pip install -r requirements.txt
  python3 -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload --timeout-keep-alive 600 --workers 10
  ```
- using docker
  ```
  docker build -t lmqg/app:latest .
  docker run -p 8080:8080 lmqg/app:latest
  ```
## Execute

- using python
  ```
  import requests
  import json
  

  def api(url,value):
    
      headers = {"Content-Type": "application/json; charset=utf-8"}
      
      data = {
          "context": value
      }
      
      response = requests.post(url, headers=headers, json=data)
      
      #print("Status Code", response.status_code)
      #print("JSON Response ", response.json())
      return response.json()
  
  if __name__ == "__main__":
    url="http://127.0.0.1:8080/generation"
    context="""William Turner was an English painter who specialised in watercolour landscapes. He is often known as William Turner of Oxford or just Turner of Oxford to distinguish him from his contemporary, J. M. W. Turner. Many of Turner's paintings depicted the countryside around Oxford. One of his best known pictures is a view of the city of Oxford from Hinksey Hill."""
    response = api(url,context)
    print(response)

  ```

## Directory Hierarchy
```
|—— .gitignore
|—— Dockerfile
|—— LICENCE
|—— app.py
|—— execute
|—— readme.MD
|—— requirements.txt
```

## References
- [source](https://github.com/asahi417/lm-question-generation)
- [huggingface](https://huggingface.co/lmqg)
  
## License

- MIT
