from app import app


def test_header(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header.text == "Soul Foods Sales Dashboard"


def test_graph_exists(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")

    assert radio is not None