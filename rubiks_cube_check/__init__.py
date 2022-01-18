Corners = [ "YBO", "YOG", "YGR", "YRB", "WOB", "WGO", "WRG", "WBR" ]
IndexCorners = [ [ 7, 19, 12 ], [ 1, 10, 39 ], [ 3, 37, 30 ], [ 21, 9, 28 ], [ 46, 18, 25 ], [ 52, 45, 16 ], [ 54, 36, 43 ], [ 48, 27, 34 ] ]
Edges = [ "BY", "YO", "GY", "YR", "RB", "OB", "OG", "RG", "BW", "WO", "GW", "WR", ]
IndexEdges = [ [ 20, 8 ], [ 11, 4 ], [ 38, 2 ], [ 6, 29 ], [ 31, 24 ], [ 15, 22 ], [ 13, 42 ], [ 33, 40 ], [ 26, 47 ], [ 49, 17 ], [ 44, 53 ], [ 51, 35 ], ]

'''
Проверка на 54 квадрата, 6 цветов по 9 квадратов в каждом
'''
def Phase0(Cube):
 Result = {}
 for Color in Cube:
  if Color not in Result:
   Result[Color] = 0
  Result[Color] += 1
 #print(Result)
 for Key, Value in Result.items():
  if Value != 9:
   return False
 else:
  return len(Cube) == 54 and len(Result) == 6


'''
Для подсчёта инверсий в перестановках углов кубики пронумерованы в начальном состоянии Corners.
Для каждой ячейки конфигурации находится номер кубика, который эту ячейку занимает IndexCorners.
Подсчёт инверсии подстановки — это когда большее число стоит левее чем меньшее,
реализуется двойным циклом.
Аналогично для рёбер: нумерация Edges → определяем номера рёбер в конфигурации IndexEdges →
подсчёт инверсий.
Чётность инверсий рёбер и углов должна быть чётной.
'''
def Phase1(Cube):
 #
 C = []
 for Item in IndexCorners:
  T = "".join(Cube[i - 1] for i in Item)
  for j, Corner in enumerate(Corners):
   if sorted(Corner) == sorted(T):
    C.append(j)
 #
 Result = 0
 Len = len(C)
 for i in range(Len):
  for j in range(Len - i):
   if C[i] > C[Len - j - 1]:
    Result += 1
 #print(Result, C)
 #
 C = []
 for Item in IndexEdges:
  T = "".join(Cube[i - 1] for i in Item)
  for j, Edge in enumerate(Edges):
   if sorted(Edge) == sorted(T):
    C.append(j)
 #
 Len = len(C)
 for i in range(Len):
  for j in range(Len - i):
   if C[i] > C[Len - j - 1]:
    Result += 1
 #print(Result, C)
 return Result > 0 and Result % 2 == 0


'''
Для каждой стороны уголков Indexes введены числовое обозначение (индексы) Corners.
Для конфигурации кубика-рубика сумма цифр на двух противоположных гранях Mod3
должна делиться на 3 (инвариант углов): Result.
Любой поворот граней сохраняет инварианты углов.
'''
def Phase2(Cube):
 C = Cube.copy()
 Mod3 = [ [ 19, 21, 25, 27, 37, 39, 43, 45, ], [ 10, 12, 16, 18, 28, 30, 34, 36, ], [ 1, 3, 7, 9, 46, 48, 52, 54, ], ]
 #
 for Item in IndexCorners:
  T = "".join(Cube[i - 1] for i in Item)
  for Corner in Corners:
   if sorted(Corner) == sorted(T):
    for i in Item:
     C[i - 1] = Corner.find(Cube[i - 1])
 #
 Result = [0, 0, 0]
 for i, Mod in enumerate(Mod3):
  for j in Mod:
   if isinstance(C[j - 1], int):
    Result[i] += C[j - 1]
   else:
    return False
 #
 #print(Result)
 for R in Result:
  if R == 0 or R % 3 != 0:
   return False
 else:
  return True


'''
Каждое ребро Indexes пронумеровано по индексам Edges.
Сумма цифр на противоположных гранях Mod2
должна делиться на 2 (инвариант рёбер): Result.
Любой поворот граней сохраняет инварианты граней.
'''
def Phase3(Cube):
 C = Cube.copy()
 Mod2 = [ [2, 8, 47, 53, ], [ 22, 24, 40, 42, ], [ 11, 17, 29, 35, ], [ 20, 26, 38, 44, ], [ 13, 15, 31, 33, ], [ 4, 6, 49, 51, ], ]
 #
 for Item in IndexEdges:
  T = "".join(Cube[i - 1] for i in Item)
  for Edge in Edges:
   if sorted(Edge) == sorted(T):
    for i in Item:
     C[i - 1] = Edge.find(Cube[i - 1])
 #
 Result = [0, 0, 0, 0, 0, 0]
 for i, Mod in enumerate(Mod2):
  for j in Mod:
   if isinstance(C[j - 1], int):
    Result[i] += C[j - 1]
   else:
    return False
 #
 #print(Result)
 for R in Result:
  if R % 2 != 0:
   return False
 else:
  return True


def Check(Cube):
 P0 = Phase0(Cube)
 P1 = Phase1(Cube)
 P2 = Phase2(Cube)
 P3 = Phase3(Cube)
 return P0 and P1 and P2 and P3

