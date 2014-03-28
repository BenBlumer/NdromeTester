#    Ndrome Tester
#    Copyright (C) 2013  Benjamin Blumer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/
#
#
#    This was a script written for the Microsoft Coding Challenge at UBC.
#    It can check whether a specified string, with a specified n, is an
#    ndrome. The string must be divisible by n for this to work.
#    The definition of an ndrome, the problem statement, and the output
#    format are given in the included "Problem.txt". Note: additional
#    information was given by the person running the session. "All strings
#    will be divisible by n".

import math


def open_file(filename):
    """Open a file and return the file object.

    Not very exciting. It just makes sure the file gets opened in read mode.

    args:
      filename: a string of the file name/full path of the file to open.

    returns:
      f: A file object in read mode.
      """
    f = open(filename, 'r')
    return f


def split_string(string_to_split, n):
    """Break a string into _n-length partitions.

    The string must be divisible by _n.

    args:
      string_to_split: A string that's length is an integer multiple of _n.
      _n: an integer.
    returns:
      parts_of_string: A list containing the _n-length strings that make up
        string_to_split.
    """
    assert(len(string_to_split) % n == 0)

    parts_of_string = []
    for i in xrange(0, len(string_to_split), n):
        parts_of_string.append(string_to_split[i:i+n])
    return parts_of_string


class OneLine(object):
    def __init__(self, n, list_of_strings, full_string):
        self._n = n
        self._list_of_strings = list_of_strings
        self._full_string = full_string
        self._is_ndrome = False
        self._number_of_strings = len(list_of_strings)


def ReadFileLine(inp_file):
    """
    Read one line from a file, return an object containing a parsed description.

    Break it into a list of n-length strings, calculate how many of these
    strings are required, and extract n.

    args:
      inp_file: a file object opened in read mode.

    returns:
      this_line_info: a OneLine object containing all of the information about
        the read line.
    """

    inp_line = inp_file.readline()
    # The pipe character separates the string from the n value.
    contents_and_n = inp_line.split("|")
    # Extract n, and strip formatting characters.
    n = int(contents_and_n[1][0])
    # Extract the string.
    stringbit = contents_and_n[0]
    # Divide the string into n-length partitions
    partitions_of_string = split_string(stringbit, n)
    this_line_info = OneLine(n,partitions_of_string,inp_line)
    return this_line_info


def CheckIfNDdrome(line_info):
    """
    Take a OneLine object, return true if it contains an ndrome.

    args:
      line_info: a OneLine object. It should already have its _n,
        _list_of_strings, _full_string, and _number_of_strings
        members set by, for example, ReadFileLine().

    returns:
      still_ndrome: True if the _full_string contains an ndrome. Otherwise,
        false.
    """
    # See if there's an odd number of n-length strings. If so, this returns 1.
    # If it's even, it returns 0;
    is_odd = line_info._number_of_strings % 2

    #If it's odd, we don't need to check the middle string
    if is_odd == 1:
        number_of_string_pairs_to_investigate = int(math.floor(line_info._number_of_strings / 2))
    else:
        number_of_string_pairs_to_investigate = int(math.ceil(line_info._number_of_strings / 2))

    still_ndrome = True
    for i in xrange(0,number_of_string_pairs_to_investigate):
        if line_info._list_of_strings[i] != line_info._list_of_strings[-i -1]:
            still_ndrome = False

    return still_ndrome


if __name__ == "__main__":
    input_file = open_file("SampleInput.txt")

    number_of_lines_in_file = 0
    for line in input_file:
        number_of_lines_in_file += 1
    input_file.seek(0)
    print "The file contains " + str(number_of_lines_in_file) + " lines"
    output_file = open("output.txt","w")

    for i in xrange(number_of_lines_in_file):
        one_line = ReadFileLine(input_file)
        ans = CheckIfNDdrome(one_line)
        if ans == True:
            ans = 1
        else:
            ans = 0
        output_file.write(one_line._full_string.rstrip() + "|" + str(ans) + "\n")

