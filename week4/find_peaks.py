#!/usr/bin/env python

import sys

from classcoding import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt

def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, contf_fname, contr_fname, width, out_fname = sys.argv[1:]
    # Define what genomic region we want to analyze
    target = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart
    width = int(width)

    # Load the sample bedgraph data, reusing the function we already wrote
    forward = load_bedgraph(forward_fname, target, 0, chromlen)
    reverse = load_bedgraph(reverse_fname, target, 0, chromlen)

    # Combine tag densities, shifting by our previously found fragment width
    sample_combined = numpy.zeros(chromlen)
    sample_combined[width//2:] += forward[:-width//2] 
    sample_combined[:-width//2] += reverse[width//2:]
 
    # Load the control bedgraph data, reusing the function we already wrote
    fwd_control = load_bedgraph(contf_fname, target, 0, chromlen)
    rev_control = load_bedgraph(contr_fname, target, 0, chromlen)
    # Combine tag densities
    control_combined = fwd_control + rev_control
    

    # Adjust the control to have the same coverage as our sample
    control_coverage = numpy.sum(sample_combined, dtype = float)/numpy.sum(control_combined, dtype = float)
    control_combined = control_coverage * control_combined
    
   
    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    sample_score = bin_array(sample_combined, 1000)/1000
    control_score = bin_array(control_combined,1000)/1000

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    mean_control = numpy.mean(control_score)
    control_mean_score = numpy.maximum(control_score, mean_control)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    sample_bin_score = bin_array(sample_score, width*2)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    p_values = 1.0 - scipy.stats.poisson.cdf(sample_bin_score, mu = control_mean_score * width *2)
    print(p_values)

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    adjusted_pvals = numpy.clip(p_values, 1e-250, 2)
    adjusted_pvals = -(numpy.log10(adjusted_pvals))
    print(adjusted_pvals)

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    write_wiggle(adjusted_pvals, target,chromstart, out_fname + '.wig')

    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(adjusted_pvals, target, chromstart, chromend, width, out_fname + '.bed' )


def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()