import subprocess


def default():
    """Crea la imagen"""

    subprocess.run(
        [
            "shot-scraper",
            "http://127.0.0.1:8000",
            "-o screenshot.png",
            "-s #container",
        ]
    )


def dark():
    """Crea la imagen en modo oscuro"""

    subprocess.run(
        [
            "shot-scraper",
            "http://127.0.0.1:8000/black",
            "-o screenshot.png",
            "-s #container",
        ]
    )
