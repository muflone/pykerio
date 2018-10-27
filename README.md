# PyKerio

[![Travis CI Build Status](https://img.shields.io/travis/muflone/pykerio/master.svg)](https://travis-ci.org/muflone/pykerio)
[![CircleCI Build Status](https://img.shields.io/circleci/project/github/muflone/pykerio/master.svg)](https://circleci.com/gh/muflone/pykerio)
[![PyPI - Version](https://img.shields.io/pypi/v/PyKerio.svg)](https://pypi.org/project/PyKerio/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PyKerio.svg)](https://pypi.org/project/PyKerio/)
[![Coveralls Status](https://img.shields.io/coveralls/github/muflone/pykerio/master.svg)](https://coveralls.io/github/muflone/pykerio?branch=master)

**Description:** API for Kerio products

**Copyright:** 2018 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-2+

**Source code:** https://github.com/muflone/pykerio

**Documentation:** http://www.muflone.com/pykerio/

# Description

PyKerio is an attempt to build a common API to interact with any
[**Kerio**](https://www.kerio.com/) server in order to operate using external
tools and simple provisioning scripts.

The interaction will make use of HTTP requests over the integrated Kerio web
server in the same way the classic Kerio Web administration does.

# System Requirements

* Python 3.x

# PyKerio Types

The original [**Kerio API**](https://manuals.gfi.com/en/kerio/api/index.htm)
interacts with the Kerio servers using JSON data but in PyKerio you can find a
lot of classes to map the JSON raw data to Python objects, in order to ease the
usage and to check for invalid data types.

The PyKerio data types are split in 4 groups:

- Simple types
- Enumerations
- Structures
- Lists

All the PyKerio types can be casted to string or JSON data using
the ```.dump()``` method on an instance object.

### PyKerio simple types

The **PyKerio simple types** can be found in ```pykerio.types``` and are simple
classes that map to Python raw data.

The reason behind the PyKerio simple types is to bound a specific type to some
functions.
For example whenever a method requires an ```IpAddress``` type you can instance
a new ```IpAddress``` object which basically wraps a string representing an IPv4
address.

Their usage is rather simple:

    >>> ip_address = pykerio.types.IpAddress('8.8.8.8')
    >>> print(ip_address)
    '8.8.8.8'

### PyKerio enumerations

The **PyKerio enumerations** can be found in ```pykerio.enums``` and are simple
classes that refer to a finished set of strings. They can be used in place of
strings when a function expects a particular constant value.

The reason behind the PyKerio Enumerations is to limit the usage of invalid
strings and to know the only admitted values for an argument.
For example whenever a method requires an ```ActiveTool``` data type you can
instance a new ```ActiveTool``` object passing its value during the object
creation. This value will be initially checked and invalid values cannot be
specified.

Their usage is shown here:

    >>> tool = pykerio.enums.ActiveTool('ActiveToolDns')
    >>> print(tool.dump())
    'ActiveToolDns'

Invalid arguments cannot be specified during the object creation. The following
instructions will raise an AssertionError.

    >>> tool = pykerio.enums.ActiveTool('Invalid value')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "pykerio/enums/BaseEnumeration.py", line 29, in __init__
        assert(name in self.VALUES)
    AssertionError

In this way you can safely pass objects to functions without any risk for
invalid values as they would be automatically forbidden.

### PyKerio structures

The **PyKerio Structures** can be found in ```pykerio.structs``` and are complex
classes with two or more members.

You cannot instanciate a PyKerio Structure without expliciting all its members
values. Their usage requires the pass of a dictionary with all its names and
values.
For example whenever a function requires you to pass an ```ApiApplication```
object you can instance it in this way:

    application = pykerio.structs.ApiApplication({
        'name': 'My application',
        'vendor': 'Fabio Castelli',
        'version': '1.1.2'})

Some PyKerio structures can be very complex as they contain a lot of members and
each member can be another PyKerio structure or a list of many other Python
structures.

### PyKerio lists

The **PyKerio Lists** can be found in ```pykerio.lists``` can be considered as
lists of a fixed and immutable data types.

The reason behind the PyKerio lists is to group a list a homogeneous objects of
the same type.

For example whenever a function needs an ```IpAddressList``` object you can
instance an ```IpAddressList``` and fill it with as many ```IpAddress``` objects
you need.

There are two ways to fill a PyKerio list with objects:

- At the creation time:

      iplist = pykerio.lists.IpAddressList([ip1], [ip2], [ip3])

- After creation:

      iplist = pykerio.lists.IpAddressList()
      iplist.append(ip1)
      iplist.append(ip2)
      iplist.append(ip3)

You cannot put inside a PyKerio list an object of a different type.

# Implemented interfaces

The following interfaces are implemented under ```pykerio.interfaces```:

- Session
- HardwareInfo
- Interfaces
- Ports
- FilenameGroups
- Server
- Storage
- IpTools

Every needed simple type, structure, enumeration or list to implement or use
these interfaces it's also present, ready to be used.

# Usage examples

The very first step to interact with a Kerio server is to instance
a ```PyKerio``` object but the ```PyKerio``` class cannot be directly instanciated
but needs to be instanciated through ```PyKerioControl``` or ```PyKerioConnect```
classes.

The next step is to login to the server using valid username and password.
Every other commands require a successful login session.

Many usage examples can be found in the ```tests``` folder as they are used
to test the API operation.

### Login

    >>> import pykerio
    >>> import ssl
    >>> ssl._create_default_https_context = ssl._create_unverified_context
    >>> api = pykerio.PyKerioControl(server='control-demo.kerio.com',
                                     port=4081)
    >>> application = pykerio.structs.ApiApplication({'name': pykerio.APP_NAME,
                                                      'vendor': pykerio.APP_AUTHOR,
                                                      'version': pykerio.APP_VERSION})
    >>> session = pykerio.interfaces.Session(api)
    >>> session.login('admin-en', 'kerio', application)

### Logout

    >>> session.logout()


# What about the missing interfaces?

The ```PyKerio``` module offers a method called ```request_rpc``` which allows
you to launch direct commands to the Kerio server just by providing the method
name and its input parameters in a JSON array.

After a successful login you can interact using the ```request_rpc``` method in
the following way:

    >>> response = api.request_rpc(method='HardwareInfo.getBoxSerialNumber',
                                   params={})
    >>> print(response.result)
    {'serialNumber': 'LNKR17123456'}

A more complex example using raw JSON input arguments:

    >>> response = api.request_rpc(method='SystemHealth.get',
                                   params={'type': 'HistogramOneDay'})
    >>> print(response.result['data']['diskTotal'])
    29239369728
    >>> print(response.result['data']['diskFree'])
    28010360832

The same example using the PyKerio ```HistogramType``` class can also be written
like this:

    >>> from pykerio.enums import HistogramType
    >>> response = api.request_rpc(method='SystemHealth.get',
                                   params={'type': HistogramType('HistogramOneDay')})
    >>> print(response.result['data']['diskTotal'])
    29239369728
    >>> print(response.result['data']['diskFree'])
    28010360832

The ```request_rpc``` method will automatically convert the PyKerio types
(from ```pykerio.structs```, ```pykerio.lists```, ```pykerio.enums``` and
```pykerio.types```) to JSON raw data.
