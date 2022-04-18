# vulnika
Vulnerable flask application with examples of exploitation of:
- Broken Access Control
- Injection (Bash scripting)
- Remote Code Execution
- Cross-site scripting (XSS)

### Run:
To run just start docker-compose `docker-compose up`

### Service:
Service will be available at [http://127.0.0.1:8089](http://0.0.0.0:8089/)

### Patch:
Change the files from original `app` folder to ones from `patches`. In particular, `main.py` and `templates/main.html` files.