# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Inventory Result Aeroo Report",
    "version": "8.0.1.0.0",
    "summary": "Adds Stock Inventory Result Report",
    "author": "Michael Viriyananda, Andhitia Rama, "
              "OpenSynergy Indonesia",
    "website": "https://opensynergy-indonesia.com",
    "category": "Stock",
    "depends": [
        "stock",
        "report_aeroo"
    ],
    "data": [
        "reports/stock_inventory_result.xml",
        "views/stock_inventory_view.xml"
    ],
    "license": "AGPL-3",
    "installable": True,
}
