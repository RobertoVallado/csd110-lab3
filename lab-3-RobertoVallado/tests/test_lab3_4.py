import sys
import re
import util

expected_output = '''#   #
## ##
# # #
#   #
#   #

 ###
  #
  #
  #
 ###

 ####
#
 ###
    #
####

 ####
#
 ###
    #
####

 ###
  #
  #
  #
 ###

 ####
#
 ###
    #
####

 ####
#
 ###
    #
####

 ###
  #
  #
  #
 ###

####
#   #
####
#
#

####
#   #
####
#
#

 ###
  #
  #
  #
 ###
'''

def test_output_is_correct(capsys):
    if 'src.lab3_4' in sys.modules.keys():
        sys.modules.pop('src.lab3_4')
    import src.lab3_4
    out, err = capsys.readouterr()
    assert out == expected_output, util.format_message("Script produces incorrect output", expected_output, out)