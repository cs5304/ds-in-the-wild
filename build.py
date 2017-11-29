import argparse
import pandas as pd
from jinja2 import Template


parser = argparse.ArgumentParser()
parser.add_argument('--site-prefix', type=str, default='/ds-in-the-wild',
    help='Set prefix so that served correctly under Github Pages. Use "" when serving locally.')
options = parser.parse_args()


settings = {
    'index_template': 'index.jinja2',
    'index_out': 'index.html',
    'syllabus': 'syllabus.csv',
}


template_kwargs = {
    'site_prefix': options.site_prefix
}


def read_template():
    with open(settings['index_template']) as f:
        template = Template(f.read())
    return template


def write_template(template, **kwargs):
    with open(settings['index_out'], 'w') as f:
        site = template.render(**kwargs)
        f.write(site)


def read_syllabus():
    syllabus = []
    df = pd.read_csv(settings['syllabus'], dtype=dict(date=str, topic=str, assignment=str))
    for row in df.iterrows():
        syllabus.append(dict(
            date=row[1].date,
            topic=row[1].topic,
            assignment=row[1].assignment,
            ))
    return syllabus


def main():
    template = read_template()
    syllabus = read_syllabus()
    template_kwargs['syllabus'] = syllabus
    write_template(template, **template_kwargs)


main()
