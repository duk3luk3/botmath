botmath
=======

A small calculator language with dicerolls

Example usage
=============

    ~/git/botmath/botmath(master)$ python2
    Python 2.7.8 (default, Sep 24 2014, 18:58:24) 
    [GCC 4.9.1 20140903 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import botmath as bm
    >>> b = bm.BotMath()
    >>> b.parse("5+5")
    10
    >>> b.parse("(3d6+5) / 2")
    8
    >>> b.parse("(3d6+5) / 2")
    8
    >>> b.parse("(3d6+5) / 2")
    6
    >>> b.parse("(3d6+5) / 2")
    6
