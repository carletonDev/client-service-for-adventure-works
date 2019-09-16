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

from swagger_client.models.product import Product  # noqa: F401,E501
from swagger_client.models.product_category import ProductCategory  # noqa: F401,E501


class ProductCategory(object):
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
        'product_category_id': 'int',
        'parent_product_category_id': 'int',
        'name': 'str',
        'rowguid': 'str',
        'modified_date': 'datetime',
        'parent_product_category': 'ProductCategory',
        'inverse_parent_product_category': 'list[ProductCategory]',
        'product': 'list[Product]'
    }

    attribute_map = {
        'product_category_id': 'productCategoryId',
        'parent_product_category_id': 'parentProductCategoryId',
        'name': 'name',
        'rowguid': 'rowguid',
        'modified_date': 'modifiedDate',
        'parent_product_category': 'parentProductCategory',
        'inverse_parent_product_category': 'inverseParentProductCategory',
        'product': 'product'
    }

    def __init__(self, product_category_id=None, parent_product_category_id=None, name=None, rowguid=None, modified_date=None, parent_product_category=None, inverse_parent_product_category=None, product=None):  # noqa: E501
        """ProductCategory - a model defined in Swagger"""  # noqa: E501

        self._product_category_id = None
        self._parent_product_category_id = None
        self._name = None
        self._rowguid = None
        self._modified_date = None
        self._parent_product_category = None
        self._inverse_parent_product_category = None
        self._product = None
        self.discriminator = None

        if product_category_id is not None:
            self.product_category_id = product_category_id
        if parent_product_category_id is not None:
            self.parent_product_category_id = parent_product_category_id
        if name is not None:
            self.name = name
        if rowguid is not None:
            self.rowguid = rowguid
        if modified_date is not None:
            self.modified_date = modified_date
        if parent_product_category is not None:
            self.parent_product_category = parent_product_category
        if inverse_parent_product_category is not None:
            self.inverse_parent_product_category = inverse_parent_product_category
        if product is not None:
            self.product = product

    @property
    def product_category_id(self):
        """Gets the product_category_id of this ProductCategory.  # noqa: E501


        :return: The product_category_id of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._product_category_id

    @product_category_id.setter
    def product_category_id(self, product_category_id):
        """Sets the product_category_id of this ProductCategory.


        :param product_category_id: The product_category_id of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._product_category_id = product_category_id

    @property
    def parent_product_category_id(self):
        """Gets the parent_product_category_id of this ProductCategory.  # noqa: E501


        :return: The parent_product_category_id of this ProductCategory.  # noqa: E501
        :rtype: int
        """
        return self._parent_product_category_id

    @parent_product_category_id.setter
    def parent_product_category_id(self, parent_product_category_id):
        """Sets the parent_product_category_id of this ProductCategory.


        :param parent_product_category_id: The parent_product_category_id of this ProductCategory.  # noqa: E501
        :type: int
        """

        self._parent_product_category_id = parent_product_category_id

    @property
    def name(self):
        """Gets the name of this ProductCategory.  # noqa: E501


        :return: The name of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductCategory.


        :param name: The name of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rowguid(self):
        """Gets the rowguid of this ProductCategory.  # noqa: E501


        :return: The rowguid of this ProductCategory.  # noqa: E501
        :rtype: str
        """
        return self._rowguid

    @rowguid.setter
    def rowguid(self, rowguid):
        """Sets the rowguid of this ProductCategory.


        :param rowguid: The rowguid of this ProductCategory.  # noqa: E501
        :type: str
        """

        self._rowguid = rowguid

    @property
    def modified_date(self):
        """Gets the modified_date of this ProductCategory.  # noqa: E501


        :return: The modified_date of this ProductCategory.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this ProductCategory.


        :param modified_date: The modified_date of this ProductCategory.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def parent_product_category(self):
        """Gets the parent_product_category of this ProductCategory.  # noqa: E501


        :return: The parent_product_category of this ProductCategory.  # noqa: E501
        :rtype: ProductCategory
        """
        return self._parent_product_category

    @parent_product_category.setter
    def parent_product_category(self, parent_product_category):
        """Sets the parent_product_category of this ProductCategory.


        :param parent_product_category: The parent_product_category of this ProductCategory.  # noqa: E501
        :type: ProductCategory
        """

        self._parent_product_category = parent_product_category

    @property
    def inverse_parent_product_category(self):
        """Gets the inverse_parent_product_category of this ProductCategory.  # noqa: E501


        :return: The inverse_parent_product_category of this ProductCategory.  # noqa: E501
        :rtype: list[ProductCategory]
        """
        return self._inverse_parent_product_category

    @inverse_parent_product_category.setter
    def inverse_parent_product_category(self, inverse_parent_product_category):
        """Sets the inverse_parent_product_category of this ProductCategory.


        :param inverse_parent_product_category: The inverse_parent_product_category of this ProductCategory.  # noqa: E501
        :type: list[ProductCategory]
        """

        self._inverse_parent_product_category = inverse_parent_product_category

    @property
    def product(self):
        """Gets the product of this ProductCategory.  # noqa: E501


        :return: The product of this ProductCategory.  # noqa: E501
        :rtype: list[Product]
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ProductCategory.


        :param product: The product of this ProductCategory.  # noqa: E501
        :type: list[Product]
        """

        self._product = product

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
        if issubclass(ProductCategory, dict):
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
        if not isinstance(other, ProductCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
