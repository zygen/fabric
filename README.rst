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

Core example::

    >> from fabric.blah import Host
    >> result = Host('foo.com').run('command')
    <no stdout/err printed by default!>
    >> show shit on result

Function-oriented example::

    >> from fabric import Host
    >> def mytask(host):
    >>     host.run('command')
    >> Host('foo.com').execute(mytask)

Host collection/list example

CLI (invoke) leveraging example
