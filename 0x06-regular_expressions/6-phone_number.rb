#!/usr/bin/env ruby
# regex that matches hbtn (zero or more t's)
# the script accepts one argument

if ARGV.empty?
    puts ""
else
    puts ARGV[0].scan(/^[0-9]{10}$/).join
end
