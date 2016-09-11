import re
from .misc import get


def html(body):
    if isinstance(body, list):
        array = body
        if len(array) == 1:
            return __build_tag(array[0], {}, [])
        elif len(array) >= 2:
            tag = array[0]
            attrs = array[1]
            if type(attrs) == dict:
                return __build_tag(tag, attrs, get(array, 2, []))
            else:
                return __build_tag(tag, {}, array[1])
    else:
        return str(body)


def __build_tag(the_tag, tag_attrs, children):
    if callable(the_tag):
        return html(the_tag(tag_attrs, children))

    tag, attrs = __parse_tag_attrs(the_tag)
    attrs.update(tag_attrs)

    return "<{tag} {attrs}>{children}</{tag}>".format(
            tag=tag,
            attrs=__build_attrs(attrs),
            children=''.join(map(html, children)))


def __build_attrs(attrs):
    return " ".join('{0}="{1}"'.format(k, v)
                    for k, v in attrs.items())


def __parse_tag_attrs(tag):
    m = re.search(r'(\w+)(#\w+)?((\.\w+)*)', tag)
    tag = m.group(1)
    id = m.group(2)
    attrs = {'id': id[1:]} if id else {}
    classes = m.group(3)
    if classes:
        attrs['class'] = ' '.join(classes[1:].split('.'))
    return (tag, attrs, )
