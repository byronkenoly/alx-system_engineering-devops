#!/usr/bin/env ruby
# regex that matches hbtn (b is optional)
# the script accepts one argument

if ARGV.empty?
    puts ""
else
    puts ARGV[0].scan(/hb?tn/).join
end
