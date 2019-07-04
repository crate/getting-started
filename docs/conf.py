from crate.theme.rtd.conf.crate_getting_started import *

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None

source_suffix = '.rst'

exclude_patterns = ['.*', '*.lint', 'README.rst']

master_doc = 'index'

extensions = ['sphinx_sitemap']
site_url = 'https://crate.io/docs/crate/getting-started/en/latest/'
