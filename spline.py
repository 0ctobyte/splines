#!/usr/local/bin/python3

import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', **{'family':'sans-serif', 'sans-serif':['Helvetica']})

def splerp(t, control_points):
  if len(control_points) == 1:
    return control_points[0]

  derived_points = []
  for (x0, y0), (x1, y1) in zip(control_points, control_points[1:]):
    x = x0 + t*(x1-x0)
    y = y0 + t*(y1-y0)
    derived_points.append((x, y))

  return splerp(t, derived_points)


def plot_spline(control_points, fig_name="spline"):
  interpolated_points = []
  for t in np.arange(0, 1.1, 0.1):
    interpolated_points.append(splerp(t, control_points))

  plt.figure(0)
  plt.clf()
  plt.plot([p[0] for p in interpolated_points], [p[1] for p in interpolated_points])
  plt.title('Spline Curve with ' + str(len(control_points)) + ' Control Points')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.savefig(fig_name+".svg")
  plt.show()


plot_spline([(0, 0), (3, 6)], 'spline2')
plot_spline([(0, 1), (0, 0), (1, 0)], 'spline3')
plot_spline([(0, 0), (1, 2), (2, -5), (3, 8)], 'spline4')
plot_spline([(0, 0), (1, 2), (2, -5), (3, 8), (1, 7)], 'spline5')
plot_spline([(0, 0), (1, 2), (2, -5), (3, 8), (4, 8), (5, 3)], 'spline6')
