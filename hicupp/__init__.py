import re


def html(array):
    if type(array) == str:
        return array
    elif len(array) == 1:
        return __build_tag(array[0], {}, [])
    elif len(array) == 2:
        tag = array[0]
        attrs = array[1]
        if type(attrs) == dict:
            return __build_tag(tag, attrs, array[2:])
        else:
            return __build_tag(tag, {}, array[1:])
    else:
        return __build_tag(array[0], array[1], array[2:])


def __build_tag(tag_string, tag_attrs, children):
    tag, attrs = __parse_tag_attrs(tag_string)
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
