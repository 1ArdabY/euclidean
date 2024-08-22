import math

def euclideanDistance(point1, point2):
  """İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: İlk nokta, bir demet olarak (x1, y1).
    point2: İkinci nokta, bir demet olarak (x2, y2).

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Nokta örnekleri
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

# Mesafelerin hesaplanması
distances = []
for i in range(len(points) - 1):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)
