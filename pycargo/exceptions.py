import typing


class PyCargoException(Exception):
    pass


class InvalidHeaderException(PyCargoException):
    pass


class ValidationException(PyCargoException):
    def __init__(self, message: str):
        self.message = message
