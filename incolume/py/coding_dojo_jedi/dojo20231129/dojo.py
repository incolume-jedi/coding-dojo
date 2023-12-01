"""Dojo."""
def land_perimeter_0(arr):
    """__author__: https://www.codewars.com/users/egaletsky"""
   
    I,J = len(arr), len(arr[0])
    
    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0   or arr[i-1][j] == 'O': P += 1
                if i == I-1 or arr[i+1][j] == 'O': P += 1
                if j == 0   or arr[i][j-1] == 'O': P += 1
                if j == J-1 or arr[i][j+1] == 'O': P += 1
                   
                  
    return 'Total land perimeter: ' + str(P)

def land_perimeter_1(grid):
    """__author__: https://www.codewars.com/users/MoinoFrankman."""
    s, m = len(grid), len(grid[0])
    ans = 0
    for x in range(s):
        for y in range(m):
            if grid[x][y] == 'X':
                ans += 4
                if x < s - 1 and grid[x+1][y] == 'X':
                    ans -= 2
                if y < m - 1 and grid[x][y+1] == 'X':
                    ans -= 2
                    
    return ('Total land perimeter: {}'.format(ans))

def land_perimeter_2(arr):
  """__author__: https://www.codewars.com/users/Alser69rus"""
  perimetr=0
  height=len(arr)
  for y in range(height):
    width=len(arr[y])
    for x in range(width):
      if arr[y][x]=='X':
        if x==0 or arr[y][x-1]=='O':perimetr+=1
        if x==width-1 or arr[y][x+1]=='O':perimetr+=1
        if y==0 or arr[y-1][x]=='O':perimetr+=1
        if y==height-1 or arr[y+1][x]=='O':perimetr+=1
  return 'Total land perimeter: '+str(perimetr)


def land_perimeter_3(arr):
    """__author__: https://www.codewars.com/users/daddepledge"""
    land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2
    return 'Total land perimeter: ' + str(''.join(arr).count('X') * 4 - land(arr) - land(zip(*arr)))


def land_permetercal(matriz: list) -> int:
    """Calcular perímetro de um espaço."""
    def land_next(line_or_column: list) -> int:
        """Count land neighbord."""
        return sum(t == ('X', 'X') for r in line_or_column for t in zip(r, r[1:])) * 2
    
    def calc_perim(arr: list) -> int:
        """Calculate perimeter."""
        return ''.join(arr).upper().count('X') * 4 - land_next(arr) - land_next(zip(*arr))
    
    return f'Total land perimeter: {calc_perim(matriz)}'
    
