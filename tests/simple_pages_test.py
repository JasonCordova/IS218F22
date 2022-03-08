"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/pythonflask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/continuous">Continuous Integration/Deployment</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_gitpage(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"git" in response.data

def test_request_dockerpage(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"docker" in response.data

def test_request_pythonflask(client):
    """This makes the index page"""
    response = client.get("/pythonflask")
    assert response.status_code == 200
    assert b"pythonflask" in response.data

def test_request_continuous(client):
    """This makes the index page"""
    response = client.get("/continuous")
    assert response.status_code == 200
    assert b"continuous" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
