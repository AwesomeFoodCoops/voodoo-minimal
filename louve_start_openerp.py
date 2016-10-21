#!/usr/bin/python

import sys

# TODO Replace this empty list by the one generated in the /bin/start_openerp
# file, after each ak build order.
sys.path[0:0] = []


from anybox.recipe.odoo import devtools
devtools.load(for_tests=False)


import anybox.recipe.odoo.runtime.start_openerp

if __name__ == '__main__':
    sys.exit(anybox.recipe.odoo.runtime.start_openerp.main('/workspace/parts/odoo-production/odoo/openerp-server', '/workspace/louve_openerp.cfg', version=(9, 0), gevent_script_path='/workspace/bin/gevent_openerp'))
