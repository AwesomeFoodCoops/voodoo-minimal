#!/usr/bin/python

import sys

# TODO Replace this empty list by the one generated in the /bin/start_openerp
# file, after each ak build order.
sys.path[0:0] = [
  '/home/sylvain/.voodoo/shared/eggs/nose-1.3.7-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/Unidecode-0.4.19-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/Pillow-3.4.2-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/phonenumbers-7.7.2-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/unicodecsv-0.14.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyBarcode-0.7-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyinotify-0.9.6-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/PyChart-1.39-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/anybox.recipe.odoo-1.9.2-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/Babel-2.3.4-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/decorator-4.0.10-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/docutils-0.12-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/feedparser-5.2.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/gevent-1.1.2-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/Jinja2-2.8-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/lxml-3.6.4-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/Mako-1.0.4-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/mock-2.0.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/ofxparse-0.15-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/passlib-1.6.5-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/psutil-4.3.1-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/psycogreen-1.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/psycopg2-2.6.2-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/Python_Chart-1.39-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pydot-1.0.28-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyparsing-2.1.10-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyPdf-1.13-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyserial-3.2.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/python_dateutil-2.4.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/python_ldap-2.4.27-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pytz-2016.7-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pyusb-1.0.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/PyYAML-3.12-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/qrcode-5.3-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/reportlab-2.7-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/requests-2.11.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/suds_jurko-0.6-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/vatnumber-1.2-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/vobject-0.9.3-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/Werkzeug-0.11.11-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/xlwt-1.1.2-py2.7.egg',
  '/workspace/parts/odoo-production/odoo',
  '/home/sylvain/.voodoo/shared/eggs/anybox.testing.datetime-0.5-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/unittest2-1.1.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/traceback2-1.4.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/six-1.10.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/argparse-1.4.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/setuptools-28.6.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/python_stdnum-1.4-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/beautifulsoup4-4.5.1-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/pbr-1.10.0-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/funcsigs-1.0.2-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/MarkupSafe-0.23-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/greenlet-0.4.10-py2.7-linux-x86_64.egg',
  '/home/sylvain/.voodoo/shared/eggs/pip-8.1.2-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/zc.buildout-2.5.3-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/zc.recipe.egg-2.0.3-py2.7.egg',
  '/home/sylvain/.voodoo/shared/eggs/linecache2-1.0.0-py2.7.egg',
  ]


from anybox.recipe.odoo import devtools
devtools.load(for_tests=False)


import anybox.recipe.odoo.runtime.start_openerp

if __name__ == '__main__':
    sys.exit(anybox.recipe.odoo.runtime.start_openerp.main('/workspace/parts/odoo-production/odoo/openerp-server', '/workspace/louve_openerp.cfg', version=(9, 0), gevent_script_path='/workspace/bin/gevent_openerp'))
