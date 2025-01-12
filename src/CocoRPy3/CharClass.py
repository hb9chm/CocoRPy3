#-------------------------------------------------------------------------
#Basics.py -- Some basic definitions
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
#-------------------------------------------------------------------------
from Trace import Trace

class CharClass( object ):
   classes = [ ]
   dummyName = ord('A')

   charSetSize = 256     # must be a multiple of 16

   def __init__( self, name, s ):
      assert isinstance( name, str )
      assert isinstance( s, set )
      if name == "#":
         name = "#" + chr(CharClass.dummyName)
         CharClass.dummyName += 1
      self.n = len(CharClass.classes)       # class number
      self.name = name            # class name
      self.set = s                # set representing the class
      CharClass.classes.append(self)

   @staticmethod
   def Find( nameOrSet ):
      assert isinstance( nameOrSet, (str, set) )
      if isinstance(nameOrSet,str):
         name = nameOrSet
         for c in CharClass.classes:
            if c.name == name:
               return c
         return None
      else:
         s = nameOrSet
         for c in CharClass.classes:
            if s == c.set: #Sets.Equals(s, c.set):
               return c
         return None

   @staticmethod
   def Set( i ):
      assert isinstance( i, int )
      return CharClass.classes[i].set

   @staticmethod
   def Ch( ch ):
      assert isinstance( ch, str ) or isinstance( ch, int )
      if isinstance( ch, str ):
         ch = ord(ch)
      if ch < ord(' ') or ch >= 127 or ch == ord('\'') or ch == ord('\\'):
         return str(ch)
      else:
         return "'" + chr(ch) + "'"

   @staticmethod
   def WriteClasses( ):
      for c in CharClass.classes:
         Trace.Write(str(c.name), -10)
         Trace.Write(': ')
         c.WriteSet( )
         Trace.WriteLine()
      Trace.WriteLine()

   def WriteSet( self ):
      s = self.set.copy()
      try:
         s.remove('ANYCHAR')
      except KeyError:
         pass

      i = 0
      mx = max(s) + 1
      while i < mx:
         while i < mx and (i not in s):
            i += 1
         if i == mx:
            break
         j = i
         while i < mx and (i in s):
            i += 1
         if j < (i - 1):
            Trace.Write(str(CharClass.Ch(j)) + ".." + str(CharClass.Ch(i-1)) + " ")
         else:
            Trace.Write(str(CharClass.Ch(j) + " "))
