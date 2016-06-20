#-*- coding: UTF-8 -*-
from bokeh.plotting import figure, output_file, show
output_file("out.html")		#設定資料與輸出檔案
p = figure()				#利用 Bokeh 繪製圖表
p.line([1,2,3,4,5],[5,4,3,2,1])		#設定坐標
show(p)						#開啟產生的 HTML 檔