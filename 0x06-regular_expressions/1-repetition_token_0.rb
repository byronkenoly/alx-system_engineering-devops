#!/usr/bin/env ruby
# regex that matches hbtn (btwn 2-5 t's)
# the script accepts one argument

if ARGV.empty?
    puts ""
else
    puts ARGV[0].scan(/hbt{2,5}n/).join
end
