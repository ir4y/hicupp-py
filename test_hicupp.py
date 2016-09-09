from hicupp import html


def test_simple_tag():
    assert '<div ></div>' == html(["div"])


def test_simple_tag_with_id():
    assert '<div id="myid"></div>' == html(["div", {"id": "myid"}])


def test_simple_tag_with_child():
    assert '<div ><p >hello</p></div>' == html(["div", ["p", "hello"]])


def test_simple_tag_with_id_and_child():
    assert '<div id="myid"><p >hello</p></div>' == html(["div",
                                                         {"id": "myid"},
                                                         ["p", "hello"]])


def test_tag_with_attrs_notation():
    assert '<div id="myid"></div>' == html(["div#myid"])
    assert '<div class="foo"></div>' == html(["div.foo"])
    assert '<div class="foo bar" id="myid"></div>' == html(["div#myid.foo.bar"])


def test_tag_as_function():
    def my_tag(attrs, children):
        return ["noscript"]

    assert '<noscript ></noscript>' == html([my_tag,
                                             {"id": "foo"},
                                             ["p", "data"]])
