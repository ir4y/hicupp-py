# Python implementation of beautiful clojure library named [Hiccup](https://github.com/weavejester/hiccup)

Hiccup-py is a library for representing HTML in Python. It uses lists
to represent elements, and dicts to represent an element's attributes.

## Syntax

Here is a basic example of Hiccup-py syntax:

```python
from hicupp import html

html(["span", {"class": "foo"} "bar"]) #<span class="foo">bar</span>
```

The first element of the list is used as the element name. The second
attribute can optionally be a dict, in which case it is used to supply
the element's attributes. The third element is a tag's body.

The ability to provides a CSS-like shortcut for denoting `id` and `class` keeps
attributes:

```python
from hicupp import html

html(["div#foo.bar.baz", "bang"]) #<div id="foo" class="bar baz">bang</div>
```

If the body of the element is an iterable, its contents will be expanded out
into the element body. This makes working with forms like `map` more convenient:

```python
from hicupp import html

data = [1, 2, 3, 4]
html(["ul", (["li", i] for i in data)]) #<ul ><li >1</li><li >2</li><li >3</li><li >4</li></ul>
```


## License

Copyright © 2016 Ilya Beda

Distributed under the MIT License.
