#!/usr/bin/env python
#
# This file is part of pyasn1-modules software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pyasn1/license.html
#
# Read ASN.1/PEM X.509 CRMF request on stdin, parse into
# plain text, then build substrate from it
#
import sys

from pyasn1.codec.der import decoder, encoder

from pyasn1_modules import pem, rfc2560

if len(sys.argv) != 1:
    print(
        """Usage:
$ cat ocsp-request.pem | %s"""
        % sys.argv[0]
    )
    sys.exit(-1)

ocspReq = rfc2560.OCSPRequest()

substrate = pem.readBase64FromFile(sys.stdin)
if not substrate:
    sys.exit(0)

cr, rest = decoder.decode(substrate, asn1Spec=ocspReq)

print(cr.prettyPrint())

assert encoder.encode(cr) == substrate, "OCSP request recode fails"
