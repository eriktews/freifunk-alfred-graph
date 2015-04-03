# Depending on your website, you might wanna change the size here
set term pngcairo enhanced color notransparent font 'Open Sans,14' size 900,400

# Write output to clients.png
set output 'clients.png'

# German short date style
set format x '%d.%m.%y'

# Line styles for nodes and clients
set style line 1 lc rgb '#dc0067' lt 1 lw 2 pt 5
set style line 2 lc rgb '#009ee0' lt 1 lw 2 pt 5

# Key is left top, this position is usually empty otherwise
set key left top

# We are plotting time
set xdata time

# Grid line
set style line 101 lc rgb '#808080' lt 0 lw 1

# Border line
set style line 102 lc rgb '#808080' lt 1 lw 1

# Border
set border 3 front ls 102

# Time is in unix epoc
set timefmt '%s'

# Grid defaults
set grid xtics ytics nomxtics ls 101

# TODO: ytics is 20, you might want to change it for bigger communities
set ytics 20 

# do not mirror tics, looks usually better on websites
set tics nomirror

# TODO: You might want to adjust that do your local community
#set xrange ['1413830659':*]
set xrange [*:*]

# Format is: time, nodes, wifi, totoal
plot 'all.dat' using 1:4 with lines ls 2 lw 2 title 'Clients', 'all.dat' using 1:2 with lines ls 1 lw 2 title 'Nodes'

