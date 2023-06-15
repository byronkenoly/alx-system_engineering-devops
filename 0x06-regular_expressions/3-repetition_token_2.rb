#!/usr/bin/env ruby
# regex that matches hbtn (one or more t's)
# the script accepts one argument

if ARGV.empty?
    puts ""
else
    puts ARGV[0].scan(/hbt+n/).join
end
