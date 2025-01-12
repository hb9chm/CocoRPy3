#-------------------------------------------------------------------------
#ParserGen.py -- Main compiler file generation routines.
#Compiler Generator Coco/R,
#Copyright (c) 1990, 2004 Hanspeter Moessenboeck, University of Linz
#extended by M. Loeberbauer & A. Woess, Univ. of Linz
#ported from Java to Python by Ronald Longo
#
#This program is free software; you can redistribute it and/or modify it
#under the terms of the GNU General Public License as published by the
#Free Software Foundation; either version 2, or (at your option) any
#later version.
#
#This program is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
#As an exception, it is allowed to write an extension of Coco/R that is
#used as a plugin in non-free software.
#
#If not otherwise stated, any source code generated by Coco/R (other than
#Coco/R itself) does not fall under the GNU General Public License.
#-------------------------------------------------------------------------*/
import os
import os.path
from Errors import Errors
from Core import Tab
from CodeGenerator import CodeGenerator

class DriverGen( object ):
   EOF            =  -1
   CR             =  '\r'
   LF             =  '\n'

   srcName        =  ''         # name of the attributed grammar file
   srcDir         =  ''         # directory of attributed grammar file
   
   codeGen        = CodeGenerator( )

   @staticmethod
   def WriteDriver( ):
      fr = os.path.join(DriverGen.srcDir, str( Tab.gramSy.name + '.frame' ))
      fn = os.path.join(DriverGen.srcDir, Tab.gramSy.name + '.py')
      fn = str(fn)
      DriverGen.codeGen.openFiles( [ fr, 'Driver.frame' ], Tab.gramSy.name + '.atg', fn, True )
      DriverGen.codeGen.CopyFramePart( '-->begin' )
      DriverGen.codeGen.CopyFramePart( '$$$' )
      DriverGen.codeGen.close( )
      os.chmod(fn, 0o755)

   @staticmethod
   def Init( f, dir ):
      assert isinstance( f, str )
      assert isinstance( dir, str )
      DriverGen.srcName = f
      DriverGen.srcDir  = dir
