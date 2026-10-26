import project

def test_add():
    assert project.add(2, 3) == 5

def test_subtract():
    assert project.subtract(10, 4) == 6

def test_multiply():
    assert project.multiply(5, 4) == 20

def test_divide():
    assert project.divide(10, 2) == 5

def test_power():
    assert project.power(2, 3) == 8

def test_menu(capsys):
    project.menu()
    output = capsys.readouterr().out

    assert "PYTHON MATH LAB" in output
    assert "1. Calculator" in output
    assert "2. Graph" in output
    assert "3. Exit" in output

def test_choose_function(monkeypatch, capsys):
    inputs = iter(["1", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    project.choose_function()

    output = capsys.readouterr().out

    assert "y = x" in output
    assert "5.00" in output

def test_graph(capsys):
    project.graph(project.linear, "y = x", 5)

    output = capsys.readouterr().out

    assert "y = x" in output
    assert "●" in output
