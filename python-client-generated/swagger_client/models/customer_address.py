# coding: utf-8

"""
    AdventureWorksAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.address import Address  # noqa: F401,E501
from swagger_client.models.customer import Customer  # noqa: F401,E501


class CustomerAddress(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer_id': 'int',
        'address_id': 'int',
        'address_type': 'str',
        'rowguid': 'str',
        'modified_date': 'datetime',
        'address': 'Address',
        'customer': 'Customer'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'address_id': 'addressId',
        'address_type': 'addressType',
        'rowguid': 'rowguid',
        'modified_date': 'modifiedDate',
        'address': 'address',
        'customer': 'customer'
    }

    def __init__(self, customer_id=None, address_id=None, address_type=None, rowguid=None, modified_date=None, address=None, customer=None):  # noqa: E501
        """CustomerAddress - a model defined in Swagger"""  # noqa: E501

        self._customer_id = None
        self._address_id = None
        self._address_type = None
        self._rowguid = None
        self._modified_date = None
        self._address = None
        self._customer = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if address_id is not None:
            self.address_id = address_id
        if address_type is not None:
            self.address_type = address_type
        if rowguid is not None:
            self.rowguid = rowguid
        if modified_date is not None:
            self.modified_date = modified_date
        if address is not None:
            self.address = address
        if customer is not None:
            self.customer = customer

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerAddress.  # noqa: E501


        :return: The customer_id of this CustomerAddress.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerAddress.


        :param customer_id: The customer_id of this CustomerAddress.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def address_id(self):
        """Gets the address_id of this CustomerAddress.  # noqa: E501


        :return: The address_id of this CustomerAddress.  # noqa: E501
        :rtype: int
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this CustomerAddress.


        :param address_id: The address_id of this CustomerAddress.  # noqa: E501
        :type: int
        """

        self._address_id = address_id

    @property
    def address_type(self):
        """Gets the address_type of this CustomerAddress.  # noqa: E501


        :return: The address_type of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this CustomerAddress.


        :param address_type: The address_type of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def rowguid(self):
        """Gets the rowguid of this CustomerAddress.  # noqa: E501


        :return: The rowguid of this CustomerAddress.  # noqa: E501
        :rtype: str
        """
        return self._rowguid

    @rowguid.setter
    def rowguid(self, rowguid):
        """Sets the rowguid of this CustomerAddress.


        :param rowguid: The rowguid of this CustomerAddress.  # noqa: E501
        :type: str
        """

        self._rowguid = rowguid

    @property
    def modified_date(self):
        """Gets the modified_date of this CustomerAddress.  # noqa: E501


        :return: The modified_date of this CustomerAddress.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CustomerAddress.


        :param modified_date: The modified_date of this CustomerAddress.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def address(self):
        """Gets the address of this CustomerAddress.  # noqa: E501


        :return: The address of this CustomerAddress.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerAddress.


        :param address: The address of this CustomerAddress.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def customer(self):
        """Gets the customer of this CustomerAddress.  # noqa: E501


        :return: The customer of this CustomerAddress.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerAddress.


        :param customer: The customer of this CustomerAddress.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CustomerAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
