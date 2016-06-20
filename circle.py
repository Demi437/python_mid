from bokeh.plotting import figure, output_file, show
output_file("test.html")
p = figure(width=800,height=300)
p.circle([1,2,3],[2,5,3],size=[10,20,30],color=["pink","olive","gold"])
show(p)