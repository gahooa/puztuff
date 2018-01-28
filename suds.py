#!/usr/bin/python3.6
# vim:fileencoding=utf-8:ts=2:sw=2:expandtab

print()
print('Suds - Suduko Solver')
print()

INPUT = '''
5-- --1 3--
--- -65 17-
--- 4-- -25

-6- -7- -3-
-75 --- 68-
-8- -4- -1-

82- --6 ---
-56 38- ---
--1 7-- --3
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

class Puzzle():
  
  def GCEL(self, col, row):
    return self.Solving[9*row+col]
  
  # Excludes specified position from the returned ROW
  def GROW(self, col, row):
    return [self.Solving[9*row+c] for c in range(9) if c!=col]
  
  # Excludes specified position from the returned COL
  def GCOL(self, col, row):
    return [self.Solving[9*r+col] for r in range(9) if r!=row]
  
  # Excludes specified position from the returned GRP
  def GGRP(self, col, row):
    for chk in ((0,1,2),(3,4,5),(6,7,8)):
      if col in chk:  
        cols = chk
      if row in chk:
        rows = chk
    return [self.Solving[9*r+c] for r in rows for c in cols if (col,row) != (c,r)]



      
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
          self.Solving.append({1,2,3,4,5,6,7,8,9})
        else:
          self.Solving.append({val})



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
      
    
    
    output = str.join('', output)

    print(output)




p1 = Puzzle(INPUT)
p2 = Puzzle(INPUT)


p1.PrintDebug()
p1.Print()

    



