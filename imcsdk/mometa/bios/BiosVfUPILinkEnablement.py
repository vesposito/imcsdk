"""This module contains the general information for BiosVfUPILinkEnablement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfUPILinkEnablementConsts:
    VP_UPILINK_ENABLEMENT_1 = "1"
    VP_UPILINK_ENABLEMENT_2 = "2"
    VP_UPILINK_ENABLEMENT_3 = "3"
    VP_UPILINK_ENABLEMENT_AUTO = "Auto"
    VP_UPILINK_ENABLEMENT_PLATFORM_DEFAULT = "platform-default"


class BiosVfUPILinkEnablement(ManagedObject):
    """This is BiosVfUPILinkEnablement class."""

    consts = BiosVfUPILinkEnablementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfUPILinkEnablement", "biosVfUPILinkEnablement", "UPI-Link-Enablement", VersionMeta.Version421b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_upi_link_enablement": MoPropertyMeta("vp_upi_link_enablement", "vpUPILinkEnablement", "string", VersionMeta.Version421b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1", "2", "3", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpUPILinkEnablement": "vp_upi_link_enablement", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_upi_link_enablement = None

        ManagedObject.__init__(self, "BiosVfUPILinkEnablement", parent_mo_or_dn, **kwargs)

