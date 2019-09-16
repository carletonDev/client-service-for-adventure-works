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


class ErrorLog(object):
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
        'error_log_id': 'int',
        'error_time': 'datetime',
        'error_number': 'int',
        'error_severity': 'int',
        'error_state': 'int',
        'error_procedure': 'str',
        'error_line': 'int',
        'error_message': 'str'
    }

    attribute_map = {
        'error_log_id': 'errorLogId',
        'error_time': 'errorTime',
        'error_number': 'errorNumber',
        'error_severity': 'errorSeverity',
        'error_state': 'errorState',
        'error_procedure': 'errorProcedure',
        'error_line': 'errorLine',
        'error_message': 'errorMessage'
    }

    def __init__(self, error_log_id=None, error_time=None, error_number=None, error_severity=None, error_state=None, error_procedure=None, error_line=None, error_message=None):  # noqa: E501
        """ErrorLog - a model defined in Swagger"""  # noqa: E501

        self._error_log_id = None
        self._error_time = None
        self._error_number = None
        self._error_severity = None
        self._error_state = None
        self._error_procedure = None
        self._error_line = None
        self._error_message = None
        self.discriminator = None

        if error_log_id is not None:
            self.error_log_id = error_log_id
        if error_time is not None:
            self.error_time = error_time
        if error_number is not None:
            self.error_number = error_number
        if error_severity is not None:
            self.error_severity = error_severity
        if error_state is not None:
            self.error_state = error_state
        if error_procedure is not None:
            self.error_procedure = error_procedure
        if error_line is not None:
            self.error_line = error_line
        if error_message is not None:
            self.error_message = error_message

    @property
    def error_log_id(self):
        """Gets the error_log_id of this ErrorLog.  # noqa: E501


        :return: The error_log_id of this ErrorLog.  # noqa: E501
        :rtype: int
        """
        return self._error_log_id

    @error_log_id.setter
    def error_log_id(self, error_log_id):
        """Sets the error_log_id of this ErrorLog.


        :param error_log_id: The error_log_id of this ErrorLog.  # noqa: E501
        :type: int
        """

        self._error_log_id = error_log_id

    @property
    def error_time(self):
        """Gets the error_time of this ErrorLog.  # noqa: E501


        :return: The error_time of this ErrorLog.  # noqa: E501
        :rtype: datetime
        """
        return self._error_time

    @error_time.setter
    def error_time(self, error_time):
        """Sets the error_time of this ErrorLog.


        :param error_time: The error_time of this ErrorLog.  # noqa: E501
        :type: datetime
        """

        self._error_time = error_time

    @property
    def error_number(self):
        """Gets the error_number of this ErrorLog.  # noqa: E501


        :return: The error_number of this ErrorLog.  # noqa: E501
        :rtype: int
        """
        return self._error_number

    @error_number.setter
    def error_number(self, error_number):
        """Sets the error_number of this ErrorLog.


        :param error_number: The error_number of this ErrorLog.  # noqa: E501
        :type: int
        """

        self._error_number = error_number

    @property
    def error_severity(self):
        """Gets the error_severity of this ErrorLog.  # noqa: E501


        :return: The error_severity of this ErrorLog.  # noqa: E501
        :rtype: int
        """
        return self._error_severity

    @error_severity.setter
    def error_severity(self, error_severity):
        """Sets the error_severity of this ErrorLog.


        :param error_severity: The error_severity of this ErrorLog.  # noqa: E501
        :type: int
        """

        self._error_severity = error_severity

    @property
    def error_state(self):
        """Gets the error_state of this ErrorLog.  # noqa: E501


        :return: The error_state of this ErrorLog.  # noqa: E501
        :rtype: int
        """
        return self._error_state

    @error_state.setter
    def error_state(self, error_state):
        """Sets the error_state of this ErrorLog.


        :param error_state: The error_state of this ErrorLog.  # noqa: E501
        :type: int
        """

        self._error_state = error_state

    @property
    def error_procedure(self):
        """Gets the error_procedure of this ErrorLog.  # noqa: E501


        :return: The error_procedure of this ErrorLog.  # noqa: E501
        :rtype: str
        """
        return self._error_procedure

    @error_procedure.setter
    def error_procedure(self, error_procedure):
        """Sets the error_procedure of this ErrorLog.


        :param error_procedure: The error_procedure of this ErrorLog.  # noqa: E501
        :type: str
        """

        self._error_procedure = error_procedure

    @property
    def error_line(self):
        """Gets the error_line of this ErrorLog.  # noqa: E501


        :return: The error_line of this ErrorLog.  # noqa: E501
        :rtype: int
        """
        return self._error_line

    @error_line.setter
    def error_line(self, error_line):
        """Sets the error_line of this ErrorLog.


        :param error_line: The error_line of this ErrorLog.  # noqa: E501
        :type: int
        """

        self._error_line = error_line

    @property
    def error_message(self):
        """Gets the error_message of this ErrorLog.  # noqa: E501


        :return: The error_message of this ErrorLog.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ErrorLog.


        :param error_message: The error_message of this ErrorLog.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(ErrorLog, dict):
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
        if not isinstance(other, ErrorLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other