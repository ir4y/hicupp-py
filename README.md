# Python implementation of beautiful clojure library named [Hiccup](https://github.com/weavejester/hiccup)

Hiccup-py is a library for representing HTML in Python. It uses lists
to represent elements, and dicts to represent an element's attributes.

## Syntax

Here is a basic example of Hiccup-py syntax:

```python
from hicupp import html

html(["span", {"class": "foo"} "bar"]) #"<span class="foo">bar</span>"
```

The first element of the list is used as the element name. The second
attribute can optionally be a dict, in which case it is used to supply
the element's attributes. Every other element is considered part of the
tag's body.

The ability to provides a CSS-like shortcut for denoting `id` and `class` keeps
attributes:

```python
from hicupp import html

html(["div#foo.bar.baz", "bang"]) #<div id="foo" class="bar baz">bang</div>
```

## License

Copyright © 2016 Ilya Beda

Distributed under the MIT License.
