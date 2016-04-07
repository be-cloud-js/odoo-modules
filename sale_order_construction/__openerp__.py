# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#
#    Author: Yannick Gouin <yannick.gouin@elico-corp.com>
#            Jerome Sonnet <jerome.sonnet@be-cloud.be> port to 9.0
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Sales Order for Construction Projects',
    'version': '0.1',
    'category': 'Sales',
    'description': """
    Add information to sale order and process to manage construction projects.
    """,
    "author": "be-cloud.be (Jerome Sonnet)",
    "website": "http://www.be-cloud.be",
    'depends': ['sale'],
    'init_xml': [],
    'data': ['views/sale_order_view.xml'],
    'installable': True,
    'active': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: