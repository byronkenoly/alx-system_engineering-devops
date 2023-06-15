#!/usr/bin/env ruby
# regex that matches School
# the script accepts one argument

if ARGV.empty?
    puts ""
else
    puts ARGV[0].scan(/School/).join
end
