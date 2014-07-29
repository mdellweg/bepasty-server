# Copyright: 2014 Daniel Gonzalez <gonvaled@gonvaled.com>
# License: BSD 2-clause, see LICENSE for details.

from xstatic.main import XStatic

# names below must be package names
mod_names = [
    'pygments',
]

pkg = __import__('xstatic.pkg', fromlist=mod_names)
serve_files = {}
for mod_name in mod_names:
    mod = getattr(pkg, mod_name)
    xs = XStatic(mod, root_url='/static', provider='local', protocol='http')
    serve_files[xs.name] = xs.base_dir