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


def __build_tag(tag, attrs, children):
    return "<{tag} {attrs}>{children}</{tag}>".format(
            tag=tag,
            attrs=__build_attrs(attrs),
            children=''.join(map(html, children)))


def __build_attrs(attrs):
    return " ".join('{0}="{1}"'.format(k, v)
                    for k, v in attrs.items())
