#!/usr/bin/env ruby

phone_pattern = /\A\d{10}\z/

if ARGV[0] =~ phone_pattern
  puts ARGV[0]
end
