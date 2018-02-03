#!/usr/bin/python3.6
# vim:fileencoding=utf-8:ts=2:sw=2:expandtab

import itertools

print()
print('Suds - Suduko Solver')
print()

# Easy
INPUT = '''
5----13--
----6517-
---4---25
-6--7--3-
-75---68-
-8--4--1-
82---6---
-5638----
--17----3
'''

# Medium
INPUT = '''
8625-----
-54-----8
-1--6-2--
5376----2
6--7-4--3
2----5976
--5-1--3-
3-----61-
-----8524
'''

# Hard
INPUT = '''
---67----
-26-4-3--
-4----89-
8----5---
13--6--82
---8----4
-83----4-
--5-8-76-
----54---
'''

PrintTemplate = ('''
┌───┬───┬───╥───┬───┬───╥───┬───┬───┐
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
╞═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╡
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
╞═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╡
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
├───┼───┼───╫───┼───┼───╫───┼───┼───┤
│ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 ║ 3 │ 3 │ 3 │
└───┴───┴───╨───┴───┴───╨───┴───┴───┘
''').strip()


DebugTemplate = ('''
┌─────────┬─────────┬─────────╥─────────┬─────────┬─────────╥─────────┬─────────┬─────────┐
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
╞═════════╪═════════╪═════════╬═════════╪═════════╪═════════╬═════════╪═════════╪═════════╡
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
╞═════════╪═════════╪═════════╬═════════╪═════════╪═════════╬═════════╪═════════╪═════════╡
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
├─────────┼─────────┼─────────╫─────────┼─────────┼─────────╫─────────┼─────────┼─────────┤
│         │         │         ║         │         │         ║         │         │         │
│333333333│333333333│333333333║333333333│333333333│333333333║333333333│333333333│333333333│
│         │         │         ║         │         │         ║         │         │         │
└─────────┴─────────┴─────────╨─────────┴─────────┴─────────╨─────────┴─────────┴─────────┘
''').strip()

###############################################################################


class CELL(set):
  def __init__(self, col, row, val):
    set.__init__(self, val)
    self.col = col
    self.row = row
  
  def __hash__(self):
    return hash(id(self))

  def __repr__(self):
    return f'CELL({self.col}, {self.row}, {tuple(self)})'


class Puzzle():
  
  def GCEL(self, col, row):
    return {self.Solving[9*row+col]}
  
  def GROW(self, col, row):
    return {self.Solving[9*row+c] for c in range(9)}
  
  def GCOL(self, col, row):
    return {self.Solving[9*r+col] for r in range(9)}
  
  def GGRP(self, col, row):
    for chk in ((0,1,2),(3,4,5),(6,7,8)):
      if col in chk:  
        cols = chk
      if row in chk:
        rows = chk
    return {self.Solving[9*r+c] for r in rows for c in cols}



      
  def __init__(self, text):
    self.Original = []
    self.Solving = []

    row = -1
    for line in text.strip().split('\n'):
      line = line.strip()
      
      # Skip blank lines
      if line == '':
        continue

      row += 1
        
      # Sanity check!
      if row >= 9:
        raise ValueError(f'More than 9 non-empty rows encountered')
      
      col = -1
      for char in line:
        # Skip spaces and other characters
        if char not in '-123456789':
          continue

        # Advance to next column
        col += 1

        # Sanity check!
        if col >= 9:
          raise ValueError(f'More than 9 columns encountered in (non-empty) row #{row}')

        # Convert to inteeger or None
        if char == '-':
          val = None
        else:
          val = int(char)

        # Store in Original
        self.Original.append(val)
      
        # Build possibilities
        if val is None:
          self.Solving.append(CELL(col, row, (1,2,3,4,5,6,7,8,9)))
        else:
          self.Solving.append(CELL(col, row, (val,)))

  def Solve(self):

    # First tactic is to see if a cell only has a single possibility.  If that is true then
    # we can discard it from all other positions on that row, col, and grp
    for row in range(9):
      for col in range(9):
        CEL = self.GCEL(col,row)
        ROW = self.GROW(col,row)
        COL = self.GCOL(col,row)
        GRP = self.GGRP(col,row)

        (CEL1,) = CEL #Unpack
   
        if len(CEL1) == 1:
          (val,) = CEL1 #unpack value
#          import pdb; pdb.set_trace()
          for c in (ROW | COL | GRP) - CEL:
            if val in c:
              print(f'On {CEL1} Discard {val} from {c}')
              c.discard(val)
   
    # Second tactic is to see if any of the possible values in a cell are not present on 
    # the row, col, or group.  If any one of these is true then we know we have an answer.
    for row in range(9):
      for col in range(9):

        CEL = self.GCEL(col,row)
        ROW = self.GROW(col,row)
        COL = self.GCOL(col,row)
        GRP = self.GGRP(col,row)
        
        CEL1, = CEL #unpack

#        import pdb
#        pdb.set_trace()

        NotFound = False
        for VAL in CEL1:
          for other_cel in GRP-CEL: 
            if VAL in other_cel:
              break
          else:
            NotFound = True
          
          for other_cel in ROW-CEL: 
            if VAL in other_cel:
              break
          else:
            NotFound = True
          
          for other_cel in COL-CEL: 
            if VAL in other_cel:
              break
          else:
            NotFound = True
          
          if NotFound:
            CEL1.clear()
            CEL1.add(VAL)
            break
            


  def SP(self):
    lst = None
    cnt = 0
    i = 0

    print(f'\n{"#"*80}\n')

    while True:
      i += 1
      lst = cnt
      cnt = sum(1 for CEL in self.Solving if len(CEL) == 1)
      
      if cnt == lst:
        break
      
      print(('Solved' if i > 1 else 'Started with') +  f' {cnt} of 81')
      self.Solve()
      self.Print()

      input('Press Enter')
      
    self.PrintDebug()

  def Print(self):
    output = []
    
    output.append('Initial Puzzle State\n\n')

    # split template into 82 parts (81 delimiters)
    parts = PrintTemplate.split('3')
    
    # Start the output by popping the first item of the 82, leaving 81 parts
    output.append(parts.pop(0))

    for val,part in zip(self.Original, parts):
      output.append(str(val or ' '))
      output.append(part)

    output.append('\n\n')
    output.append('Current Solve State\n\n')
    
    # split template into 82 parts (81 delimiters)
    parts = PrintTemplate.split('3')
    
    # Start the output by popping the first item of the 82, leaving 81 parts
    output.append(parts.pop(0))

    # Look at the current solve state and only print the number if it is the only number in the set
    for val,part in zip(self.Solving, parts):
      output.append(str(tuple(val)[0]) if len(val) == 1 else ' ')
      output.append(part)
    
    output.append('\n')
    output = str.join('', output)

    print(output)
    
    
  def PrintDebug(self):
    output = []

    output.append('Possibilities State\n\n')
    
    # split template into 82 parts (81 delimiters)
    parts = DebugTemplate.split('333333333')
    
    # Start the output by popping the first item of the 82, leaving 81 parts
    output.append(parts.pop(0))

    # Look at the current solve state and only print the number if it is the only number in the set
    for val,part in zip(self.Solving, parts):
      output.append(''.join(str(n) if n in val else ' ' for n in (1,2,3,4,5,6,7,8,9)))
      output.append(part)
      
    
    output.append('\n')
    
    output = str.join('', output)

    print(output)




p1 = Puzzle(INPUT)
p2 = Puzzle(INPUT)


p1.SP()

    



