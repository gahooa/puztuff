#!/usr/bin/python3.6
# vim:fileencoding=utf-8:ts=2:sw=2:expandtab

import itertools

print()
print('Suds - Suduko Solver')
print()

# Easy
INPUT = '''
5 - - - - 1 3 - -
- - - - 6 5 1 7 -
- - - 4 - - - 2 5
- 6 - - 7 - - 3 -
- 7 5 - - - 6 8 -
- 8 - - 4 - - 1 -
8 2 - - - 6 - - -
- 5 6 3 8 - - - -
- - 1 7 - - - - 3
'''

# Medium
INPUT = '''
8 6 2 5 - - - - -
- 5 4 - - - - - 8
- 1 - - 6 - 2 - -
5 3 7 6 - - - - 2
6 - - 7 - 4 - - 3
2 - - - - 5 9 7 6
- - 5 - 1 - - 3 -
3 - - - - - 6 1 -
- - - - - 8 5 2 4
'''

# Hard
INPUT = '''
- - - 6 7 - - - -
- 2 6 - 4 - 3 - -
- 4 - - - - 8 9 -
8 - - - - 5 - - -
1 3 - - 6 - - 8 2
- - - 8 - - - - 4
- 8 3 - - - - 4 -
- - 5 - 8 - 7 6 -
- - - - 5 4 - - -
'''

# 554
INPUT = '''
4 _ _ 7 6 _ _ 2 _
_ 2 _ _ _ _ _ 7 _
_ _ _ 4 _ 2 _ _ 8
_ 7 _ _ _ _ 6 _ _
_ 8 _ 9 3 6 _ 4 _
_ _ 1 _ _ _ _ 5 _
7 _ _ 5 _ 1 _ _ _
_ 9 _ _ _ _ _ 1 _
_ 5 _ _ 8 7 _ _ 9
'''

INPUT = '''
_ _ 8 _ _ _ 1 _ _
9 _ _ 2 3 _ _ _ 5
_ _ _ _ 1 6 _ _ _
_ 3 6 _ 8 _ _ _ 7
_ 7 9 _ _ _ 6 5 _
2 _ _ _ 6 _ 4 3 _
_ _ _ 4 9 _ _ _ _
5 _ _ _ 7 1 _ _ 9
_ _ 4 _ _ _ 3 _ _
'''

INPUT = '''
_ _ _ _ _ 7 _ _ 8
_ _ _ 3 4 _ 9 _ _
9 _ 8 _ _ _ _ 1 7
_ 6 _ 4 _ _ _ _ 1
_ _ 9 _ _ _ 8 _ _
1 _ _ _ _ 5 _ 2 _
8 2 _ _ _ _ 7 _ 6
_ _ 1 _ 7 4 _ _ _
5 _ _ 2 _ _ _ _ _
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
        if char not in '_-123456789':
          continue

        # Advance to next column
        col += 1

        # Sanity check!
        if col >= 9:
          raise ValueError(f'More than 9 columns encountered in (non-empty) row #{row}')

        # Convert to inteeger or None
        if char in '-_':
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

    for row in range(9):
      for col in range(9):
        CEL = self.GCEL(col,row)
        ROW = self.GROW(col,row)
        COL = self.GCOL(col,row)
        GRP = self.GGRP(col,row)

        (CEL1,) = CEL #Unpack
   
        # First tactic is to see if a cell only has a single possibility.  If that is true then
        # we can discard it from all other positions on that row, col, and grp
        if len(CEL1) == 1:
          (val,) = CEL1 #unpack value
#          import pdb; pdb.set_trace()
          for c in (ROW | COL | GRP) - CEL:
            if val in c:
#              print(f'On {CEL1} Discard {val} from {c}')
              c.discard(val)


   
        # Second tactic is to see if any of the possible values in a cell are not present on 
        # the row, col, or group.  If any one of these is true then we know we have an answer.
        NotFound = False
        for val in CEL1:
          for other_cel in GRP-CEL: 
            if val in other_cel:
              break
          else:
            NotFound = True
          
          for other_cel in ROW-CEL: 
            if val in other_cel:
              break
          else:
            NotFound = True
          
          for other_cel in COL-CEL: 
            if val in other_cel:
              break
          else:
            NotFound = True
          
          if NotFound:
            CEL1.clear()
            CEL1.add(val)
            break
        
        # Third tactic is to see if any numbers ONLY exist in the current subrow or subcolumn
        # inside the current group.  If they do then remove them from that row or column in 
        # the other 2 groups that it goes through

        for RC in ROW,COL:
          subset = GRP.intersection(RC)
          subset_numbers = set(itertools.chain(*(s for s in subset if len(s) > 1)))
          others = GRP - subset
          others_numbers = set(itertools.chain(*others))
          extern = RC - subset
          
          only_in_subset = subset_numbers - others_numbers
        
          if only_in_subset:
            for cel in extern:
              for n in only_in_subset:
                if n in cel:
                  print(f'Discarding {n} from {cel} because subset only has {only_in_subset}')
                  cel.remove(n)





  def SP(self):
    lst = None
    cur = None 
    i = 0

    print(f'\n{"#"*80}\n')

    while True:
      i += 1
      lst = cur
      cur = [sorted(cel) for cel in self.Solving]
      cnt = sum(1 for cel in self.Solving if len(cel) == 1)
      cntp = sum(len(cel) for cel in self.Solving if len(cel) > 1)
      
      if cur == lst:
        break
      
      self.Solve()
      
      print(('Solved' if i > 1 else 'Started with') +  f' {cnt} of 81 solved with {cntp} possiblities left')
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

    



