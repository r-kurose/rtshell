# -*- Python -*-
# -*- coding: utf-8 -*-

'''rtshell

Copyright (C) 2009-2010
    Geoffrey Biggs
    RT-Synthesis Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
Licensed under the Eclipse Public License -v 1.0 (EPL)
http://www.opensource.org/licenses/eclipse-1.0.txt

Exceptions that may occur.

'''


import rtctree.path


class RtShellError(Exception):
    '''Base error for all errors that may occur.'''
    pass


class RequiredActionFailedError(RtShellError):
    '''Error raised when an action that must succeed fails.'''
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return 'Required action failed: {0}'.format(self._msg)


class PrecedingTimeoutError(RtShellError):
    '''The time limit on a preceding condition being met has elapsed.'''
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return 'Preceding condition timed out: {0}'.format(self._msg)


class EmptyConstExprError(RtShellError):
    '''A constant expression that should be evaluated is empty.'''
    def __str__(self):
        return 'Empty constant expression '


class AmbiguousTypeError(RtShellError):
    '''A data type is ambiguous.'''
    def __init__(self, type):
        self._type = type

    def __str__(self):
        return 'Ambiguous port type: {0}'.format(self._type)


class TypeNotFoundError(RtShellError):
    '''A data type was not found.'''
    def __init__(self, type):
        self._type = type

    def __str__(self):
        return 'Type not found: {0}'.format(self._type)


class BadPortSpecError(RtShellError):
    '''A port specification is badly formatted.'''
    def __init__(self, ps):
        self._ps = ps

    def __str__(self):
        return 'Bad port specification: {0}'.format(self._ps)


class SameNameDiffSpecError(RtShellError):
    '''A port spec has a different property from another with the same name.'''
    def __init__(self, ps):
        self._ps = ps

    def __str__(self):
        return 'Port specification with same name has different properties: '\
                '{0}'.format(self._ps)


class NoSuchObjectError(RtShellError):
    '''The given path does not point to the necessary object.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'No such object: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'No such object: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'No such object: {0}'.format(self._path)


class NotAComponentError(RtShellError):
    '''A given path is not a component.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Not a component: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Not a component: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Not a component: {0}'.format(self._path)


class ParentNotADirectoryError(RtShellError):
    '''A given path's parent is not a directory.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Parent not a directory: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Parent not a directory: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Parent not a directory: {0}'.format(self._path)


class NotADirectoryError(RtShellError):
    '''A given path is not a directory.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Not a directory: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Not a directory: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Not a directory: {0}'.format(self._path)


class NotAPortError(RtShellError):
    '''A given path is not a port.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Not a port: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Not a port: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Not a port: {0}'.format(self._path)


class NotInManagerError(RtShellError):
    '''A component name does not exist in a manager.'''
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return '{0} is not in the manager.'.format(self._name)


class UndeletableObjectError(RtShellError):
    '''Some objects cannot be deleted.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Undeletable object: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Undeletable object: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Undeletable object: {0}'.format(self._path)


class NotZombieObjectError(RtShellError):
    '''A given path does not point to a zombie.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Not a zombie object: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Not a zombie object: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Not a zombie object: {0}'.format(self._path)


class ZombieObjectError(RtShellError):
    '''A given path points to a zombie.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'Zombie object: {0}'.format(
                    rtctree.path.format_path(self._path))
        elif type(self._path) == list:
            return 'Zombie object: {0}'.format(
                    rtctree.path.format_path((self._path, None)))
        else:
            return 'Zombie object: {0}'.format(self._path)


class NoDestPortError(RtShellError):
    '''A required destination port was not specified.'''
    def __str__(self):
        return 'No destination port specified.'


class NoSourcePortError(RtShellError):
    '''A required source port was not specified.'''
    def __str__(self):
        return 'No source port specified.'


class PortNotFoundError(RtShellError):
    '''The port was not found on the component.'''
    def __init__(self, rtc, port):
        self._rtc = rtc
        self._port = port

    def __str__(self):
        return 'Port not found: {0}'.format(
                rtctree.path.format_path((self._rtc, self._port)))


class ConnectionNotFoundError(RtShellError):
    '''The port was not found on the component.'''
    def __init__(self, path1, path2):
        self._path1 = path1
        self._path2 = path2

    def __str__(self):
        if type(self._path) == tuple:
            return 'No connection from {0} to {1}.'.format(
                    rtctree.path.format_path(self._path1), self._path2)
        elif type(self._path) == list:
            return 'No connection from {0} to {1}.'.format(
                    rtctree.path.format_path((self._path, None)), self._path2)
        else:
            return 'No connection from {0} to {1}'.format(self._path,
                    self._path2)


class ConnectionIDNotFoundError(RtShellError):
    '''The port was not found on the component.'''
    def __init__(self, id, path):
        self._id = id
        self._path = path

    def __str__(self):
        if type(self._path) == tuple:
            return 'No connection from {0} with ID {1}.'.format(
                    rtctree.path.format_path(self._path), self._id)
        elif type(self._path) == list:
            return 'No connection from {0} with ID {1}.'.format(
                    rtctree.path.format_path((self._path, None)), self._id)
        else:
            return 'No connection from {0} with ID {1}'.format(self._path,
                    self._id)


class BadPortTypeError(RtShellError):
    '''The port type is not defined.'''
    def __init__(self, rtc, port):
        self._rtc = rtc
        self._port = port

    def __str__(self):
        return 'Incorrect port type: {0}'.format(
                rtctree.path.format_path((self._rtc, self._port)))


class MissingCompError(RtShellError):
    '''An expected component is missing.'''
    def __init__(self, path):
        self._path = path

    def __str__(self):
        return 'Expected component missing: {0}'.format(self._path)


class ConnectFailedError(RtShellError):
    '''An error occured connecting two ports.'''
    def __init__(self, rtc, port):
        self._rtc = rtc
        self._port = port

    def __str__(self):
        return 'Failed to connect port: {0}'.format(
                rtctree.path.format_path((self._rtc, self._port)))


class ActivateError(RtShellError):
    '''An error occured activating a component.'''
    def __init__(self, comp):
        self._comp = comp

    def __str__(self):
        return 'Error activating component: {0}'.format(self._comp)


class DeactivateError(RtShellError):
    '''An error occured deactivating a component.'''
    def __init__(self, comp):
        self._comp = comp

    def __str__(self):
        return 'Error deactivating component: {0}'.format(self._comp)


class PortNotInputError(RtShellError):
    '''A port is not an input that should be.'''
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Port is not input: {0}'.format(self._name)


class PortNotOutputError(RtShellError):
    '''A port is not an output that should be.'''
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Port is not output: {0}'.format(self._name)


class ImportFormatterError(RtShellError):
    '''An error occured importing a formatting function.'''
    def __init__(self, exc):
        self._exc = exc

    def __str__(self):
        return 'Error importing formatter: {0}'.format(self._exc)


class BadFormatterError(RtShellError):
    '''The imported formatter is bad (most likely not a function).'''
    def __init__(self, fun):
        self._fun = fun

    def __str__(self):
        return 'Bad formatter: {0}'.format(self._fun)


class MissingPOAError(RtShellError):
    '''A data type from a module was used without a matching POA loaded.'''
    def __init__(self, mod):
        self._mod = mod

    def __str__(self):
        return 'Missing POA module: {0}'.format(self._mod)


class NoConfSetError(RtShellError):
    '''The specified configuration set does not exist.'''
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'No such configuration set: {0}'.format(self._name)


# vim: tw=79

