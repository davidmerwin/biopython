# Copyright 2002 by Jeffrey Chang.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

from Bio.config.DBRegistry import CGIDB, DBGroup, EUtilsDB
from _support import *

from Martel import *

proxy_error_expr = has_expr(Alt(Str("500"), Str("502")) + Str(" Proxy Error"))
diagnostic_error_expr = has_str("WWW Error 500 Diagnostic")
error_expr = Str("ERROR")

ncbi_failures=[
    (proxy_error_expr, "proxy error"),
    (diagnostic_error_expr, "diagnostic error"),
    (error_expr, "ERROR"),
    (html_expr, "I got HTML and shouldn't have"),
    (Str("Please try again later"), "Please try again later"),
    (Str("The sequence has been intentionally withdrawn"),
     "Sequence withdrawn"),
    (blank_expr, "No data returned")
    ]

nucleotide_genbank_eutils = EUtilsDB(
        name = "nucleotide-genbank-eutils",
        doc = "Retrieve nucleotide GenBank sequences from NCBI using EUtils",
        delay = 5.0,
        db = "nucleotide",
        rettype = "gb",
        failure_cases = ncbi_failures
        )

# If the id is not in the database, I get a message like:
# ERROR : GenPept does not exist for gi = 433174
not_exist_expr = Str("ERROR") + Re("[^d]*") + Str("does not exist for gi")

protein_genbank_eutils = EUtilsDB(
        name = "protein-genbank-eutils",
        doc = "Retrieve protein GenPept sequences from NCBI using EUtils",
        delay = 5.0,
        db = "protein",
        rettype = "gp",
        failure_cases = ncbi_failures+[(not_exist_expr, "GI does not exist")]
        )
