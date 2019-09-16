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
from swagger_client.models.sales_order_detail import SalesOrderDetail  # noqa: F401,E501


class SalesOrderHeader(object):
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
        'sales_order_id': 'int',
        'revision_number': 'int',
        'order_date': 'datetime',
        'due_date': 'datetime',
        'ship_date': 'datetime',
        'status': 'int',
        'online_order_flag': 'bool',
        'sales_order_number': 'str',
        'purchase_order_number': 'str',
        'account_number': 'str',
        'customer_id': 'int',
        'ship_to_address_id': 'int',
        'bill_to_address_id': 'int',
        'ship_method': 'str',
        'credit_card_approval_code': 'str',
        'sub_total': 'float',
        'tax_amt': 'float',
        'freight': 'float',
        'total_due': 'float',
        'comment': 'str',
        'rowguid': 'str',
        'modified_date': 'datetime',
        'bill_to_address': 'Address',
        'customer': 'Customer',
        'ship_to_address': 'Address',
        'sales_order_detail': 'list[SalesOrderDetail]'
    }

    attribute_map = {
        'sales_order_id': 'salesOrderId',
        'revision_number': 'revisionNumber',
        'order_date': 'orderDate',
        'due_date': 'dueDate',
        'ship_date': 'shipDate',
        'status': 'status',
        'online_order_flag': 'onlineOrderFlag',
        'sales_order_number': 'salesOrderNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'account_number': 'accountNumber',
        'customer_id': 'customerId',
        'ship_to_address_id': 'shipToAddressId',
        'bill_to_address_id': 'billToAddressId',
        'ship_method': 'shipMethod',
        'credit_card_approval_code': 'creditCardApprovalCode',
        'sub_total': 'subTotal',
        'tax_amt': 'taxAmt',
        'freight': 'freight',
        'total_due': 'totalDue',
        'comment': 'comment',
        'rowguid': 'rowguid',
        'modified_date': 'modifiedDate',
        'bill_to_address': 'billToAddress',
        'customer': 'customer',
        'ship_to_address': 'shipToAddress',
        'sales_order_detail': 'salesOrderDetail'
    }

    def __init__(self, sales_order_id=None, revision_number=None, order_date=None, due_date=None, ship_date=None, status=None, online_order_flag=None, sales_order_number=None, purchase_order_number=None, account_number=None, customer_id=None, ship_to_address_id=None, bill_to_address_id=None, ship_method=None, credit_card_approval_code=None, sub_total=None, tax_amt=None, freight=None, total_due=None, comment=None, rowguid=None, modified_date=None, bill_to_address=None, customer=None, ship_to_address=None, sales_order_detail=None):  # noqa: E501
        """SalesOrderHeader - a model defined in Swagger"""  # noqa: E501

        self._sales_order_id = None
        self._revision_number = None
        self._order_date = None
        self._due_date = None
        self._ship_date = None
        self._status = None
        self._online_order_flag = None
        self._sales_order_number = None
        self._purchase_order_number = None
        self._account_number = None
        self._customer_id = None
        self._ship_to_address_id = None
        self._bill_to_address_id = None
        self._ship_method = None
        self._credit_card_approval_code = None
        self._sub_total = None
        self._tax_amt = None
        self._freight = None
        self._total_due = None
        self._comment = None
        self._rowguid = None
        self._modified_date = None
        self._bill_to_address = None
        self._customer = None
        self._ship_to_address = None
        self._sales_order_detail = None
        self.discriminator = None

        if sales_order_id is not None:
            self.sales_order_id = sales_order_id
        if revision_number is not None:
            self.revision_number = revision_number
        if order_date is not None:
            self.order_date = order_date
        if due_date is not None:
            self.due_date = due_date
        if ship_date is not None:
            self.ship_date = ship_date
        if status is not None:
            self.status = status
        if online_order_flag is not None:
            self.online_order_flag = online_order_flag
        if sales_order_number is not None:
            self.sales_order_number = sales_order_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if account_number is not None:
            self.account_number = account_number
        if customer_id is not None:
            self.customer_id = customer_id
        if ship_to_address_id is not None:
            self.ship_to_address_id = ship_to_address_id
        if bill_to_address_id is not None:
            self.bill_to_address_id = bill_to_address_id
        if ship_method is not None:
            self.ship_method = ship_method
        if credit_card_approval_code is not None:
            self.credit_card_approval_code = credit_card_approval_code
        if sub_total is not None:
            self.sub_total = sub_total
        if tax_amt is not None:
            self.tax_amt = tax_amt
        if freight is not None:
            self.freight = freight
        if total_due is not None:
            self.total_due = total_due
        if comment is not None:
            self.comment = comment
        if rowguid is not None:
            self.rowguid = rowguid
        if modified_date is not None:
            self.modified_date = modified_date
        if bill_to_address is not None:
            self.bill_to_address = bill_to_address
        if customer is not None:
            self.customer = customer
        if ship_to_address is not None:
            self.ship_to_address = ship_to_address
        if sales_order_detail is not None:
            self.sales_order_detail = sales_order_detail

    @property
    def sales_order_id(self):
        """Gets the sales_order_id of this SalesOrderHeader.  # noqa: E501


        :return: The sales_order_id of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._sales_order_id

    @sales_order_id.setter
    def sales_order_id(self, sales_order_id):
        """Sets the sales_order_id of this SalesOrderHeader.


        :param sales_order_id: The sales_order_id of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._sales_order_id = sales_order_id

    @property
    def revision_number(self):
        """Gets the revision_number of this SalesOrderHeader.  # noqa: E501


        :return: The revision_number of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._revision_number

    @revision_number.setter
    def revision_number(self, revision_number):
        """Sets the revision_number of this SalesOrderHeader.


        :param revision_number: The revision_number of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._revision_number = revision_number

    @property
    def order_date(self):
        """Gets the order_date of this SalesOrderHeader.  # noqa: E501


        :return: The order_date of this SalesOrderHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this SalesOrderHeader.


        :param order_date: The order_date of this SalesOrderHeader.  # noqa: E501
        :type: datetime
        """

        self._order_date = order_date

    @property
    def due_date(self):
        """Gets the due_date of this SalesOrderHeader.  # noqa: E501


        :return: The due_date of this SalesOrderHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this SalesOrderHeader.


        :param due_date: The due_date of this SalesOrderHeader.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def ship_date(self):
        """Gets the ship_date of this SalesOrderHeader.  # noqa: E501


        :return: The ship_date of this SalesOrderHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this SalesOrderHeader.


        :param ship_date: The ship_date of this SalesOrderHeader.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def status(self):
        """Gets the status of this SalesOrderHeader.  # noqa: E501


        :return: The status of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SalesOrderHeader.


        :param status: The status of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def online_order_flag(self):
        """Gets the online_order_flag of this SalesOrderHeader.  # noqa: E501


        :return: The online_order_flag of this SalesOrderHeader.  # noqa: E501
        :rtype: bool
        """
        return self._online_order_flag

    @online_order_flag.setter
    def online_order_flag(self, online_order_flag):
        """Sets the online_order_flag of this SalesOrderHeader.


        :param online_order_flag: The online_order_flag of this SalesOrderHeader.  # noqa: E501
        :type: bool
        """

        self._online_order_flag = online_order_flag

    @property
    def sales_order_number(self):
        """Gets the sales_order_number of this SalesOrderHeader.  # noqa: E501


        :return: The sales_order_number of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._sales_order_number

    @sales_order_number.setter
    def sales_order_number(self, sales_order_number):
        """Sets the sales_order_number of this SalesOrderHeader.


        :param sales_order_number: The sales_order_number of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._sales_order_number = sales_order_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this SalesOrderHeader.  # noqa: E501


        :return: The purchase_order_number of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this SalesOrderHeader.


        :param purchase_order_number: The purchase_order_number of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def account_number(self):
        """Gets the account_number of this SalesOrderHeader.  # noqa: E501


        :return: The account_number of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SalesOrderHeader.


        :param account_number: The account_number of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def customer_id(self):
        """Gets the customer_id of this SalesOrderHeader.  # noqa: E501


        :return: The customer_id of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SalesOrderHeader.


        :param customer_id: The customer_id of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def ship_to_address_id(self):
        """Gets the ship_to_address_id of this SalesOrderHeader.  # noqa: E501


        :return: The ship_to_address_id of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._ship_to_address_id

    @ship_to_address_id.setter
    def ship_to_address_id(self, ship_to_address_id):
        """Sets the ship_to_address_id of this SalesOrderHeader.


        :param ship_to_address_id: The ship_to_address_id of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._ship_to_address_id = ship_to_address_id

    @property
    def bill_to_address_id(self):
        """Gets the bill_to_address_id of this SalesOrderHeader.  # noqa: E501


        :return: The bill_to_address_id of this SalesOrderHeader.  # noqa: E501
        :rtype: int
        """
        return self._bill_to_address_id

    @bill_to_address_id.setter
    def bill_to_address_id(self, bill_to_address_id):
        """Sets the bill_to_address_id of this SalesOrderHeader.


        :param bill_to_address_id: The bill_to_address_id of this SalesOrderHeader.  # noqa: E501
        :type: int
        """

        self._bill_to_address_id = bill_to_address_id

    @property
    def ship_method(self):
        """Gets the ship_method of this SalesOrderHeader.  # noqa: E501


        :return: The ship_method of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._ship_method

    @ship_method.setter
    def ship_method(self, ship_method):
        """Sets the ship_method of this SalesOrderHeader.


        :param ship_method: The ship_method of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._ship_method = ship_method

    @property
    def credit_card_approval_code(self):
        """Gets the credit_card_approval_code of this SalesOrderHeader.  # noqa: E501


        :return: The credit_card_approval_code of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_approval_code

    @credit_card_approval_code.setter
    def credit_card_approval_code(self, credit_card_approval_code):
        """Sets the credit_card_approval_code of this SalesOrderHeader.


        :param credit_card_approval_code: The credit_card_approval_code of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._credit_card_approval_code = credit_card_approval_code

    @property
    def sub_total(self):
        """Gets the sub_total of this SalesOrderHeader.  # noqa: E501


        :return: The sub_total of this SalesOrderHeader.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this SalesOrderHeader.


        :param sub_total: The sub_total of this SalesOrderHeader.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def tax_amt(self):
        """Gets the tax_amt of this SalesOrderHeader.  # noqa: E501


        :return: The tax_amt of this SalesOrderHeader.  # noqa: E501
        :rtype: float
        """
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, tax_amt):
        """Sets the tax_amt of this SalesOrderHeader.


        :param tax_amt: The tax_amt of this SalesOrderHeader.  # noqa: E501
        :type: float
        """

        self._tax_amt = tax_amt

    @property
    def freight(self):
        """Gets the freight of this SalesOrderHeader.  # noqa: E501


        :return: The freight of this SalesOrderHeader.  # noqa: E501
        :rtype: float
        """
        return self._freight

    @freight.setter
    def freight(self, freight):
        """Sets the freight of this SalesOrderHeader.


        :param freight: The freight of this SalesOrderHeader.  # noqa: E501
        :type: float
        """

        self._freight = freight

    @property
    def total_due(self):
        """Gets the total_due of this SalesOrderHeader.  # noqa: E501


        :return: The total_due of this SalesOrderHeader.  # noqa: E501
        :rtype: float
        """
        return self._total_due

    @total_due.setter
    def total_due(self, total_due):
        """Sets the total_due of this SalesOrderHeader.


        :param total_due: The total_due of this SalesOrderHeader.  # noqa: E501
        :type: float
        """

        self._total_due = total_due

    @property
    def comment(self):
        """Gets the comment of this SalesOrderHeader.  # noqa: E501


        :return: The comment of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SalesOrderHeader.


        :param comment: The comment of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def rowguid(self):
        """Gets the rowguid of this SalesOrderHeader.  # noqa: E501


        :return: The rowguid of this SalesOrderHeader.  # noqa: E501
        :rtype: str
        """
        return self._rowguid

    @rowguid.setter
    def rowguid(self, rowguid):
        """Sets the rowguid of this SalesOrderHeader.


        :param rowguid: The rowguid of this SalesOrderHeader.  # noqa: E501
        :type: str
        """

        self._rowguid = rowguid

    @property
    def modified_date(self):
        """Gets the modified_date of this SalesOrderHeader.  # noqa: E501


        :return: The modified_date of this SalesOrderHeader.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this SalesOrderHeader.


        :param modified_date: The modified_date of this SalesOrderHeader.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def bill_to_address(self):
        """Gets the bill_to_address of this SalesOrderHeader.  # noqa: E501


        :return: The bill_to_address of this SalesOrderHeader.  # noqa: E501
        :rtype: Address
        """
        return self._bill_to_address

    @bill_to_address.setter
    def bill_to_address(self, bill_to_address):
        """Sets the bill_to_address of this SalesOrderHeader.


        :param bill_to_address: The bill_to_address of this SalesOrderHeader.  # noqa: E501
        :type: Address
        """

        self._bill_to_address = bill_to_address

    @property
    def customer(self):
        """Gets the customer of this SalesOrderHeader.  # noqa: E501


        :return: The customer of this SalesOrderHeader.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SalesOrderHeader.


        :param customer: The customer of this SalesOrderHeader.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def ship_to_address(self):
        """Gets the ship_to_address of this SalesOrderHeader.  # noqa: E501


        :return: The ship_to_address of this SalesOrderHeader.  # noqa: E501
        :rtype: Address
        """
        return self._ship_to_address

    @ship_to_address.setter
    def ship_to_address(self, ship_to_address):
        """Sets the ship_to_address of this SalesOrderHeader.


        :param ship_to_address: The ship_to_address of this SalesOrderHeader.  # noqa: E501
        :type: Address
        """

        self._ship_to_address = ship_to_address

    @property
    def sales_order_detail(self):
        """Gets the sales_order_detail of this SalesOrderHeader.  # noqa: E501


        :return: The sales_order_detail of this SalesOrderHeader.  # noqa: E501
        :rtype: list[SalesOrderDetail]
        """
        return self._sales_order_detail

    @sales_order_detail.setter
    def sales_order_detail(self, sales_order_detail):
        """Sets the sales_order_detail of this SalesOrderHeader.


        :param sales_order_detail: The sales_order_detail of this SalesOrderHeader.  # noqa: E501
        :type: list[SalesOrderDetail]
        """

        self._sales_order_detail = sales_order_detail

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
        if issubclass(SalesOrderHeader, dict):
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
        if not isinstance(other, SalesOrderHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
