from hicupp import html


def test_simple_tag():
    assert '<div ></div>' == html(["div"])


def test_simple_tag_with_text_content():
    assert '<div >hello</div>' == html(["div", "hello"])


def test_simple_tag_with_id():
    assert '<div id="myid"></div>' == html(["div", {"id": "myid"}])


def test_simple_tag_with_child():
    assert '<div ><p >hello</p></div>' == html(["div", [["p", "hello"]]])


def test_simple_tag_with_id_and_child():
    assert '<div id="myid"><p >hello</p></div>' == html(["div",
                                                         {"id": "myid"},
                                                         [["p", "hello"]]])


def test_tag_with_attrs_notation():
    assert '<div id="myid"></div>' == html(["div#myid"])
    assert '<div class="foo"></div>' == html(["div.foo"])
    assert '<div class="foo bar" id="myid"></div>' == html(["div#myid.foo.bar"])


def test_tag_as_function():
    def noscript(attrs, children):
        return ["noscript"]

    assert '<noscript ></noscript>' == html([noscript,
                                             {"id": "foo"},
                                             [["p", "data"]]])


def test_tag_with_computed_children_map():
    data = [1, 2, 3, 4]

    def mod(i):
        return ["li", i]

    assert '<ul ><li >1</li><li >2</li><li >3</li><li >4</li></ul>' ==\
        html(["ul", map(mod, data)])


def test_tag_with_computed_children_generator():
    data = [1, 2, 3, 4]
    assert '<ul ><li >1</li><li >2</li><li >3</li><li >4</li></ul>' ==\
        html(["ul", (["li", i] for i in data)])
