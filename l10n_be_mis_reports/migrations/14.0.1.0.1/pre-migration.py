# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

import logging

import openugradelib

_logger = logging.getLogger(__name__)

_field_renames = [
    ("dms.file", "dms_file", "res_mimetype", "mimetype"),
]

# These xmlids where deleted in the current version.
# When migrating from a previous version, the update process try to
# delete these records but it's part from other element that cannot be
# deleted.
_xmlids = [
    "mis_report_vat",
    "mis_report_vat_cadre_2",
    "mis_report_vat_grid_00",
    "mis_report_vat_grid_01",
    "mis_report_vat_grid_02",
    "mis_report_vat_grid_03",
    "mis_report_vat_grid_44",
    "mis_report_vat_grid_45",
    "mis_report_vat_grid_46",
    "mis_report_vat_grid_47",
    "mis_report_vat_grid_48",
    "mis_report_vat_grid_49",
    "mis_report_vat_cadre_3",
    "mis_report_vat_grid_81",
    "mis_report_vat_grid_82",
    "mis_report_vat_grid_83",
    "mis_report_vat_grid_84",
    "mis_report_vat_grid_85",
    "mis_report_vat_grid_86",
    "mis_report_vat_grid_87",
    "mis_report_vat_grid_88",
    "mis_report_vat_cadre_4",
    "mis_report_vat_grid_54",
    "mis_report_vat_grid_55",
    "mis_report_vat_grid_56",
    "mis_report_vat_grid_57",
    "mis_report_vat_grid_61",
    "mis_report_vat_grid_63",
    "mis_report_vat_grid_xx",
    "mis_report_vat_cadre_5",
    "mis_report_vat_grid_59",
    "mis_report_vat_grid_62",
    "mis_report_vat_grid_64",
    "mis_report_vat_grid_yy",
    "mis_report_vat_cadre_6",
    "mis_report_vat_grid_71",
    "mis_report_vat_grid_72",
    "mis_report_vat_control",
    "mis_report_vat_control_T",
    "mis_report_vat_control_U",
    "mis_report_vat_control_O",
    "mis_report_vat_control_P",
    "mis_report_vat_control_Q",
    "mis_report_vat_control_S",
    "mis_report_vat_control_70",
    "mis_report_vat_control_60",
]


@openupgrade.migrate()
def migrate(env, version):
    openupgradelib.set_xml_ids_noupdate_value(
        env, "l10n_be_mis_reports", _xmlids, True
    )
