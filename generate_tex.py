from yaml import load, FullLoader

with open('data.yml', 'r') as f:
    data = load(f, Loader=FullLoader)


def safe(d, key):
    """Safely return value of the dict or empty string."""
    if key in d:
        return d[key]
    else:
        return ''


def print_personal_info(personal_info):
    lines = ['\\personalinfo{\n']
    for key in personal_info:
        line = '  \\'
        line += key
        line += '{'
        line += safe(personal_info, key)
        line += '}\n'
        lines.append(line)
    lines.append('}\n')
    return lines


def print_list(items):
    """Return TeX lines of an itemize element."""
    lines = []
    lines.append('\\begin{itemize}\n')
    for item in items:
        lines.append('\\item ' + item + '\n')
    return lines


def print_event(event):
    """Return TeX lines for an event."""
    lines = []
    lines.append('\\cvevent{')
    lines[0] += safe(event, 'title') + '}{'
    lines[0] += safe(event, 'org') + '}{'
    lines[0] += safe(event, 'time') + '}{'
    lines[0] += safe(event, 'location') + '}\n'
    description = safe(event, 'description')
    if type(description) is str:
        lines.append(description + '\n')
    elif type(description) is list:
        lines += print_list(description)
    return lines


with open('personal-info.tex', 'w') as f:
    f.writelines(print_personal_info(data['personalinfo']))
