"""Service Group Object."""

from fortigate_api.base import Base


class ServiceGroup(Base):
    """Service Group Object.

    - Web UI: https://hostname/ng/firewall/service
    - API: https://hostname/api/v2/cmdb/firewall.service/group
    - Data: :ref:`ServiceGroup.yml`
    """

    def __init__(self, rest):
        """Init Service Group Object.

        :param rest: :ref:`Fortigate` REST API connector.
        :type rest: Fortigate
        """
        super().__init__(rest=rest, url_obj="api/v2/cmdb/firewall.service/group/")
