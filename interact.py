from bokeh.plotting import figure, gridplot, output_file, show

s1 = figure(width=250,height=250)
s1.circle([1,2,3,4], [1,2,3,4], size=10)

s2 = figure(width=250, height=250, x_range=s1.x_range)
s2.triangle([1,2,3,4],[4,3,2,1], size=10)

s3 = figure(width=250, height=250, x_range=s1.x_range)
s3.square([1,2,3,4],[4,2,1,3], size=10)

p = gridplot([[s1, s2, s3]])
output_file("panning.html")
show(p)