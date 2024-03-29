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

from swagger_client.models.product_description import ProductDescription  # noqa: F401,E501
from swagger_client.models.product_model import ProductModel  # noqa: F401,E501


class ProductModelProductDescription(object):
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
        'product_model_id': 'int',
        'product_description_id': 'int',
        'culture': 'str',
        'rowguid': 'str',
        'modified_date': 'datetime',
        'product_description': 'ProductDescription',
        'product_model': 'ProductModel'
    }

    attribute_map = {
        'product_model_id': 'productModelId',
        'product_description_id': 'productDescriptionId',
        'culture': 'culture',
        'rowguid': 'rowguid',
        'modified_date': 'modifiedDate',
        'product_description': 'productDescription',
        'product_model': 'productModel'
    }

    def __init__(self, product_model_id=None, product_description_id=None, culture=None, rowguid=None, modified_date=None, product_description=None, product_model=None):  # noqa: E501
        """ProductModelProductDescription - a model defined in Swagger"""  # noqa: E501

        self._product_model_id = None
        self._product_description_id = None
        self._culture = None
        self._rowguid = None
        self._modified_date = None
        self._product_description = None
        self._product_model = None
        self.discriminator = None

        if product_model_id is not None:
            self.product_model_id = product_model_id
        if product_description_id is not None:
            self.product_description_id = product_description_id
        if culture is not None:
            self.culture = culture
        if rowguid is not None:
            self.rowguid = rowguid
        if modified_date is not None:
            self.modified_date = modified_date
        if product_description is not None:
            self.product_description = product_description
        if product_model is not None:
            self.product_model = product_model

    @property
    def product_model_id(self):
        """Gets the product_model_id of this ProductModelProductDescription.  # noqa: E501


        :return: The product_model_id of this ProductModelProductDescription.  # noqa: E501
        :rtype: int
        """
        return self._product_model_id

    @product_model_id.setter
    def product_model_id(self, product_model_id):
        """Sets the product_model_id of this ProductModelProductDescription.


        :param product_model_id: The product_model_id of this ProductModelProductDescription.  # noqa: E501
        :type: int
        """

        self._product_model_id = product_model_id

    @property
    def product_description_id(self):
        """Gets the product_description_id of this ProductModelProductDescription.  # noqa: E501


        :return: The product_description_id of this ProductModelProductDescription.  # noqa: E501
        :rtype: int
        """
        return self._product_description_id

    @product_description_id.setter
    def product_description_id(self, product_description_id):
        """Sets the product_description_id of this ProductModelProductDescription.


        :param product_description_id: The product_description_id of this ProductModelProductDescription.  # noqa: E501
        :type: int
        """

        self._product_description_id = product_description_id

    @property
    def culture(self):
        """Gets the culture of this ProductModelProductDescription.  # noqa: E501


        :return: The culture of this ProductModelProductDescription.  # noqa: E501
        :rtype: str
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this ProductModelProductDescription.


        :param culture: The culture of this ProductModelProductDescription.  # noqa: E501
        :type: str
        """

        self._culture = culture

    @property
    def rowguid(self):
        """Gets the rowguid of this ProductModelProductDescription.  # noqa: E501


        :return: The rowguid of this ProductModelProductDescription.  # noqa: E501
        :rtype: str
        """
        return self._rowguid

    @rowguid.setter
    def rowguid(self, rowguid):
        """Sets the rowguid of this ProductModelProductDescription.


        :param rowguid: The rowguid of this ProductModelProductDescription.  # noqa: E501
        :type: str
        """

        self._rowguid = rowguid

    @property
    def modified_date(self):
        """Gets the modified_date of this ProductModelProductDescription.  # noqa: E501


        :return: The modified_date of this ProductModelProductDescription.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this ProductModelProductDescription.


        :param modified_date: The modified_date of this ProductModelProductDescription.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def product_description(self):
        """Gets the product_description of this ProductModelProductDescription.  # noqa: E501


        :return: The product_description of this ProductModelProductDescription.  # noqa: E501
        :rtype: ProductDescription
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this ProductModelProductDescription.


        :param product_description: The product_description of this ProductModelProductDescription.  # noqa: E501
        :type: ProductDescription
        """

        self._product_description = product_description

    @property
    def product_model(self):
        """Gets the product_model of this ProductModelProductDescription.  # noqa: E501


        :return: The product_model of this ProductModelProductDescription.  # noqa: E501
        :rtype: ProductModel
        """
        return self._product_model

    @product_model.setter
    def product_model(self, product_model):
        """Sets the product_model of this ProductModelProductDescription.


        :param product_model: The product_model of this ProductModelProductDescription.  # noqa: E501
        :type: ProductModel
        """

        self._product_model = product_model

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
        if issubclass(ProductModelProductDescription, dict):
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
        if not isinstance(other, ProductModelProductDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
