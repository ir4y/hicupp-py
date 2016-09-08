from hicupp import html


def test_simple_tag():
    assert '<div ></div>' == html(["div"])


def test_simple_tag_with_id():
    assert '<div id="myid"></div>' == html(["div", {"id": "myid"}])


def test_simple_tag_with_child():
    assert '<div ><p >hello</p></div>' == html(["div", ["p", "hello"]])


def test_simple_tag_with_id_and_child():
    assert '<div id="myid"><p >hello</p></div>' == html(["div", {"id": "myid"},
                                                        ["p", "hello"]])

