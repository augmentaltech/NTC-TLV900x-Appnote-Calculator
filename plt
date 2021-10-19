set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5
set xlabel "Temperature"
set ylabel "Voltage"
set term png
set output "curve.png"

plot 'curve.csv' with linespoints linestyle 1 \
    title 'Real T/U curve'

pause -1
