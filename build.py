import argparse

from jinja2 import Template


parser = argparse.ArgumentParser()
parser.add_argument('--site-prefix', type=str, default='/ds-in-the-wild',
    help='Set prefix so that served correctly under Github Pages. Use "" when serving locally.')
options = parser.parse_args()


settings = {
    'index_template': 'index.jinja2',
    'index_out': 'index.html',
}


template_kwargs = {
    'site_prefix': options.site_prefix
}


with open(settings['index_template']) as f:
    template = Template(f.read())


with open(settings['index_out'], 'w') as f:
    site = template.render(**template_kwargs)
    f.write(site)
