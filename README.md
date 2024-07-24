# Rag Tutor

A retrieval augmented generation application for biostatistics.

## Development

How to develop on this project.

1. Install [poetry](https://python-poetry.org/) if it is not already on your system.
2. From the root directory run `poetry install`. This will install `ragtutor` and its dependencies into a virtual environment. You only need to do this the first time you start using the project.
3. Run `poetry shell` to activate this environment.
4. To run the web server in dev mode (use this for local development): `fastapi dev ragtutor/main.py`.
   1. Now go to the URL printed out to the console, [http://127.0.0.1:8000](http://127.0.0.1:8000). This will return the data from the `/` (root) route in your app. It is running this code:
   ```python
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
   ```
   2. Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see your interactive documentation. This shows you your routes (`/` and `/query`) available as endpoints in your application. You can click on these routes in the documentation and then click "Try it out" to send over real requests to your web application.
5. If you want to have some run and access your webserver over your local network run `fastapi run ragtutor/main.py`. You'll notice that it is now serving on [http://0.0.0.0:8000](http://0.0.0.0:8000). The `0.0.0.0` means it is now no longer serving just on your `localhost` network but that other machines can connect to the app at the IP address of your laptop. You can lookup the IP address of your laptop in system preferences usually under a "network" setting. Assuming you find your IP address is `192.168.1.171` then on another laptop (or mobile device) connected to the same network go to `http://192.168.1.171:8000` and you'll be able to access the web application.
