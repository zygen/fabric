.. image:: https://secure.travis-ci.org/fabric/fabric.png?branch=v2
        :target: https://travis-ci.org/fabric/fabric

Fabric is a Python 2.6-3.x compatible library for executing remote system
commands via the SSH protocol. It builds on top of `Paramiko
<http://paramiko.org>`_'s low-level SSH functionality, and optionally leverages
`Invoke <http://pyinvoke.org>`_ for command-line task execution.

Our feature set focuses on three core areas:

* **Execution**: invoking remote shell commands (directly or via wrappers like
  ``sudo``) and uploading/downloading files and directories.
* **Orchestration**: determining what execution code is run against which
  remote servers, and in what fashion (serially, in parallel, etc).
* **SSH behavior**: high level control over the various facets of the SSH
  ecosystem such as config file loading, connection retries, gateway support
  and so forth.

The most basic form of the API is a simple ``Connection`` object exposing primitives
like ``run``, ``get`` etc::

    >>> from fabric import Connection
    >>> result = Connection('example.com').run('uname -sr')
    >>> print(result.stdout)
    Linux 2.6.32-5-xen-amd64
    >>> print(result.exited)
    0

Connection objects can be given subroutines (via ``execute``), which they will run
with themselves as the first argument::

    >>> from fabric import Connection
    >>> def disk_usage(host):
    ...     result = host.run('df /dev/sda1')
    ...     header, info = result.stdout.splitlines()
    ...     cols = header.split()
    ...     return info.split()[cols.index('Use%')]
    >>> percentile = Connection('foo.com').execute(disk_usage)
    >>> print("foo.com sda1 is {0} full".format(percentile))
    foo.com sda1 is 18% full

Want to run the same commands or subroutines across multiple connections? Enter
``Batch``, which has a similar API as ``Connection`` (except results are dicts
keyed by the batch's member Connection objects)::

    >>> from fabric import Batch
    >>> batch = Batch('web1.example.com', 'web2.example.com')
    >>> results = batch.run('hostname')
    >>> print(results.keys())
    [Connection('web1.example.com'), Connection('web2.example.com')]
    >>> for x in results.values()
    ...     print(x.stdout)
    web1
    web2

CLI (invoke) leveraging example
